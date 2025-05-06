# Hướng Dẫn Cài Đặt Dự Án

## Yêu Cầu Hệ Thống
- Python 3.8 trở lên
- pip (trình quản lý gói Python)
- Git

## Các Bước Cài Đặt

1. **Clone Repository**
    ```bash
    git clone <URL của repository>
    cd GIt_baitap
    ```

2. **Tạo Virtual Environment (Tùy chọn)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Linux/MacOS
    venv\Scripts\activate     # Trên Windows
    ```

3. **Cài Đặt Các Gói Phụ Thuộc**
    ```bash
    pip install -r requirements.txt
    ```

4. **Chạy File Chính**
    ```bash
    python BaiTaplon.py
    ```

## Ghi Chú
- Đảm bảo bạn đã cài đặt đầy đủ các gói phụ thuộc trong `requirements.txt`.
- Nếu gặp lỗi, kiểm tra lại phiên bản Python và các gói phụ thuộc.

