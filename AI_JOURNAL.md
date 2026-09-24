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

---

## Lab 05: Đặc tả yêu cầu công cụ phân tích dòng tiền (SPEC.md)

**Prompt:**
> Hãy tạo một tệp có tên `SPEC.md` trong thư mục hiện tại. Nội dung tệp chứa bản đặc tả yêu cầu cho công cụ phân tích dòng tiền với cấu trúc chính xác như sau:
> ## 1. Bài toán
> Xây dựng một công cụ nhận vào một địa chỉ ví, trả về báo cáo dòng tiền vào và ra của ví đó trong 90 ngày gần nhất, kèm biểu đồ số dư theo thời gian.
> ## 2. Đầu vào
> - Một địa chỉ ví, dạng chuỗi 42 ký tự bắt đầu bằng 0x.
> - Khóa API của Etherscan, đọc từ biến môi trường ETHERSCAN_API_KEY.
> - Số ngày cần phân tích, mặc định 90.
> ## 3. Quy tắc nghiệp vụ
> - R1: Giao dịch có trường "to" trùng địa chỉ đang xét được tính là dòng tiền vào.
> - R2: Giao dịch có trường "from" trùng địa chỉ đang xét được tính là dòng tiền ra.
> - R3: Với giao dịch đi ra, số tiền thực trừ khỏi ví = giá trị chuyển + phí giao dịch.
> - R4: Giao dịch có trạng thái thất bại vẫn bị trừ phí, phải tính vào dòng tiền ra.
> - R5: Mọi số tiền lấy về ở đơn vị wei, phải chia cho 10^18 trước khi hiển thị.
> - R6: Sắp xếp theo thời gian tăng dần.
> ## 4. Đầu ra
> - Bảng dữ liệu gồm: thời gian, loại (vào/ra), số tiền ETH, phí, số dư lũy kế.
> - Một biểu đồ đường: trục ngang là thời gian, trục dọc là số dư lũy kế.
> - Ba con số tổng hợp: tổng vào, tổng ra, số dư cuối kỳ.
> ## 5. Trường hợp ngoại lệ
> - Nếu API trả về danh sách rỗng: in thông báo "Vi khong co giao dich trong ky", không báo lỗi.
> - Nếu API trả về mã lỗi: in mã lỗi và dừng, không xử lý tiếp.
> - Nếu ví có hơn 10.000 giao dịch: API trả theo trang, phải lấy đủ các trang.
> ## 6. Ngoài phạm vi
> - Không phân tích giao dịch token (chỉ ETH gốc).
> - Không quy đổi ra tiền Việt.

**AI trả về:**
- Đã khởi tạo hoàn chỉnh tệp `SPEC.md` với đúng 6 phần theo đặc tả kỹ thuật: Bài toán, Đầu vào, 6 Quy tắc nghiệp vụ (R1-R6), Đầu ra, Trường hợp ngoại lệ và Ngoài phạm vi.

**Đánh giá:** Dùng được.

**Chỗ sai / Điểm cần lưu ý:**
- Đặc tả yêu cầu đọc khóa API từ biến môi trường `ETHERSCAN_API_KEY` hoàn toàn khớp với quy tắc bảo mật khi viết Python trong `AGENTS.md`.
- Quy tắc R3 và R4 phân định chính xác tính chất on-chain: giao dịch chuyển đi thất bại vẫn tiêu tốn gas và trừ phí khỏi ví người gửi.
- Cần chú ý thuật toán phân trang (pagination) của Etherscan API khi số lượng giao dịch vượt ngưỡng 10.000 bản ghi.

**Cách sửa:** Thiết lập cấu trúc đặc tả chuẩn xác, sẵn sàng làm cơ sở kiểm thử cho việc cài đặt mã nguồn phân tích dòng tiền.

**Ai phát hiện:** AI và sinh viên thống nhất theo tài liệu đặc tả.

### Kiểm tra chéo đặc tả (NHAN_XET.md)

**Prompt:**
> Dựa vào bản đặc tả trong tệp `SPEC.md` vừa tạo, bạn hãy đóng vai là một Chuyên viên phân tích (BA) của nhóm bên cạnh để thực hiện bước "Kiểm tra chéo". 
> Nhiệm vụ của bạn là đọc kỹ đặc tả và chỉ ra ít nhất 2 chỗ còn mơ hồ, thiếu sót hoặc chưa rõ ràng trong bản yêu cầu này (ví dụ: thiếu định nghĩa về số dư đầu kỳ khi tính số dư lũy kế, hoặc chưa rõ biểu đồ đường hiển thị trên giao diện web hay terminal).
> Hãy ghi 2 nhận xét mơ hồ này vào một tệp mới có tên `NHAN_XET.md`.

**AI trả về:**
- Đóng vai BA chỉ ra 4 điểm thiếu sót / mơ hồ kỹ thuật then chốt trong `SPEC.md` và lưu vào tệp `NHAN_XET.md`:
  1. Thiếu định nghĩa về "Số dư đầu kỳ" (Starting Balance) dẫn đến nguy cơ số dư lũy kế bị âm hoặc sai lệch bản chất.
  2. Chưa chỉ định nền tảng hiển thị và định dạng biểu đồ (Web Dashboard HTML/JS hay CLI Terminal / ảnh PNG).
  3. Thiếu quy tắc xử lý giao dịch tự chuyển cho chính mình (`from == to`).
  4. Chưa làm rõ mạng Blockchain mục tiêu (Ethereum Mainnet hay Sepolia Testnet).

**Đánh giá:** Dùng được.

**Chỗ sai / Điểm cần lưu ý:** Các điểm mơ hồ được chỉ ra rất xác đáng, sát với thực tế triển khai Web3 và giúp tránh rủi ro lệch tiêu chí nghiệm thu.

**Cách sửa:** Tạo lập tệp `NHAN_XET.md` hoàn chỉnh để nhóm đối tác phản biện và hoàn thiện đặc tả.

**Ai phát hiện:** AI (trong vai trò BA nhóm kiểm tra chéo) phát hiện.

---

## Lab 06 - Nhật ký kiểm tra mã AI sinh ra

**Lỗi 1 (Mục số 4 trong danh mục kiểm tra: Giao dịch thất bại):**
- **AI phát hiện:** Khi viết quy tắc xử lý dòng tiền ra, công cụ AI đã dùng lệnh `if tx['isError'] == '1': continue;` để bỏ qua toàn bộ giao dịch lỗi.
- **Cách sửa:** Tôi đã sửa lại mã để khi `isError == '1'` ở dòng tiền ra (from), chương trình không cộng giá trị chuyển (value) nhưng vẫn phải trừ đi phí giao dịch (fee_eth) vào số dư, đảm bảo tuân thủ đúng Quy tắc R4 trong đặc tả.

**Lỗi 2 (Mục số 3 trong danh mục kiểm tra: Phân trang):**
- **AI phát hiện:** Mã AI sinh ra lúc đầu chỉ gọi API đúng một lần (lấy mặc định trang 1), bỏ qua trường hợp ngoại lệ "Nếu ví có hơn 10.000 giao dịch: API trả theo trang". Điều này dẫn đến thiếu hụt dữ liệu nghiêm trọng.
- **Cách sửa:** Tôi đã bổ sung vòng lặp `while True`, tăng biến `page += 1` sau mỗi lần gọi và điều kiện dừng `if len(txs) < 10000: break` để đảm bảo lấy toàn bộ lịch sử giao dịch trước khi tiến hành lọc 90 ngày.

---

## Lab 07: Báo cáo tính khả thi dự án thẻ tích điểm (lab07.md)

**Prompt:**
> Hãy tạo một tệp có tên `lab07.md` trong thư mục hiện tại để báo cáo tính khả thi của dự án thẻ tích điểm. Nội dung tệp cần có một bảng tính chi phí và các đoạn văn trả lời 4 câu hỏi phân tích...
> a. Bảng tính chi phí một tháng bằng USD trên mạng chính (Layer 1). Trình bày rõ từng bước tính: tổng gas 1 tháng, quy đổi ra ETH, và quy đổi ra USD.
> b. Tính chi phí một tháng nếu chuyển sang mạng Layer 2 (đơn giá rẻ hơn 100 lần).
> c. Trả lời câu hỏi: Ai trả khoản này — câu lạc bộ hay sinh viên? Nếu sinh viên trả (chịu phí giao dịch để nhận điểm), họ có chấp nhận không? (Hãy phân tích tính kinh tế: so sánh giữa chi phí giao dịch và giá trị thực tế của 1 điểm thưởng sinh viên).
> d. Kết luận rút ra: Mô hình kinh doanh này khả thi trên mạng nào?

**AI trả về:**
- Thiết lập tệp `lab07.md` hoàn chỉnh với các công thức và bảng so sánh chi phí chi tiết giữa Layer 1 và Layer 2 (L1 tốn $1.200 USD/tháng vs. L2 chỉ tốn $12 USD/tháng).
- Phân tích kinh tế vi mô: Phí gas trên L1 ($1.20 ~ 30.000 VNĐ) cao gấp 30 lần giá trị thực của 1 điểm thưởng sinh viên (~1.000 VNĐ), do đó sinh viên chắc chắn sẽ từ chối tham gia.
- Đề xuất giải pháp khả thi: Triển khai trên Layer 2 kết hợp cơ chế tài trợ gas (ERC-4337 Paymaster) do CLB chi trả (khoảng $12/tháng).
- Kết luận: Mô hình hoàn toàn bất khả thi trên Ethereum Layer 1 và cực kỳ khả thi trên Layer 2.

**Đánh giá:** Dùng được.

**Chỗ sai / Điểm cần lưu ý:** Cần đối chiếu tỷ giá ETH/USD thực tế và giá trị quy đổi của điểm thưởng sinh viên để lập luận thuyết phục.

**Cách sửa:** Trình bày rõ ràng từng bước tính toán số học và bảng đối chiếu trực quan.

**Ai phát hiện:** AI và sinh viên cùng thống nhất theo yêu cầu phân tích kinh tế.
