import math

# Toán tử gán được sử dụng để gán giá trị cho 1 biến

count = 5

# count = count + 1
# count += 1
# Output: 6

# count = count - 2
# count -= 2
# Output: 3

# count = count * 3
# count *= 3
# Output: 15

# count = count / 4
# count /= 4
# Output: 1.25

# count = count % 3
# count %= 3
# Output: 2

# count = count ** 5
# count **= 5


# Exercise 1: Tính chu vi của hình tròn
# P = 2π * r

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is {round(circumference, 2)} cm")

# Exercise 2: Tính diện tích của hình tròn
# A = π * r²

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The circumference is {round(area, 2)} cm²")


# Exercise 3: Tính cạnh huyền của tam giác vuông, cho 2 cạnh góc vuông
# c = √a² + b²

a = float(input("Enter the first right-angle side: "))
b = float(input("Enter the second right-angle side: "))

hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse is {hypotenuse} cm")
