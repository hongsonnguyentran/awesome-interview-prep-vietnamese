## Introduction of Python
- Python là 1 ngôn ngữ thông dịch, được tạo ra bởi Guido van Rossum và được ra mắt lần đầu vào năm 1991.
- Python sử dụng cơ chế **kiểu dữ liệu dynamic**, tự quản lý bộ nhớ và hỗ trợ nhiều mô hình lập trình như
thủ tục, hàm và đối tượng.
- Python chạy được trên nhiều hệ điều hành nhưng phụ thuộc vào phiên bản Python và môi trường. 

- **Các đặc điểm chính**:
    - Chạy bằng trình thông dịch, không cần biên dịch trước.
    - Hệ thống kiểu dữ liệu động và tự dọn dẹp bộ nhớ (garbage collection).
    - Cú pháp dễ đọc, sử dụng thụt lề để xác định cấu trúc code.
    - Thư viện chuẩn phong phú với nhiều mô-đun xử lý file, mạng, toán học, lập trình song song,...
    - Có khả năng chạy trên nhiều hệ điều hành mà không cần sửa đổi nhiều.

- **Các ứng dụng phổ biến**:
    - Phát triển web với các framework như Django, Flask và FastAPI.
    - Phân tích dữ liệu và tính toán khoa học bằng NumPy, Pandas.
    - Học máy với TensorFlow, PyTorch và các công cụ liên quan.
    - Viết script tự động hóa tác vụ hệ thống.
    - Xây dựng API, testing, prototype nhanh.

## How Python works
- Python sử dụng **Python Interpreter** để biên dịch source code (.py) sang bytecode (.pyc).
    - Bytecode là code trung gian, phụ thuộc theo Python version và được lưu trong thư mục `__pycache__`.
    - Bytecode được tạo bởi các VM khác nhau thì khác nhau (CPython != PyPy != Jython)
        - CPython là trình biên dịch mặc định.
        - PyPy (JIT)
        - Jython (chạy trên JVM)
        - IronPython (chạy trên .NET)
- Bytecode được thực thi bởi CPython Virtual Machine (Python Virtual Machine – PVM).
    - Bytecode thông qua vòng lặp thực thi (evaluation loop) đọc từng opcode và thực hiện tương ứng bằng các hàm C trong CPython.
