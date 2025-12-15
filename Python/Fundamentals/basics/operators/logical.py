# ===============================
# Logical Operators
# ===============================

# Toán tử logic dùng để kết hợp hoặc phủ định các biểu thức boolean

# and : True nếu TẤT CẢ điều kiện đều True
# or  : True nếu ÍT NHẤT 1 điều kiện True
# not : Đảo ngược giá trị boolean

age = 20
has_id = True

print(age >= 18 and has_id)     # True
print(age >= 18 or has_id)      # True
print(not has_id)               # False

# Exercise 1: Kiểm tra xem năm nhập vào có phải năm nhuận không

year = int(input("Enter a year: "))

is_leap_year = year % 4 == 0 and year % 100 != 0

print(f"{year} is leap year? {is_leap_year}")

# Exercise 2: Kiểm tra điều kiện đăng nhập
username_correct = True
password_correct = False

can_login = username_correct and password_correct

print("Can login:", can_login)


# Exercise 3: Kiểm tra số nằm trong khoảng [10, 50]
number = int(input("Enter a number: "))

in_range = number >= 10 and number <= 50

print("In range:", in_range)
