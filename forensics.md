# Kết quả Lab 3 - Điều tra giao dịch (Forensics)

**Mã băm giao dịch (Transaction Hash):** `0x15482ae20c17d95d6c46280a8c76d8385742ddd7528ceb9534eb0fb948af676d`  
**Mạng kiểm thử:** Ethereum Sepolia Testnet

## Phần 1: Ý nghĩa các trường dữ liệu trong giao dịch

| Trường | Giá trị thực tế (từ tx hash) | Ý nghĩa | Vì sao người làm nghiệp vụ cần |
| :--- | :--- | :--- | :--- |
| Status | Thành công (`Success / 0x1`) | Thành công hay thất bại | Giao dịch thất bại vẫn mất phí — ảnh hưởng hạch toán |
| Block | `11771075` | Số thứ tự khối chứa giao dịch | Xác định thời điểm ghi nhận |
| Timestamp | `2026-09-24 09:17:24 UTC` (16:17:24 UTC+7) | Thời gian | Mốc ghi nhận doanh thu / chi phí |
| From / To | **From:** `0xee917bc552f81fe4db72025e05f146919b3b4032`<br>**To:** `0xafb64eef8093cf3dc4e2c51bb1d18e16afddb6f5` | Ví gửi / ví nhận (đều là ví cá nhân EOA) | Đối tượng cần xác minh danh tính; phân biệt ví cá nhân và hợp đồng thông minh |
| Value | `0.01 ETH` | Số tiền chuyển | Giá trị giao dịch |
| Transaction Fee | `0.000053956450443 ETH` (~0.000054 ETH) | Phí thực trả | Chi phí giao dịch, cần hạch toán riêng |
| Gas Price | `2.569354783 Gwei` (2,569,354,783 wei) | Đơn giá phí (Effective Gas Price) | Giải thích vì sao cùng một giao dịch mà phí khác nhau |
| Gas Limit | `31,500` | Mức gas tối đa ví gửi cho phép dùng | Đặt quá thấp → giao dịch thất bại vì hết gas (Out of Gas) nhưng vẫn mất phí |
| Gas Used | `21,000` (66.67% Gas Limit) | Lượng gas thực tế đã tiêu | Cùng Gas Price với Gas Used tính ra phí: Transaction Fee = Gas Used × Gas Price. 21,000 gas là mức chuẩn cơ sở của giao dịch chuyển ETH giữa hai ví EOA |
| Nonce | `1` | Số thứ tự giao dịch của ví gửi | Phát hiện giao dịch bị bỏ sót hoặc thay thế |
| Input Data | `0x` | Dữ liệu đính kèm gọi hàm | Dữ liệu trống (`0x`) chứng minh đây là giao dịch chuyển tiền thuần túy, không gọi hàm smart contract |

## Phần 2: Trả lời câu hỏi điều tra (Từ mã băm giao dịch & Đối chiếu hợp đồng USDT)

### 1. Hợp đồng bạn xem có công bố mã nguồn đã xác thực không?  
-> **Trả lời:**
- **Phân tích từ mã băm (`0x1548...`):** Giao dịch này là giao dịch chuyển Native ETH trực tiếp giữa hai tài khoản cá nhân thông thường (**EOA** - *Externally Owned Account*), từ ví `0xee91...` đến ví `0xafb6...`. Trường `contractAddress` là `null`, mã bytecode của địa chỉ nhận là `0x` và `Input Data` trống (`0x`). Giao dịch **không tương tác hay gọi đến bất kỳ hợp đồng thông minh (Smart Contract) nào**, do đó **không có mã nguồn hợp đồng** để công bố hay xác thực (không xuất hiện tab *Contract* hay dấu tích xanh xác thực trên Etherscan).
- **Đối chiếu với hợp đồng token USDT (`0xdAC17F958D2ee523a2206206994597C13D831ec7`):** **Có.** Mã nguồn của hợp đồng USDT đã được đơn vị phát hành (Tether) công bố công khai và xác thực hoàn toàn trên Etherscan (*Contract Source Code Verified* với biểu tượng dấu tích xanh), đảm bảo mã nguồn Solidity công khai khớp chính xác 100% với Bytecode đang thực thi trên blockchain.

### 2. Tổng cung của đồng đó là bao nhiêu? Đọc ra từ hàm nào?  
-> **Trả lời:**
- **Phân tích từ mã băm (`0x1548...`):** Đồng tiền được giao dịch trong mã băm là **ETH** (giá trị chuyển là `0.01 ETH`). ETH là đồng tiền gốc (Native Cryptocurrency) của mạng lưới Ethereum, được điều tiết trực tiếp ở tầng giao thức đồng thuận (Consensus layer) chứ không phải token ERC-20 được phát hành qua Smart Contract. Do đó, **không có địa chỉ hợp đồng và không có hàm `totalSupply()`** nào trên blockchain để đọc ra tổng cung của ETH. Tổng cung lưu hành của ETH trên toàn mạng hiện tại được quản lý bởi thuật toán phát hành/đốt (EIP-1559) của mạng Ethereum (hiện tại dao động khoảng ~120 triệu ETH).
- **Đối chiếu với hợp đồng token USDT:** Tổng cung đọc ra từ hàm `totalSupply()` trong tab **Read Contract** trên Etherscan. Giá trị ghi nhận là **88,304,342,264.55 USDT** (tương đương với `88,304,342,264,551,664` theo đơn vị số nguyên nhỏ nhất, do USDT có 6 chữ số thập phân - `decimals = 6`).

### 3. Trong tab Write Contract, có hàm nào cho phép một địa chỉ đặc biệt đóng băng tài khoản người khác không? Nếu có, tên hàm là gì?  
-> **Trả lời:**
- **Phân tích từ mã băm (`0x1548...`):** Do giao dịch chuyển Native ETH giữa 2 ví EOA không thông qua hợp đồng thông minh, nên **không tồn tại tab `Write Contract`**. Ở cấp độ giao thức blockchain Ethereum đối với tài khoản cá nhân (EOA), **không có bất kỳ cơ chế hay địa chỉ đặc biệt nào có thể đóng băng số dư ETH của người khác**. Quyền sở hữu và chuyển số dư ETH hoàn toàn phụ thuộc vào khóa bí mật (Private Key) của chủ sở hữu địa chỉ ví đó.
- **Đối chiếu với hợp đồng token USDT:** **Có cơ chế đóng băng tài khoản.** Trong tab **Write Contract**, hàm thực hiện việc này có tên là `addBlackList(address _evilUser)`. Hàm này được bảo vệ bởi quyền hạn của chủ sở hữu hợp đồng (`Owner`). Khi một địa chỉ ví bị đưa vào danh sách đen (`isBlackListed[_evilUser] = true`), ví đó lập tức bị đóng băng toàn bộ số dư USDT và không thể gửi hoặc nhận token. (Hợp đồng USDT còn có hàm `removeBlackList` để hủy đóng băng và `destroyBlackFunds` để tiêu hủy token trong tài khoản bị đóng băng).
