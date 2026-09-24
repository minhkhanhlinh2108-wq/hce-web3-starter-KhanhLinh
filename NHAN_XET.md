# Biên bản kiểm tra chéo đặc tả (Cross-Check Review) - SPEC.md

**Người thực hiện:** Chuyên viên phân tích nghiệp vụ (BA) - Nhóm kiểm tra chéo  
**Tài liệu thẩm định:** [SPEC.md](file:///d:/crypto-smart-contract-2026/hce-web3-starter-KhanhLinh/SPEC.md) (Công cụ phân tích dòng tiền ví Ethereum)  
**Ngày đánh giá:** 24/09/2026  

---

Sau khi đọc kỹ bản đặc tả yêu cầu trong tệp `SPEC.md`, nhóm kiểm tra chéo chỉ ra các điểm còn mơ hồ, thiếu sót kỹ thuật và chưa rõ ràng cần được làm rõ trước khi chuyển giao cho đội ngũ phát triển (Dev):

### 1. Thiếu định nghĩa về "Số dư đầu kỳ" khi tính số dư lũy kế (Mục 3 - R3, R4 & Mục 4)
* **Vấn đề mơ hồ:** Bản đặc tả yêu cầu tính toán "số dư lũy kế" và hiển thị "trục dọc là số dư lũy kế" trong phạm vi **90 ngày gần nhất**, nhưng **hoàn toàn không có định nghĩa về số dư ban đầu (Starting Balance)** tại thời điểm bắt đầu chu kỳ 90 ngày.
* **Rủi ro kỹ thuật & nghiệp vụ:**
  - Nếu mặc định số dư ban đầu bằng `0 ETH`: Giả sử ví đã có sẵn 10 ETH từ trước ngày thứ 90 và giao dịch đầu tiên phát sinh trong chu kỳ là chuyển đi 2 ETH, số dư lũy kế sẽ bị tính thành **-2.000... ETH** (bị âm). Việc số dư ví blockchain bị âm là phi lý và sai lệch bản chất kế toán.
  - Ngược lại, nếu muốn thể hiện số dư thực tế của ví, hệ thống bắt buộc phải truy vấn số dư lịch sử tại khối (block) ở thời điểm 90 ngày trước (thông qua RPC node với `eth_getBalance` tại block quá khứ hoặc tính toán truy hồi từ số dư hiện tại).
* **Đề xuất làm rõ:** Cần xác định rõ đây là:
  - Biểu đồ **Dòng tiền ròng tích lũy (Cumulative Net Cash Flow)** trong kỳ (bắt đầu từ mốc 0)?
  - Hay là **Số dư thực tế tích lũy (Historical Actual Balance)** của ví (cần lấy số dư tại thời điểm `T - 90 ngày` làm số dư đầu kỳ)?

---

### 2. Chưa xác định nền tảng hiển thị và định dạng xuất biểu đồ (Mục 4 - Đầu ra)
* **Vấn đề mơ hồ:** Bản đặc tả yêu cầu *"Bảng dữ liệu gồm..."* và *"Một biểu đồ đường: trục ngang là thời gian, trục dọc là số dư lũy kế"*, nhưng không chỉ định rõ môi trường hiển thị:
  - Ứng dụng chạy trên dòng lệnh (**CLI / Terminal**)? Nếu chạy trên Terminal thì vẽ biểu đồ bằng ký tự ASCII (như thư viện `plotille`, `asciichartpy`) hay xuất tệp ảnh tĩnh (`.png` qua `matplotlib`)?
  - Ứng dụng giao diện web trực quan (**Web Dashboard** - HTML/CSS/JavaScript sử dụng `Chart.js` hoặc `ECharts`)?
  - Hay xuất ra một tệp báo cáo độc lập (file HTML báo cáo hoặc bảng tính Excel có nhúng biểu đồ)?
* **Rủi ro:** Đội ngũ phát triển có thể tạo script Python in kết quả dạng văn bản thô ra terminal, trong khi khách hàng hoặc người chấm bài kỳ vọng một giao diện web trực quan mở trên trình duyệt, dẫn đến nguy cơ không đạt nghiệm thu.
* **Đề xuất làm rõ:** Xác định rõ hình thức giao diện đầu ra (ví dụ: giao diện Web HTML/JS mở trên trình duyệt, hay script Python lưu biểu đồ dạng `balance_chart.png`).

---

### 3. Thiếu quy tắc xử lý giao dịch tự chuyển cho chính mình (Self-Transfer: `from == to`)
* **Vấn đề mơ hồ:**
  - Quy tắc **R1** quy định: Giao dịch có trường `to` trùng địa chỉ xét là dòng tiền vào.
  - Quy tắc **R2** quy định: Giao dịch có trường `from` trùng địa chỉ xét là dòng tiền ra.
  - Trong thực tế trên mạng Ethereum, người dùng thường xuyên thực hiện giao dịch tự gửi cho chính mình (ví dụ: gửi 0 ETH với nonce cũ để hủy lệnh nghẽn mạng - Speed up / Cancel transaction).
  - Khi `from == to == địa chỉ đang xét`, giao dịch thỏa mãn đồng thời cả R1 và R2.
* **Rủi ro:**
  - Trong bảng dữ liệu, giao dịch này sẽ hiển thị là 1 dòng hay 2 dòng? Cột "Loại" sẽ ghi nhận là "Vào" hay "Ra"?
  - Tổng tiền vào và tổng tiền ra đều bị đội khống lên một lượng bằng giá trị chuyển (dù thực tế ví chỉ bị trừ phí gas).
* **Đề xuất làm rõ:** Bổ sung quy tắc: Với giao dịch tự chuyển (`from == to`), chỉ ghi nhận dòng tiền ra bằng đúng phí giao dịch (phí gas), giá trị chuyển ròng bằng 0.

---

### 4. Chưa làm rõ mạng Blockchain mục tiêu (Network Endpoint)
* **Vấn đề mơ hồ:** Mục 2 chỉ nêu `ETHERSCAN_API_KEY` mà không chỉ định mạng blockchain:
  - Ethereum Mainnet (endpoint: `api.etherscan.io`)
  - Hay Ethereum Sepolia Testnet (endpoint: `api-sepolia.etherscan.io`)
* **Rủi ro:** Các bài thực hành trong dự án ECO2432 đều thực hiện trên mạng Sepolia Testnet. Nếu lập trình viên gọi mặc định API Mainnet, hệ thống sẽ trả về danh sách rỗng đối với các địa chỉ ví thử nghiệm của sinh viên.
* **Đề xuất làm rõ:** Bổ sung tham số cấu hình mạng hoặc quy định rõ mạng mặc định (Sepolia Testnet).
