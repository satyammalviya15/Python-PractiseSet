# 2. Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage
temp_c = 25
print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c)}°F")