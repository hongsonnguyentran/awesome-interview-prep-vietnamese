# conditional expression hay ternary operator - toán tử 3 ngôi
# Là cách viết ngắn gọn của if-else trên 1 dòng

num = 5

print("Positive" if num < 0 else "Negative")

# ============

val = 6
is_even_or_odd = "Even" if val % 2 == 0 else "Odd"
print(is_even_or_odd)

# ============

a = 8
b = 12

max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

# ============

age = 21

status = "Adult" if age >= 18 else "Child"
print(status)

# ============

temp = 26

weather = "hot" if temp >= 33 else "cool"

print(weather)

# ============

user_role = "admin"

access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)
