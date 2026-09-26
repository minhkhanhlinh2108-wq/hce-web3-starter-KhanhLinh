| Trường | Giao dịch thành công | Giao dịch thất bại |
| --- | --- | --- |
| Mã băm giao dịch | `0x15482ae20c17d95d6c46280a8c76d8385742ddd7528ceb9534eb0fb948af676d` | `0xebde8ef1572719b7cced99b045ae5035388eb405144cbb18efa6c86de03393d5` |
| Số tiền chuyển | 0.01 ETH | 0 ETH |
| Phí giao dịch thực trả | 0.000053956450443 ETH (~0.000054 ETH) | 0.000040148191437384 ETH (~0.000040 ETH) |
| Trạng thái | Thành công (Success) | Thất bại (Failed / Reverted) |
| Nguyên nhân (nếu thất bại) | Không có | `execution reverted: OMMLibrary: POOL_NOT_FOUND` (Hợp đồng thông minh hoàn tác giao dịch do không tìm thấy bể thanh khoản) |

Nếu chuyển nhầm cho người lạ, bạn gần như không thể lấy lại được số tiền đã chuyển. Nguyên nhân là vì blockchain hoạt động phi tập trung và có tính bất biến, nên một khi giao dịch đã được xác nhận vào khối thì không một cá nhân, tổ chức hay bên trung gian nào có thể đảo ngược hay hủy bỏ giao dịch đó. Cơ hội duy nhất để nhận lại tiền là người nhận có thiện chí và tự nguyện thực hiện một giao dịch mới để hoàn trả lại cho bạn.
