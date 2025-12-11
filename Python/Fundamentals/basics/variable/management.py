"""
    Python lưu trữ và quản lý biến theo mô hình 'name -> object -> memory'.
        - 'name' là tên biến mà bạn sử dụng trong mã nguồn.
        - 'object' là giá trị hoặc dữ liệu mà biến tham chiếu đến.
        - 'memory' là vị trí trong bộ nhớ nơi đối tượng được lưu trữ.
    Khi bạn tạo một biến và gán nó một giá trị, Python sẽ thực hiện các bước sau:
        1. Tạo một đối tượng trong bộ nhớ (heap) để lưu trữ giá trị.
        2. Liên kết tên biến với đối tượng đó.

    Khi bạn thay đổi giá trị của biến, Python sẽ tạo một đối tượng mới trong bộ nhớ
    và cập nhật liên kết của tên biến để tham chiếu đến đối tượng mới.
"""

x = 42      # Tạo biến x và gán giá trị 42
y = x       # Tạo biến y và liên kết nó với cùng đối tượng mà x tham chiếu
print(f"x: {x}, y: {y}")    # Output: x: 42, y: 42

# Kiểm tra địa chỉ bộ nhớ của các biến
print(f"Address of x: {id(x)}")  # Địa chỉ bộ nhớ của x
print(f"Address of y: {id(y)}")  # Địa chỉ bộ nhớ của y

x = 100     # Gán lại giá trị của x, tạo đối tượng mới với giá trị 100 và cập nhật liên kết mới
print(f"x: {x}, y: {y}")    # Output: x: 100, y: 42

# Kiểm tra địa chỉ bộ nhớ của các biến
print(f"Address of x: {id(x)}")  # Địa chỉ bộ nhớ của x
print(f"Address of y: {id(y)}")  # Địa chỉ bộ nhớ của y

###

# Immutable và Mutable Objects
""" 
    Immutable objects (đối tượng không thể thay đổi): Khi bạn thay đổi giá trị
    của một biến tham chiếu đến một đối tượng immutable (như int, str, tuple),
    Python sẽ tạo một đối tượng mới trong bộ nhớ và cập nhật liên kết của biến.
"""

x = "hi"
x = x + "!"
# tạo object "hi!" mới


"""
    Mutable objects (đối tượng có thể thay đổi): Khi bạn thay đổi giá trị của một
    biến tham chiếu đến một đối tượng mutable (như list, dict, set), Python sẽ
    thay đổi nội dung của đối tượng trong bộ nhớ mà không tạo đối tượng mới.
"""

a = [1, 2]
b = a
b.append(3)
# a và b đều thấy [1, 2, 3]


"""
    Python quản lý object bằng reference counting + garbage collector.
    Mỗi object giữ một bộ đếm 'refcount'.
        Khi tên mới trỏ đến object → 'refcount' tăng
        Khi bỏ tên hoặc gán tên sang object khác → 'refcount' giảm
        Khi 'refcount' về 0 → object bị giải phóng
    Ngoài ra, Python dùng cyclic GC để xử lý vòng tham chiếu.
"""
import gc
gc.collect()    # Kích hoạt quá trình thu gom rác để giải phóng bộ nhớ không sử dụng
print("Garbage collection completed.")
