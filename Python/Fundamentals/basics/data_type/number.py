"""
    1. Các kiểu dữ liệu số trong Python
    - int: Số nguyên
    - float: Số thực
    - complex: Số phức
"""

# int - Số nguyên
# Lưu trữ giá trị nguyên không giới hạn độ lớn.
# Python tự mở rộng bộ nhớ để chứa các số nguyên lớn.

a = 10
b = 10**100  # Số nguyên rất lớn


# float - Số thực
# Biểu diễn theo chuẩn IEEE 754 (64-bit).
# Có sai số do giới hạn độ chính xác.
# Giá trị lớn nhất bị giới hạn bởi 'sys.float_info.max'

x = 0.1 + 0.2
print(x)  # In ra: 0.30000000000000004


# complex - Số phức
# Biểu diễn số phức với phần thực và phần ảo.
# Luôn chứa 2 số float.
# Cú pháp: a + bj, trong đó a là phần thực, b là phần ảo.
z = 3 + 4j


# 2. Khởi tạo và ép kiểu

# Khởi tạo trực tiếp
i = 5
f = 3.14
c = 2 + 3j

# Ép kiểu
float(5)        # 5.0
int(3.99)       # 3
complex(7)      # (7+0j)
complex(2, 3)   # (2+3j)
# Lưu ý: Ép kiểu từ 'float' sang 'int' sẽ làm mất phần thập phân.
# Lưu ý: Ép kiểu từ 'complex' sang 'int' hoặc 'float' sẽ gây lỗi.

# 3. Kiểm tra kiểu dữ liệu
num = 10
type(num)               # <class 'int'>

isinstance(num, int)    # True
isinstance(num, float)  # False
isinstance(num, complex) # False

# 4. Biểu diễn 'int' dưới dạng nhị phân, thập lục phân, bát phân
n = 42
bin(n)   # '0b101010'
hex(n)   # '0x2a'
oct(n)   # '0o52'