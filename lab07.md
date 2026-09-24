# Báo cáo Đánh giá Tính khả thi Dự án Thẻ Tích điểm Sinh viên (Lab 07)

## 1. Thông số đầu vào và Giả định mô hình

* **Quy mô hoạt động:** 1.000 lượt cộng điểm / tháng.
* **Loại thao tác blockchain:** Ghi trạng thái biến mới vào bộ nhớ lưu trữ (`SSTORE` / Storage).
* **Lượng gas tiêu thụ ước tính:** 20.000 gas / giao dịch.
* **Đơn giá gas mạng chính (Layer 1):** 20 Gwei ($20 \times 10^{-9}$ ETH).
* **Giá thị trường tham chiếu của ETH:** 3.000 USD / ETH.
* **Công thức tính toán:**
  $$\text{Chi phí (ETH)} = \text{Lượng gas tiêu thụ} \times \text{Đơn giá (Gwei)} \times 10^{-9}$$
  $$\text{Chi phí (USD)} = \text{Chi phí (ETH)} \times \text{Giá ETH (USD)}$$

---

## 2. Bảng tính chi phí chi tiết: Layer 1 vs. Layer 2

### a. Bảng tính chi phí một tháng bằng USD trên mạng chính (Layer 1)

* **Bước 1: Tính tổng lượng gas tiêu thụ trong 1 tháng:**
  $$\text{Tổng gas} = 1.000 \text{ lượt} \times 20.000 \text{ gas} = 20.000.000 \text{ gas}$$
* **Bước 2: Quy đổi chi phí ra ETH:**
  * Cho 1 giao dịch: $20.000 \times 20 \times 10^{-9} = 0,0004 \text{ ETH}$
  * Cho cả tháng (1.000 giao dịch): $20.000.000 \times 20 \times 10^{-9} = 0,4 \text{ ETH}$
* **Bước 3: Quy đổi chi phí ra USD (tỷ giá 3.000 USD/ETH):**
  * Cho 1 giao dịch: $0,0004 \text{ ETH} \times 3.000 \text{ USD} = 1,20 \text{ USD}$
  * Cho cả tháng (1.000 giao dịch): $0,4 \text{ ETH} \times 3.000 \text{ USD} = 1.200 \text{ USD}$

---

### b. Chi phí một tháng nếu chuyển sang mạng Layer 2 (Rẻ hơn 100 lần)

* **Chi phí cho 1 giao dịch trên Layer 2:**
  * Chi phí ETH: $\frac{0,0004 \text{ ETH}}{100} = 0,000004 \text{ ETH}$
  * Chi phí USD: $\frac{1,20 \text{ USD}}{100} = 0,012 \text{ USD}$ (~300 VNĐ)
* **Tổng chi phí cho cả tháng (1.000 giao dịch):**
  * Tổng chi phí ETH: $\frac{0,4 \text{ ETH}}{100} = 0,004 \text{ ETH}$
  * Tổng chi phí USD: $\frac{1.200 \text{ USD}}{100} = 12 \text{ USD}$ (~300.000 VNĐ)

---

### Bảng so sánh tổng hợp chi phí

| Chỉ số / Khoản mục | Mạng chính (Layer 1) | Mạng Layer 2 (Rẻ hơn 100 lần) | Chênh lệch tiết kiệm |
| :--- | :--- | :--- | :--- |
| **Gas tiêu thụ / giao dịch** | 20.000 gas | 20.000 gas | - |
| **Đơn giá Gas** | 20 Gwei | 0,2 Gwei | Giảm 100 lần |
| **Chi phí 1 giao dịch (ETH)** | 0,0004 ETH | 0,000004 ETH | Tiết kiệm 0,000396 ETH |
| **Chi phí 1 giao dịch (USD)** | **1,20 USD** (~30.000 VNĐ) | **0,012 USD** (~300 VNĐ) | Giảm từ 30.000đ xuống 300đ |
| **Tổng gas tiêu thụ / tháng** | 20.000.000 gas | 20.000.000 gas | - |
| **Tổng chi phí tháng (ETH)** | 0,4 ETH | 0,004 ETH | Tiết kiệm 0,396 ETH |
| **Tổng chi phí tháng (USD)** | **1.200 USD** (~30.000.000 VNĐ) | **12 USD** (~300.000 VNĐ) | **Tiết kiệm 1.188 USD / tháng** |

---

## 3. Phân tích kinh tế và Trải nghiệm người dùng

### c. Ai trả khoản này — Câu lạc bộ hay Sinh viên? Sinh viên có chấp nhận không?

#### 1. Ai trả khoản phí này?
* **Cơ chế mặc định:** Người gửi giao dịch (sinh viên) phải chịu phí gas từ số dư ví cá nhân.
* **Cơ chế tài trợ phí (Gas Sponsorship / ERC-4337 Paymaster):** Hệ thống có thể cấu hình để quỹ Câu lạc bộ chi trả toàn bộ phí thay cho sinh viên.

#### 2. Phân tích tính kinh tế: Nếu sinh viên phải tự trả phí:
* **Giá trị thực tế của điểm thưởng:** Trong môi trường học đường, 1 điểm thưởng sinh viên (dùng để đổi nước uống, bánh ngọt, voucher in tài liệu, quà lưu niệm...) thường có giá trị quy đổi tượng trưng từ **500 VNĐ đến 2.000 VNĐ** (khoảng **0,02 – 0,08 USD**).
* **So sánh kinh tế trên Layer 1:**
  * Sinh viên phải bỏ ra **1,20 USD (~30.000 VNĐ)** phí gas để nhận 1 điểm thưởng trị giá **0,04 USD (~1.000 VNĐ)**.
  * Phí gas **cao gấp 30 lần** giá trị phần thưởng nhận được.
  * **Đánh giá:** **Sinh viên chắc chắn 100% sẽ từ chối tham gia**. Việc phải bỏ ra 30.000 VNĐ và bắt buộc phải sở hữu tiền mã hóa ETH trong ví chỉ để tích 1 điểm thưởng là rào cản hoàn toàn phi lý đối với người dùng đại chúng.
  * Nếu CLB trả trên Layer 1: CLB sẽ phải chi trả tới **1.200 USD/tháng (~30 triệu VNĐ)**, vượt xa ngân sách hoạt động của một câu lạc bộ sinh viên.
* **So sánh kinh tế trên Layer 2:**
  * Chi phí giao dịch chỉ còn **0,012 USD (~300 VNĐ)**, thấp hơn nhiều so với giá trị điểm thưởng.
  * Quan trọng hơn, với tổng ngân sách chỉ **12 USD/tháng (~300.000 VNĐ)**, **Câu lạc bộ hoàn toàn có thể đứng ra tài trợ toàn bộ khoản phí này**. Sinh viên được tích điểm hoàn toàn miễn phí, mang lại trải nghiệm mượt mà như các ứng dụng Web2 truyền thống.

---

## 4. Kết luận khả thi mô hình kinh doanh

### d. Mô hình kinh doanh này khả thi trên mạng nào?

1. **Trên mạng chính Ethereum (Layer 1): HOÀN TOÀN KHÔNG KHẢ THI (Infeasible)**
   * **Gánh nặng chi phí khổng lồ:** 1.200 USD/tháng là khoản chi phí quá lớn, làm triệt tiêu tính khả thi tài chính của dự án.
   * **Trải nghiệm người dùng kém:** Phí gas đắt đỏ và thời gian xác nhận khối (12–15 giây) không đáp ứng được yêu cầu thanh toán / tích điểm tức thời tại các quầy sự kiện.

2. **Trên mạng Layer 2 (như Arbitrum, Optimism, Base, Polygon...): CỰC KỲ KHẢ THI (Highly Feasible)**
   * **Chi phí siêu tiết kiệm:** Chi phí chỉ **12 USD/tháng (~300.000 VNĐ)**, hoàn toàn vừa vặn với quỹ tài trợ hoạt động của câu lạc bộ.
   * **Hiệu năng cao:** Tốc độ xử lý giao dịch tính bằng mili-giây, phí gas ổn định và cực thấp.
   * **Tích hợp Account Abstraction (ERC-4337):** Cho phép tài trợ gas và tạo ví tự động thông qua tài khoản Google/Email của sinh viên, xóa bỏ rào cản kỹ thuật Web3 và thúc đẩy sinh viên tham gia đông đảo.
