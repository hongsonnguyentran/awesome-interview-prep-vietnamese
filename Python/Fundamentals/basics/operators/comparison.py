# ===============================
# Comparison Operators
# ===============================

# Toán tử so sánh dùng để so sánh 2 giá trị
# Kết quả luôn là kiểu bool: True hoặc False

# ==  : Bằng
# !=  : Không bằng
# >   : Lớn hơn
# <   : Nhỏ hơn
# >=  : Lớn hơn hoặc bằng
# <=  : Nhỏ hơn hoặc bằng

a = 10
b = 20

print(a == b)    # False
print(a != b)    # True
print(a > b)     # False
print(a < b)     # True
print(a >= 10)   # True
print(b <= 15)   # False


# Exercise 1: So sánh 2 số
x = float(input("Enter x: "))
y = float(input("Enter y: "))

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
