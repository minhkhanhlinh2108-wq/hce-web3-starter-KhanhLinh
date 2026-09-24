import os
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def analyze_wallet(address):
    # Lấy API Key từ biến môi trường
    api_key = os.environ.get("ETHERSCAN_API_KEY")
    if not api_key:
        print("Lỗi: Không tìm thấy khóa API trong biến môi trường ETHERSCAN_API_KEY.")
        return

    # Tính mốc thời gian 90 ngày trước
    start_time_90_days = int((datetime.now() - timedelta(days=3650)).timestamp())
    
    transactions = []
    page = 1
    
    print("Đang tải dữ liệu từ Etherscan...")
    # Vòng lặp xử lý phân trang (đảm bảo lấy đủ nếu > 10.000 giao dịch)
    while True:
        url = f"https://api.etherscan.io/v2/api?chainid=1&module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page={page}&offset=10000&sort=asc&apikey={api_key}"
        response = requests.get(url).json()
        
        if response['status'] == '0':
            if response['message'] == 'No transactions found':
                if page == 1:
                    print("Vi khong co giao dich trong ky")
                    return
                break
            else:
                print(f"Lỗi từ API: {response['result']}")
                return
                
        txs = response['result']
        if not txs:
            break
            
        transactions.extend(txs)
        if len(txs) < 10000:
            break
        page += 1

    # Lọc các giao dịch trong 90 ngày và sắp xếp tăng dần theo thời gian
    filtered_txs = [tx for tx in transactions if int(tx['timeStamp']) >= start_time_90_days]
    filtered_txs.sort(key=lambda x: int(x['timeStamp']))

    if not filtered_txs:
        print("Vi khong co giao dich trong ky")
        return

    balance = 0.0
    total_in = 0.0
    total_out = 0.0
    times = []
    balances = []

    print(f"{'Thời gian':<20} | {'Loại':<5} | {'Số tiền (ETH)':<15} | {'Phí (ETH)':<15} | {'Số dư lũy kế':<15}")
    print("-" * 80)

    for tx in filtered_txs:
        dt_object = datetime.fromtimestamp(int(tx['timeStamp'])).strftime("%Y-%m-%d %H:%M")
        
        # Chia cho 10^18 để đổi từ wei sang ETH
        value_eth = int(tx['value']) / (10**18)
        fee_eth = (int(tx['gasUsed']) * int(tx['gasPrice'])) / (10**18)
        is_error = tx['isError'] == '1'
        
        tx_type = ""
        amount = 0.0
        
        if tx['to'].lower() == address.lower():
            # Dòng tiền vào
            if not is_error:
                balance += value_eth
                total_in += value_eth
                tx_type = "Vào"
                amount = value_eth
            else:
                continue # Giao dịch vào bị lỗi thì không tính
                
        elif tx['from'].lower() == address.lower():
            # Dòng tiền ra
            tx_type = "Ra"
            if not is_error:
                balance -= (value_eth + fee_eth)
                total_out += (value_eth + fee_eth)
                amount = value_eth
            else:
                # Giao dịch thất bại vẫn bị trừ phí gas
                balance -= fee_eth
                total_out += fee_eth
                amount = 0.0
        else:
            continue

        times.append(dt_object)
        balances.append(balance)
        
        print(f"{dt_object:<20} | {tx_type:<5} | {amount:<15.6f} | {fee_eth:<15.6f} | {balance:<15.6f}")

    print("-" * 80)
    print(f"Tổng vào: {total_in:.6f} ETH")
    print(f"Tổng ra: {total_out:.6f} ETH")
    print(f"Số dư cuối kỳ: {balance:.6f} ETH")

    # Vẽ biểu đồ đường
    plt.figure(figsize=(10, 5))
    plt.plot(times, balances, marker='o', linestyle='-', color='b')
    plt.title(f'Biến động số dư ví trong 90 ngày')
    plt.xlabel('Thời gian')
    plt.ylabel('Số dư (ETH)')
    # Ẩn bớt nhãn trục x nếu quá nhiều để tránh rối mắt
    if len(times) > 10:
        plt.xticks(times[::len(times)//10], rotation=45)
    else:
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("bieu_do.png")
print("Đã lưu biểu đồ thành tệp bieu_do.png trong thư mục hiện tại.")

if __name__ == "__main__":
    # Thay địa chỉ ví dưới đây bằng địa chỉ mẫu giảng viên cung cấp
    target_wallet = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
    analyze_wallet(target_wallet)