# AGENTS.md - Quy ước dự án ECO2432

## Ngôn ngữ và phiên bản

- Solidity `^0.8.20`.
- OpenZeppelin Contracts 5.x; dùng `_update`, không dùng `_beforeTokenTransfer`.
- Python 3.10+.

## Quy tắc bắt buộc khi viết hợp đồng

1. Mọi hàm làm thay đổi trạng thái phải phát `event`.
2. Mọi hàm dành cho chủ sở hữu phải kiểm tra quyền rõ ràng.
3. Áp dụng Checks - Effects - Interactions.
4. Chuyển ETH bằng `call{value: ...}("")` và kiểm tra kết quả; không dùng `transfer`.
5. Ưu tiên `error` tùy biến thay cho chuỗi lỗi dài.
6. Không dùng `tx.origin` để xác thực.
7. Tỷ lệ phần trăm dùng basis point, trong đó 1% = 100.

## Quy tắc khi viết Python

1. Không ghi khóa API trong mã nguồn; đọc từ biến môi trường.
2. Kiểm tra trạng thái phản hồi trước khi xử lý dữ liệu.
3. Đổi wei sang ETH trước khi hiển thị.

## Khi được yêu cầu sinh mã

- Giải thích ngắn gọn lựa chọn thiết kế trước khi đưa mã.
- Hỏi lại khi yêu cầu chưa rõ; không tự suy đoán quy tắc kinh tế.
- Nêu tối thiểu ba trường hợp kiểm thử, gồm một trường hợp gian lận.
- Chú thích trong mã bằng Tiếng Việt không dấu.

## Quy tắc đồng bộ nhật ký làm việc (AI_JOURNAL.md)

- Mọi bài thực hành (Lab) hoặc tệp công việc mới khi được thực hiện đều phải tự động đồng bộ và ghi lại nhật ký làm việc vào `AI_JOURNAL.md`.
- Cấu trúc mục nhật ký chuẩn gồm:
  - **Prompt:** Nguyên văn yêu cầu của người dùng.
  - **AI trả về:** Tóm tắt giải pháp / mã / phân tích của AI.
  - **Đánh giá:** Dùng được / Phải sửa / Sai, bỏ.
  - **Chỗ sai / Điểm cần lưu ý:** Chi tiết kỹ thuật hoặc phản biện thực tế.
  - **Cách sửa:** Giải pháp người dùng / AI đã thực hiện.
  - **Ai phát hiện:** AI tự nhận / Sinh viên phát hiện.
