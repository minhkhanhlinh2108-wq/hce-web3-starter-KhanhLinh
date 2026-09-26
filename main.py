import os
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def analyze_wallet(address, days=90):
    # Lay API Key tu bien moi truong theo quy tac AGENTS.md
    api_key = os.environ.get("ETHERSCAN_API_KEY")
    if not api_key:
        print("Loi: Khong tim thay khoa API trong bien moi truong ETHERSCAN_API_KEY.")
        return

    # Tinh moc thoi gian can phan tich (mac dinh 90 ngay theo SPEC.md)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp())
    
    transactions = []
    page = 1
    
    print(f"Dang tai du lieu tu Etherscan cho vi {address} trong {days} ngay qua...")
    # Vong lap xu ly phan trang (dam bao lay du neu > 10.000 giao dich)
    while True:
        url = f"https://api.etherscan.io/v2/api?chainid=1&module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page={page}&offset=10000&sort=asc&apikey={api_key}"
        response = requests.get(url).json()
        
        # Kiem tra trang thai phan hoi truoc khi xu ly du lieu (quy tac AGENTS.md)
        if response.get('status') == '0':
            if response.get('message') == 'No transactions found':
                if page == 1:
                    print("Vi khong co giao dich trong ky")
                    return
                break
            else:
                print(f"Loi tu API: {response.get('result')}")
                return
                
        txs = response.get('result', [])
        if not txs:
            break
            
        transactions.extend(txs)
        if len(txs) < 10000:
            break
        page += 1

    # Loc cac giao dich trong thoi gian quy dinh va sap xep tang dan theo thoi gian (R6)
    filtered_txs = [tx for tx in transactions if int(tx['timeStamp']) >= start_time]
    filtered_txs.sort(key=lambda x: int(x['timeStamp']))

    if not filtered_txs:
        print("Vi khong co giao dich trong ky")
        return

    balance = 0.0
    total_in = 0.0
    total_out = 0.0
    times = []
    balances = []

    print(f"{'Thoi gian':<20} | {'Loai':<5} | {'So tien (ETH)':<15} | {'Phi (ETH)':<15} | {'So du luy ke':<15}")
    print("-" * 80)

    for tx in filtered_txs:
        dt_object = datetime.fromtimestamp(int(tx['timeStamp'])).strftime("%Y-%m-%d %H:%M")
        
        # Chia cho 10^18 de doi tu wei sang ETH truoc khi hien thi (R5 va quy tac AGENTS.md)
        value_eth = int(tx['value']) / (10**18)
        fee_eth = (int(tx['gasUsed']) * int(tx['gasPrice'])) / (10**18)
        is_error = tx['isError'] == '1'
        
        tx_type = ""
        amount = 0.0
        
        if tx['to'].lower() == address.lower():
            # R1: Dong tien vao
            if not is_error:
                balance += value_eth
                total_in += value_eth
                tx_type = "Vao"
                amount = value_eth
            else:
                continue # Giao dich vao bi loi thi khong ghi nhan
                
        elif tx['from'].lower() == address.lower():
            # R2: Dong tien ra
            tx_type = "Ra"
            if not is_error:
                # R3: So tien thuc tru = gia tri chuyen + phi giao dich
                balance -= (value_eth + fee_eth)
                total_out += (value_eth + fee_eth)
                amount = value_eth
            else:
                # R4: Giao dich that bai van bi tru phi gas
                balance -= fee_eth
                total_out += fee_eth
                amount = 0.0
        else:
            continue

        times.append(dt_object)
        balances.append(balance)
        
        print(f"{dt_object:<20} | {tx_type:<5} | {amount:<15.6f} | {fee_eth:<15.6f} | {balance:<15.6f}")

    print("-" * 80)
    print(f"Tong vao: {total_in:.6f} ETH")
    print(f"Tong ra: {total_out:.6f} ETH")
    print(f"So du cuoi ky: {balance:.6f} ETH")

    # Ve bieu do duong
    plt.figure(figsize=(10, 5))
    plt.plot(times, balances, marker='o', linestyle='-', color='b')
    plt.title(f'Bien dong so du vi trong {days} ngay')
    plt.xlabel('Thoi gian')
    plt.ylabel('So du (ETH)')
    # An bot nhan truc x neu qua nhieu de tranh roi mat
    if len(times) > 10:
        plt.xticks(times[::len(times)//10], rotation=45)
    else:
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("bieu_do.png")
    print("Da luu bieu do thanh tep bieu_do.png trong thu muc hien tai.")

if __name__ == "__main__":
    # Thay dia chi vi duoi day bang dia chi vi can phan tich
    target_wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
    # Mac dinh phan tich 90 ngay theo SPEC.md; co the tuy chon tham so days neu can mo rong
    analyze_wallet(target_wallet, days=90)