# ===============================
# Match Statement (Structural Pattern Matching)
# ===============================

# match-case được giới thiệu từ Python 3.10
# Dùng để so khớp (match) một giá trị với nhiều pattern khác nhau
# Hoạt động tương tự switch-case trong các ngôn ngữ khác nhưng mạnh hơn

# Cú pháp cơ bản:
# match <expression>:
#     case <pattern_1>:
#         ...
#     case <pattern_2>:
#         ...
#     case _:
#         ...   # default case (bắt buộc nếu muốn xử lý các trường hợp còn lại)


# -------------------------------
# Ví dụ 1: Match với giá trị đơn
# -------------------------------

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day")

# Output: Wednesday


# -------------------------------
# Ví dụ 2: Match nhiều giá trị trong một case
# -------------------------------

status_code = 404

match status_code:
    case 200:
        print("OK")
    case 400 | 401 | 403:
        print("Client Error")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")

# Output: Not Found


# -------------------------------
# Ví dụ 3: Match với tuple
# -------------------------------

point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y axis, y = {y}")
    case (x, 0):
        print(f"On X axis, x = {x}")
    case (x, y):
        print(f"Point ({x}, {y})")

# Output: On Y axis, y = 5


# -------------------------------
# Ví dụ 4: Match kết hợp điều kiện (guard)
# -------------------------------

score = 85

match score:
    case s if s >= 90:
        print("Excellent")
    case s if s >= 75:
        print("Good")
    case s if s >= 50:
        print("Pass")
    case _:
        print("Fail")

# Output: Good


# ===============================
# Exercises
# ===============================

# Exercise 1:
# Nhập vào một số từ 1–7
# In ra tên ngày tương ứng
# Nếu không hợp lệ, in "Invalid"

day = int(input("Enter day (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")


# Exercise 2:
# Nhập vào ký tự toán tử: +, -, *, /
# Thực hiện phép tính với a = 10, b = 5

a = 10
b = 5
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")


# Exercise 3:
# Nhập điểm (0–100)
# Dùng match-case để phân loại:
# >=90: A, >=80: B, >=70: C, >=60: D, còn lại: F

score = int(input("Enter score: "))

match score:
    case s if s >= 90:
        print("A")
    case s if s >= 80:
        print("B")
    case s if s >= 70:
        print("C")
    case s if s >= 60:
        print("D")
    case _:
        print("F")
