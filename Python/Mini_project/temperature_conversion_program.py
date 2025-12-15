# Chuyển đổi nhiệt độ từ °C -> °F và ngược lại

unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    result = round(((9 * temp) / 5 + 32), 1)
    print(f"{temp}°C -> {result}°F")
elif unit == "F":
    result = round(((temp - 32) * 5/9), 1)
    print(f"{temp}°F -> {result}°C")
else:
    print(f"{unit} is not valid. Please enter a valid unit to convert. (C/F)")