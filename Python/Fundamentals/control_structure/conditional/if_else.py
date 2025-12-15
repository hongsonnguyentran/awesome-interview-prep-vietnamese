# If là 1 statement chứa 1 đoạn code và thực thi chúng nếu điều kiện đúng
# Else nếu điều kiện sai thực hiện đoạn code còn lại

age = int(input("Enter your age: "))

if age >= 100:
    print("You're too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't born yet!")
else:
    print("You must be 18+ to sign up")

# =====================================

response = input("Would you like food? (y/n): ")

if response == 'y':
    print("Have some food!")
else: 
    print("No food for you!")

# =====================================

name = input("Enter your name: ")

if name == "":
    print("Please type in your name")
else:
    print(f"Hello {name}")

# =====================================
is_checked = True

if is_checked:
    print("This box is checked")
else:
    print("This box isn't checked")
