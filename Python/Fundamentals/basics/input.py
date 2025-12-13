# input() là 1 hàm tích hợp trong Python được sử dụng để nhận dữ liệu từ người dùng dưới dạng chuỗi (string).
# Khi hàm này được gọi, chương trình sẽ tạm dừng và chờ người dùng nhập dữ liệu từ bàn phím.

# Cú pháp cơ bản của hàm input() như sau:
# input(prompt)
# Trong đó, prompt là một chuỗi tùy chọn được hiển thị cho người dùng trước khi họ nhập dữ liệu.

# Ví dụ sử dụng hàm input():
name = input("What is your name?: ")
age = int(input("How old are you?: "))

age += 1

print(f"Hello, {name}. Welcome to Python!")

print("HAPPY BIRTHDAY!")

print(f"You are {age} years old.")


# Excerise 1: Tính diện tích hình chữ nhật
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"Area: {length} x {width} = {area} cm²")


# Exercise 2: Shopping Cart Program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"You have bought {quantity} {item}(s)")
print(f"Your total is: ${total}")
