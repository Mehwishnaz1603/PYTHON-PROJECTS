#--------Assigenment 12---------#
#Static Methods:
#Create a Class TempretureConverter with a Static method celcius_to_franhite(c) that returns the Faranhite values.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

if __name__== "__main__":
    temp_celsius = 25
    temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")
