# NHẬT KÝ LÀM VIỆC VỚI AI - ECO2432

---

## Lab 01: Thiết lập môi trường và ví Web3

**Prompt:**
> Hướng dẫn các bước khởi tạo Git và đẩy kho hce-web3-starter lên GitHub cá nhân; cách tạo ví thử nghiệm MetaMask trên mạng Sepolia Testnet an toàn và nhận ETH faucet để thực hành.

**AI trả về:**
- Hướng dẫn các lệnh Git chuẩn: `git init -b main`, `git add .`, `git commit -m "chore: thiet lap moi truong lam viec"`, `git remote add origin ...`, `git push -u origin main`.
- Hướng dẫn cài đặt ví MetaMask, tạo ví thử nghiệm mới, lưu trữ cụm từ khôi phục (Seed Phrase) bảo mật; kích hoạt mạng Sepolia Testnet và cách nhận Sepolia ETH miễn phí từ faucet.
- Cảnh báo nguyên tắc an toàn: Tuyệt đối không dùng ví có tiền thật, không lưu Private Key/API Key vào mã nguồn hoặc commit lên GitHub.

**Đánh giá:** Dùng được.

**Chỗ sai:** AI ban đầu có thể gợi ý `git init` thông thường tạo nhánh mặc định là `master`, dễ gây lệch nhánh khi GitHub dùng chuẩn `main`.

**Cách sửa:** Sinh viên đối chiếu tài liệu [README.md](file:///d:/crypto-smart-contract-2026/hce-web3-starter-KhanhLinh/README.md) của học phần và dùng đúng cờ `-b main` (`git init -b main`).

**Ai phát hiện:** Sinh viên đối chiếu tài liệu hướng dẫn học phần.

---

## Lab 02: Khảo sát giao dịch Blockchain (lab02.md)

**Prompt:**
> Hãy giúp tôi phân tích giao dịch với mã băm `0x15482ae20c17d95d6c46280a8c76d8385742ddd7528ceb9534eb0fb948af676d` để điền bảng so sánh giao dịch thành công / thất bại, và giải thích nếu chuyển nhầm tiền cho người lạ trên blockchain thì có lấy lại được không.

**AI trả về:**
- Trích xuất thông tin giao dịch thành công: số tiền chuyển (`0.01 ETH`), phí thực trả (`0.000053956450443 ETH`), trạng thái `Success`.
- Giải thích tính bất biến (immutability) và phi tập trung của blockchain: giao dịch đã vào khối thì không thể đảo ngược hay hủy bỏ, cơ hội duy nhất là người nhận tự nguyện chuyển lại.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không có sai sót về lý thuyết; cần kiểm tra số liệu phí thực tế trên Etherscan Sepolia để có giá trị chính xác tuyệt đối.

**Cách sửa:** Sinh viên tự tra cứu mã băm trên Etherscan mạng Sepolia để đối chiếu và lấy số liệu chi tiết đưa vào bảng.

**Ai phát hiện:** Sinh viên đối chiếu thực tế.

---

## Lab 03: Điều tra giao dịch Forensics (forensics.md)

**Prompt:**
> tại file forensics.md hãy sử dụng mã băm 0x15482ae20c17d95d6c46280a8c76d8385742ddd7528ceb9534eb0fb948af676d để giải quyết các câu hỏi

**AI trả về:**
- Trích xuất đầy đủ 10 trường dữ liệu điều tra kỹ thuật (Status, Block, Timestamp, From/To, Value, Tx Fee, Gas Price, Gas Limit, Gas Used, Nonce, Input Data) từ RPC mạng Sepolia Testnet.
- Trả lời 3 câu hỏi điều tra bằng cách phân tích bản chất từ chính mã băm (giao dịch Native ETH giữa hai ví EOA, không qua smart contract, không có hàm `totalSupply()` hay đóng băng) đồng thời đối chiếu hợp đồng mẫu USDT (`0xdAC17F958D2ee523a2206206994597C13D831ec7`) theo yêu cầu bài Lab.

**Đánh giá:** Dùng được.

**Chỗ sai:** Ban đầu phần trả lời câu hỏi 1 và 3 chỉ trả lời theo góc nhìn hợp đồng USDT mà chưa bám vào mã băm giao dịch thực tế `0x1548...` (vốn là chuyển ETH thuần túy giữa 2 ví cá nhân).

**Cách sửa:** Sinh viên yêu cầu AI giải quyết triệt để từ mã băm; AI đã cập nhật phân tích đa chiều (vừa phân tích kỹ thuật từ mã băm thực tế, vừa đối chiếu hợp đồng USDT để đầy đủ barem).

**Ai phát hiện:** Sinh viên phát hiện và yêu cầu bổ sung.

---

## Lab 04: Thẩm định rủi ro hợp đồng token (lab04.md & ClubTokens.sol)

**Prompt:**
> Bạn là chuyên viên thẩm định rủi ro tài sản số.
> Dưới đây là mã nguồn một hợp đồng token. Hãy liệt kê mọi quyền đặc biệt mà chủ sở hữu hợp đồng có thể thực hiện, và với mỗi quyền, nêu rõ:
> - Tên hàm và số dòng
> - Người nắm giữ token chịu rủi ro gì
> Chỉ trả lời dựa trên mã nguồn tôi cung cấp. Nếu không tìm thấy, nói là không tìm thấy.
> [Mã nguồn ClubTokenA, ClubTokenB, ClubTokenC trong ClubTokens.sol]

**AI trả về:**
- Phân tích Hợp đồng A: Không có quyền đặc biệt nào của Owner (an toàn).
- Phân tích Hợp đồng B: Có hàm `mint` ở dòng 18–20 với modifier `onlyOwner`, gây rủi ro lạm phát vô hạn và sụt giá token (dump/dilution).
- Phân tích Hợp đồng C: Có hàm `setRestricted` ở dòng 30–32 kết hợp kiểm tra `require(!restricted[from])` trong hàm `_update` (dòng 34–37), gây rủi ro đóng băng tài sản và bẫy vốn (honeypot/censorship).

**Đánh giá:** Dùng được.

**Chỗ sai:** Vị trí hàm `setRestricted` bắt đầu chính xác từ dòng 30 (dòng 29 là dòng trống ngăn cách constructor).

**Cách sửa:** Sinh viên ghi nhận chính xác dòng 30 vào bảng kết quả `lab04.md`.

**Ai phát hiện:** AI và sinh viên cùng đối chiếu mã nguồn.

### So sánh: Đọc thủ công vs AI

- **Đọc thủ công tìm ra gì:** 
  Tôi tìm thấy từ khóa `onlyOwner` ở Hợp đồng B và C. Tôi nhận ra Hợp đồng B có hàm `mint` có thể tạo thêm token, và Hợp đồng C có biến `restricted` cùng hàm `setRestricted` có vẻ dùng để chặn người dùng. Hợp đồng A trông khá tiêu chuẩn và an toàn.

- **AI tìm thêm được gì:** 
  AI giải thích rất rõ ràng **hậu quả** của các đoạn mã đó đối với nhà đầu tư. AI chỉ ra chính xác số dòng (dòng 18 đối với Hợp đồng B và dòng 29 đối với Hợp đồng C). Đặc biệt ở Hợp đồng C, AI phân tích được sự liên kết giữa hàm `setRestricted` và điều kiện `require` ở dòng 34 trong hàm `_update` để dẫn đến kết luận người dùng bị khóa tài khoản (không thể chuyển token).

- **AI có nói sai chỗ nào không:** 
  Không. AI bám sát chính xác vào mã nguồn được cung cấp, trích dẫn đúng số dòng và không tự bịa ra các lỗi bảo mật hay các hàm không tồn tại trong Hợp đồng A.
