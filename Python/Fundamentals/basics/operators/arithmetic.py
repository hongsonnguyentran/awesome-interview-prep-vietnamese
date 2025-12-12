# Toán tử số học được sử dụng với các giá trị số để thực hiện các phép toán thông thường

# Các toán tử số học cơ bản trong Python
a = 10
b = 3
print(a + b)  # Phép cộng: 13
print(a - b)  # Phép trừ: 7
print(a * b)  # Phép nhân: 30
print(a / b)  # Phép chia: 3.3333333333333335
print(a // b) # Phép chia lấy phần nguyên: 3
print(a % b)  # Phép chia lấy phần dư: 1
print(a ** b) # Phép lũy thừa: 1000

# Hàm toán học tích hợp (built-in)
abs(-5)             # 5
round(3.14159, 2)   # 3.14
pow(2, 3)           # 8
divmod(7, 3)        # (2, 1)

# Sử dụng module math cho float
import math
print(math.sqrt(16))    # Căn bậc hai: 4.0
print(math.pow(2, 3))   # Lũy thừa: 8.0
print(math.floor(3.7))  # Làm tròn xuống: 3
print(math.ceil(3.3))   # Làm tròn lên: 4

# Sử dụng module cmath cho complex
import cmath
z = 3 + 4j
print(cmath.phase(z))       # Góc pha: 0.927295218001
print(cmath.polar(z))       # Dạng cực: (5.0, 0.9272952180016122)
print(cmath.rect(5, 0.9272952180016122))  # Chuyển đổi ngược: (3+4j)


# Sử dụng module decimal cho số thực chính xác cao
from decimal import Decimal, getcontext
getcontext().prec = 28  # Đặt độ chính xác
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(d1 + d2)  # In ra: 0.3


# Sử dụng module fractions cho phân số
from fractions import Fraction
f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
print(f1 + f2)  # In ra: 11/15