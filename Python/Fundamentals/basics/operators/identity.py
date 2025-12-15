# ===============================
# Identity Operators
# ===============================

# Toán tử identity dùng để so sánh 2 biến có THAM CHIẾU CÙNG 1 OBJECT trong bộ nhớ hay không
# Kết quả luôn là kiểu bool: True hoặc False

# is     : True nếu 2 biến cùng trỏ tới 1 object
# is not : True nếu 2 biến KHÔNG cùng trỏ tới 1 object

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)        # True  (b tham chiếu cùng object với a)
print(a is c)        # False (giá trị giống nhau nhưng là object khác)
print(a is not c)    # True

# Ví dụ với kiểu immutable (int, str, tuple)
x = 100
y = 100

print(x is y)        # True (CPython tối ưu bộ nhớ cho số nhỏ)

# Lưu ý: KHÔNG dùng `is` để so sánh giá trị, chỉ dùng để so sánh identity
print(x == y)        # True (so sánh giá trị)


# ===============================
# Ví dụ thực tế
# ===============================

# Kiểm tra biến có phải None hay không (trường hợp dùng phổ biến nhất)
result = None

print(result is None)      # True
print(result is not None)  # False


# ===============================
# Exercises
# ===============================

# Exercise 1: Kiểm tra biến có được khởi tạo hay chưa
data = None

is_initialized = data is not None
print("Is initialized:", is_initialized)


# Exercise 2: So sánh identity giữa 2 list
list1 = [1, 2]
list2 = [1, 2]
list3 = list1

print(list1 is list2)   # False
print(list1 is list3)   # True


# Exercise 3: Kiểm tra kết quả trả về của hàm
def find_user(user_id):
    if user_id == 1:
        return {"id": 1, "name": "Alice"}
    return None

user = find_user(2)

if user is None:
    print("User not found")
else:
    print("User found:", user)
