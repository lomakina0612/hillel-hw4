# Task 1
print("---------- Task 1 ----------")

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
print("---------- Task 2 ----------")
eu_shoe_sizes_men = [
    34, 34.5, 35, 35.5, 36, 36.5, 37, 37.5, 38, 38.5, 
    39, 39.5, 40, 40.5, 41, 41.5, 42, 42.5, 43, 43.5, 
    44, 44.5, 45, 45.5, 46, 46.5, 47, 47.5, 48, 48.5, 
    49, 49.5, 50
]

us_shoe_sizes_men = [
    3, 3.5, 4, 4.5, 5, 5, 5.5, 6, 6.5, 6.5, 
    7, 7.5, 8, 8.5, 8.5, 9, 9.5, 10, 10.5, 10.5, 
    11, 11.5, 12, 12.5, 12.5, 13, 13.5, 14, 14, 
    14.5, 15, 15.5, 16
]

eu_shoe_sizes_women = [
    34, 34.5, 35, 35.5, 36, 36.5, 37, 37.5, 38, 38.5,
    39, 39.5, 40, 40.5, 41, 41.5, 42, 42.5, 43, 43.5,
    44, 44.5, 45
]

us_shoe_sizes_women = [
    4, 4.5, 5, 5.5, 6, 6, 6.5, 7, 7.5, 7.5,
    8, 8.5, 9, 9.5, 9.5, 10, 10.5, 11, 11.5, 11.5,
    12, 12.5, 13
]
# Data are taken from Wikipedia: https://en.wikipedia.org/wiki/Shoe_size#Continental_Europe

men_shoe_sizes = list(zip(eu_shoe_sizes_men, us_shoe_sizes_men))
women_shoe_sizes = list(zip(eu_shoe_sizes_women, us_shoe_sizes_women))
print(f"men_shoe_sizes: {men_shoe_sizes}")
print(f"women_shoe_sizes: {women_shoe_sizes}")


def eu_to_us(eu_size, sizes):
    us_size = next(filter(lambda x: x[0] == eu_size, sizes), None)
    return us_size[1] if us_size else None


def us_to_eu(us_size, sizes):
    eu_size = next(filter(lambda x: x[1] == us_size, sizes), None)
    return eu_size[0] if eu_size else None


eu_size = 40
us_size = eu_to_us(eu_size, men_shoe_sizes)
print(f"EU shoe size {eu_size} for men corresponds to US size {us_size}.")

us_size = 8.5
eu_size = us_to_eu(us_size, men_shoe_sizes)
print(f"US shoe size {us_size} for men corresponds to US size {eu_size}.")

eu_size = 40
us_size = eu_to_us(eu_size, women_shoe_sizes)
print(f"EU shoe size {eu_size} for women corresponds to US size {us_size}.")

us_size = 7.5
eu_size = us_to_eu(us_size, women_shoe_sizes)
print(f"US shoe size {us_size} for women corresponds to US size {eu_size}")
