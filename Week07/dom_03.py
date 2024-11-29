class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
             return (fahrenheit - 32) * 5/9


celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C = {fahrenheit_temp:.2f}°F")

fahrenheit_temp = 77
celsius_temp = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F = {celsius_temp:.2f}°C")
