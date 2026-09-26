# Kết quả Lab 02 - Khảo sát giao dịch Blockchain

**Mạng kiểm thử:** Ethereum Sepolia Testnet  
**Ví thực hành của sinh viên:** `0xeE917Bc552F81FE4db72025E05F146919b3B4032`

---

## 1. Bảng so sánh giao dịch thành công và thất bại

| Trường dữ liệu | Giao dịch thành công | Giao dịch thất bại |
| :--- | :--- | :--- |
| **Mã băm giao dịch (Tx Hash)** | `0x15482ae20c17d95d6c46280a8c76d8385742ddd7528ceb9534eb0fb948af676d` | `0xebde8ef1572719b7cced99b045ae5035388eb405144cbb18efa6c86de03393d5` |
| **Số tiền chuyển (Value)** | `0.01 ETH` | `0 ETH` |
| **Phí giao dịch thực trả (Tx Fee)** | `0.000053956450443 ETH` (~0.000054 ETH) | `0.000040148191437384 ETH` (~0.000040 ETH) |
| **Trạng thái (Status)** | Thành công (`Success / 0x1`) | Thất bại (`Failed / Reverted - 0x0`) |
| **Nguyên nhân (nếu thất bại)** | Không có | `execution reverted: OMMLibrary: POOL_NOT_FOUND` (Hợp đồng thông minh chủ động hoàn tác giao dịch do không tìm thấy bể thanh khoản tương ứng) |

> **Nhận xét chuyên môn:** Mặc dù giao dịch thất bại không thể chuyển tiền đến địa chỉ đích, tài khoản người gửi **vẫn bị trừ phí gas** (`0.000040148 ETH`). Đây là bản chất của máy ảo EVM: người gửi phải trả phí cho thợ đào/validator vì đã tiêu thụ tài nguyên tính toán để thực thi và phát hiện điều kiện hoàn tác.

---

## 2. Trả lời câu hỏi: Nếu chuyển nhầm tiền cho người lạ trên blockchain thì có lấy lại được không?

Nếu chuyển nhầm tiền cho người lạ trên blockchain, bạn **gần như không thể lấy lại được** số tiền đã chuyển.

**Nguyên nhân:**
1. **Tính bất biến (Immutability):** Một khi giao dịch đã được các validator xác nhận và đóng vào khối (block), dữ liệu sẽ được lưu trữ vĩnh viễn trên sổ cái phân tán. Không một cá nhân, công ty, tổ chức hay thậm chí là nhà sáng lập blockchain nào có quyền can thiệp, chỉnh sửa hay hủy bỏ giao dịch đã thành công.
2. **Tính phi tập trung (Decentralization) & Vắng bóng bên trung gian:** Blockchain không hoạt động như ngân hàng truyền thống (nơi có tổng đài hỗ trợ hoặc bộ phận kiểm soát để phong tỏa giao dịch nghi vấn hay đảo ngược lệnh chuyển nhầm). Mọi giao dịch được thực thi tự động theo các quy tắc toán học và mật mã học.

👉 **Cơ hội duy nhất:** Để nhận lại tiền, cách duy nhất là liên hệ với người nhận (nếu biết danh tính của họ ngoài đời thực) và trông cậy vào thiện chí của họ để họ tự nguyện thực hiện một giao dịch mới gửi trả lại tiền cho bạn.
