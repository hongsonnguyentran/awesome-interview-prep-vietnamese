""" Introduction to Variables in Python (Biến trong Python)
    + Variable - biến là các thùng được dán nhãn (variable name) chứa các đồ vật bên trong (data/value).
    + Python không có câu lệnh khai báo biến riêng biệt.
    + Một biến được tạo khi bạn gán nó một giá trị.
    + Không cần phải khai báo kiểu dữ liệu của biến.
"""

variable = 5  # variable là một biến có giá trị là số -> 5


""" Variable Naming Rules (Quy tắc đặt tên biến)
    Cách đặt tên biến trong Python:
    - Tuân thủ quy ước khi đặt tên biến: snake_case (sử dụng chữ thường và dấu gạch dưới để phân tách từ).
    - Tên biến phải bắt đầu bằng một chữ cái (a-z, A-Z) hoặc dấu gạch dưới (_).
    - Tên biến không được bắt đầu bằng một số (0-9).
    - Tên biến chỉ có thể chứa các ký tự chữ cái, số và dấu gạch dưới (A-z, 0-9, và _).
    - Tên biến phân biệt chữ hoa và chữ thường (age và Age là hai biến khác nhau).
    - Tránh sử dụng các từ khóa của Python làm tên biến (như: if, else, while, for, v.v.).
"""

""" Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""

""" Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
"""

""" Sensitive Case Variables (Biến phân biệt chữ hoa và chữ thường)
    Python phân biệt chữ hoa và chữ thường trong tên biến.
    Ví dụ: 'age', 'Age', và 'AGE' là ba biến khác nhau.

    age = 25
    Age = 30    
    AGE = 35

    print(age)  # Output: 25
    print(Age)  # Output: 30
    print(AGE)  # Output: 35
"""


""" Tạo biến chứa giá trị chuỗi (String)
    Có thể gán 1 giá trị kiểu chuỗi cho biến.
    Bằng cách sử dụng dấu ngoặc kép ("") hoặc dấu ngoặc đơn ('').
"""

sentence = "Hello, World!"  # sentence là một biến có giá trị là chuỗi -> Hello, World!
greeting = "Xin chào!"      # greeting là một biến có giá trị là chuỗi -> Xin chào!

""" Reassign giá trị mới cho biến
    Python cũng cho phép thay đổi kiểu dữ liệu của biến sau khi đã gán giá trị ban đầu.
"""
var = 10        # var là kiểu số nguyên
print(var)      # Output: 10
var = "Hello"   # var bây giờ là kiểu chuỗi
print(var)      # Output: Hello

# Có thể gán nhiều giá trị cho nhiều biến trong một dòng
a, b, c = 1, 2, 3
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Cũng có thể gán cùng một giá trị cho nhiều biến trong một dòng
x = y = z = 0
print(x)  # Output: 0
print(y)  # Output: 0
print(z)  # Output: 0


""" Tạo biến chứa 1 kiểu dữ liệu cụ thể
    Nếu nếu chỉ định cụ thể kiểu dữ liệu cho biến, bằng cách sử dụng
    hàm tích hợp như int(), float(), str(), v.v.
"""

num = int(10)       # num là một biến có giá trị kiểu số nguyên -> 10
pi = float(3.14)    # pi là một biến có giá trị kiểu số thực -> 3.14
age = str("21")     # age là một biến có giá trị kiểu chuỗi -> '21'


""" Kiểm tra kiểu dữ liệu của biến
    Có thể xem kiểu dữ liệu của biến bằng cách sử dụng hàm 'type()'.
"""

class_no = 12
student_name = "Alice"
print(type(class_no))       # Output: <class 'int'>
print(type(student_name))   # Output: <class 'str'>


""" Chi tiết hơn về biến trong Python
    - Biến trong Python là các tham chiếu đến đối tượng trong bộ nhớ.
    - Python sử dụng cơ chế quản lý bộ nhớ tự động (automatic memory management).
    - Khi một biến được tạo, Python sẽ cấp phát bộ nhớ cho đối tượng và liên kết
    biến với đối tượng đó.
    - Khi một biến được gán một giá trị mới, Python sẽ tạo một đối tượng mới và
    liên kết biến với đối tượng mới đó.
    - Nếu không còn biến nào tham chiếu đến một đối tượng, Python sẽ tự động
    giải phóng bộ nhớ của đối tượng đó thông qua cơ chế thu gom rác (garbage collection).

"""