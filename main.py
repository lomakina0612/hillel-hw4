# Task 1
def convert_temperature(temperature, scale='C_to_F'):
    if scale == 'C_to_F':
        if temperature <= -273.15:
            return "Absolute zero is -273.15 °C. Use a value bigger than -273.15."
        return (temperature * 1.8) + 32
    elif scale == 'F_to_C':
        if temperature <= -459.67:
            return "Absolute zero is -459.67 °F. Use a value bigger than -459.67."
        return (temperature - 32) / 1.8
    else:
        print("Unknown conversion type. Use 'C_to_F' or 'F_to_C'.")
        return None


temp_in_celsius = -274
result = convert_temperature(temp_in_celsius, 'C_to_K')
print(result)

temp_in_celsius = -274
result = convert_temperature(temp_in_celsius, 'C_to_F')
print(result)

temp_in_fahrenheit = -460
result = convert_temperature(temp_in_fahrenheit, 'F_to_C')
print(result)

temp_in_celsius = 100
result = convert_temperature(temp_in_celsius, 'C_to_F')
print(f"{temp_in_celsius}°C = {result}°F")

temp_in_fahrenheit = 17
result = convert_temperature(temp_in_fahrenheit, 'F_to_C')
print(f"{temp_in_fahrenheit}°F = {result:.2f}°C")


# Task 2
