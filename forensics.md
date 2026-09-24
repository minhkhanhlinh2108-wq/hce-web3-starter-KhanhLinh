# Kết quả Lab 3 - Điều tra giao dịch (Forensics)

**Mã băm giao dịch (Transaction Hash):** `0x15482ae20c17d95d6c46280a8c76d8385742ddd7528ceb9534eb0fb948af676d`

## Phần 1: Ý nghĩa các trường dữ liệu trong giao dịch

| Trường | Ý nghĩa | Vì sao người làm nghiệp vụ cần |
| --- | --- | --- |
| Status | Thành công hay thất bại | Giao dịch thất bại vẫn mất phí — ảnh hưởng hạch toán |
| Block | Số thứ tự khối chứa giao dịch | Xác định thời điểm ghi nhận |
| Timestamp | Thời gian | Mốc ghi nhận doanh thu / chi phí |
| From / To | Ví gửi / ví nhận | Đối tượng cần xác minh danh tính |
| Value | Số tiền chuyển | Giá trị giao dịch |
| Transaction Fee | Phí thực trả | Chi phí giao dịch, cần hạch toán riêng |
| Gas Price | Đơn giá phí | Giải thích vì sao cùng một giao dịch mà phí khác nhau |
| Gas Limit | Mức gas tối đa ví gửi cho phép dùng | Đặt quá thấp → giao dịch thất bại vì hết gas (Out of Gas) nhưng vẫn mất phí |
| Gas Used | Lượng gas thực tế đã tiêu | Cùng Gas Price với Gas Used tính ra phí: Transaction Fee = Gas Used × Gas Price. Gas Used = Gas Limit là dấu hiệu hết gas |
| Nonce | Số thứ tự giao dịch của ví gửi | Phát hiện giao dịch bị bỏ sót hoặc thay thế |

## Phần 2: Trả lời câu hỏi (Hợp đồng USDT)

1. Hợp đồng bạn xem có công bố mã nguồn đã xác thực không?  
-> Trả lời: Có, mã nguồn đã được bên phát hành công bố và xác thực khớp với bytecode (Source Code verified).

2. Tổng cung của đồng đó là bao nhiêu? Đọc ra từ hàm nào?  
-> Trả lời: Tổng cung: [                   ]. Thông tin này được đọc ra từ hàm `totalSupply()` trong tab Read Contract.

3. Trong tab Write Contract, có hàm nào cho phép một địa chỉ đặc biệt đóng băng tài khoản người khác không? Nếu có, tên hàm là gì?  
-> Trả lời: Có cơ chế đóng băng tài khoản. Đối với USDT, hàm thực hiện việc này có tên là `addBlackList`.
