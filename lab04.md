# Kết quả thẩm định rủi ro Lab 04

| Hợp đồng | Kết luận | Tên hàm | Số dòng | Rủi ro cho người nắm giữ |
| :--- | :--- | :--- | :--- | :--- |
| **A** | An toàn (Không có quyền đặc biệt) | Không có | Không có | Người nắm giữ không chịu rủi ro từ quyền quản trị. Hợp đồng chỉ đúc token một lần khi khởi tạo. |
| **B** | Có rủi ro lạm phát (Unlimited Minting) | `mint` | 18 | Chủ sở hữu có thể tùy ý đúc thêm vô hạn token cho bất kỳ ai. Việc này làm tăng tổng cung đột ngột, pha loãng giá trị token và khiến tài sản của người nắm giữ bị mất giá nghiêm trọng. |
| **C** | Có rủi ro đóng băng tài khoản (Blacklist) | `setRestricted` | 30 | Chủ sở hữu có thể đưa bất kỳ địa chỉ ví nào vào danh sách hạn chế (restricted). Nếu bị đưa vào danh sách này, người nắm giữ sẽ bị khóa cứng tài sản, không thể chuyển đổi hay bán token ra ngoài (dòng 34 - 37). |
