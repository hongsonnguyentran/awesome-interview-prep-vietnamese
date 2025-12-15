# Chuyển đổi giá trị từ kg -> lbs và ngược lại

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (kg/lbs): ")

if unit == 'lbs':
    result = (weight / 2) - (10/100 * weight / 2) # result = weight * 2.205
    print(f"{weight} lbs ≈ {round(result, 1)} kg.")
elif unit == 'kg':
    result = (weight * 2) + (10/100 * weight * 2) # result = weight / 2.205
    print(f"{weight} kg ≈ {round(result, 1)} lbs.")
else:
    print(f"{unit} is not valid. Please enter a valid unit to convert. (kg/lbs)")
