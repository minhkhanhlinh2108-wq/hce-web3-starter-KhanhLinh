# Báo cáo Bài toán Kinh tế Thẻ Tích điểm (Lab 07 - Bước 2)

## 1. Bảng tính chi phí một tháng trên mạng chính (Layer 1)

Dữ liệu đầu vào:
* **Số lượng:** 1.000 lượt cộng điểm / tháng.
* **Lượng gas tiêu thụ:** 20.000 gas / giao dịch.
* **Đơn giá gas (Layer 1):** 20 Gwei ($20 \times 10^{-9}$ ETH).
* **Giá ETH:** 3.000 USD / ETH.
* **Công thức:** $\text{Chi phí (ETH)} = \text{Lượng gas tiêu thụ} \times \text{Đơn giá (Gwei)} \times 10^{-9}$.

### Bảng các bước tính chi phí trên Layer 1:

| Bước tính toán | Công thức / Phép tính | Chi phí cho 1 giao dịch | Chi phí cho cả tháng (1.000 lượt) |
| :--- | :--- | :--- | :--- |
| **Bước 1: Lượng gas tiêu thụ** | $\text{Số lượt} \times 20.000 \text{ gas}$ | $20.000 \text{ gas}$ | $\mathbf{20.000.000 \text{ gas}}$ |
| **Bước 2: Quy đổi ra ETH** | $\text{Gas} \times 20 \times 10^{-9}$ | $0,0004 \text{ ETH}$ | $\mathbf{0,4 \text{ ETH}}$ |
| **Bước 3: Quy đổi ra USD** | $\text{ETH} \times 3.000 \text{ USD}$ | $1,20 \text{ USD}$ (~30.000 VNĐ) | $\mathbf{1.200 \text{ USD}}$ (~30.000.000 VNĐ) |

---

## 2. Chi phí một tháng nếu chuyển sang mạng Layer 2 (Đơn giá rẻ hơn 100 lần)

Mạng Layer 2 (như Arbitrum, Optimism, Base...) gom và nén các giao dịch trước khi gửi bằng chứng về Layer 1, giúp đơn giá gas trung bình rẻ hơn khoảng 100 lần:
* **Đơn giá gas tương đương:** $20 \text{ Gwei} / 100 = 0,2 \text{ Gwei}$.
* **Chi phí cho 1 giao dịch trên Layer 2:**
  * Quy đổi ra ETH: $0,0004 \text{ ETH} / 100 = \mathbf{0,000004 \text{ ETH}}$.
  * Quy đổi ra USD: $1,20 \text{ USD} / 100 = \mathbf{0,012 \text{ USD}}$ (~300 VNĐ).
* **Tổng chi phí cả tháng trên Layer 2 (1.000 lượt):**
  * Quy đổi ra ETH: $0,4 \text{ ETH} / 100 = \mathbf{0,004 \text{ ETH}}$.
  * Quy đổi ra USD: $1.200 \text{ USD} / 100 = \mathbf{12 \text{ USD}}$ (~300.000 VNĐ).

### Bảng so sánh chi phí Layer 1 vs. Layer 2:

| Khoản mục | Mạng chính (Layer 1) | Mạng Layer 2 | Mức độ chênh lệch |
| :--- | :--- | :--- | :--- |
| **Chi phí 1 giao dịch** | 1,20 USD (~30.000 VNĐ) | 0,012 USD (~300 VNĐ) | Layer 2 rẻ hơn 100 lần |
| **Tổng chi phí 1 tháng (1.000 tx)** | **1.200 USD** (~30.000.000 VNĐ) | **12 USD** (~300.000 VNĐ) | Tiết kiệm **1.188 USD / tháng** |

---

## 3. Phân tích kinh tế: Ai trả khoản này? Sinh viên có chấp nhận không?

### a. Ai trả khoản phí này?
* **Mặc định kỹ thuật:** Người gửi giao dịch (sinh viên) phải tự trả phí gas từ số dư ví cá nhân.
* **Cơ chế tài trợ phí (Gas Sponsorship):** Thông qua chuẩn Account Abstraction (ERC-4337 / Paymaster), Câu lạc bộ (CLB) có thể đứng ra chi trả toàn bộ phí mạng thay cho sinh viên.

### b. So sánh phí giao dịch và giá trị thực tế của 1 điểm thưởng:
* **Giá trị thực tế của điểm thưởng:** Trong các hoạt động sinh viên (đổi nước ngọt, bánh, photo tài liệu, quà lưu niệm, voucher tham dự sự kiện...), 1 điểm tích lũy thường có giá trị kinh tế tương đương **500 VNĐ đến 2.000 VNĐ** (khoảng **0,02 – 0,08 USD**).
* **Nếu sinh viên phải tự trả phí:**
  * **Trên Layer 1:** Sinh viên phải trả **30.000 VNĐ** phí gas cho một lần quét thẻ nhận điểm chỉ đáng giá **1.000 VNĐ** (phí gas cao gấp **30 lần** giá trị điểm nhận được). **Sinh viên chắc chắn 100% sẽ từ chối tham gia**, vì không ai bỏ ra số tiền lớn chỉ để nhận một phần thưởng nhỏ hơn nhiều lần, chưa kể rào cản phức tạp khi phải nạp tiền ETH thật vào ví.
  * **Nếu CLB phải trả trên Layer 1:** Ngân sách **1.200 USD/tháng (~30 triệu VNĐ)** chỉ để duy trì việc tích điểm là hoàn toàn bất khả thi đối với quỹ hoạt động của một câu lạc bộ sinh viên.
* **Giải pháp trên Layer 2:**
  * Chi phí cho 1 lần cộng điểm chỉ là **300 VNĐ (0,012 USD)**. 
  * Với tổng chi phí toàn bộ chương trình chỉ **300.000 VNĐ/tháng (12 USD)**, **Câu lạc bộ hoàn toàn có thể đứng ra tài trợ 100% khoản phí này**. Sinh viên được tích điểm hoàn toàn miễn phí mà không cần bận tâm đến phí gas blockchain.

---

## 4. Kết luận: Mô hình kinh doanh này khả thi trên mạng nào?

* **Mạng chính Ethereum (Layer 1): HOÀN TOÀN KHÔNG KHẢ THI.**
  * Chi phí vận hành quá đắt đỏ (1.200 USD/tháng), vượt quá khả năng tài chính của CLB.
  * Nếu bắt sinh viên trả, dự án sẽ thất bại ngay lập tức do chi phí gas lớn hơn nhiều giá trị nhận được. Tốc độ xác nhận khối (12–15 giây) cũng quá chậm cho việc tích điểm tại quầy.

* **Mạng Layer 2 (Arbitrum, Base, Optimism, Polygon...): CỰC KỲ KHẢ THI.**
  * Chi phí vận hành siêu rẻ (chỉ 12 USD/tháng cho 1.000 lượt), câu lạc bộ dễ dàng tài trợ toàn bộ.
  * Thời gian giao dịch gần như tức thời (1–2 giây), mang lại trải nghiệm mượt mà.
  * Tạo điều kiện ứng dụng ví thông minh (Smart Account) để sinh viên đăng nhập nhanh bằng email/Google mà không cần kiến thức tiền mã hóa phức tạp.
