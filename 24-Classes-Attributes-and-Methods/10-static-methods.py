# It is a helper method that is defined inside a class body but accepts neither the instance nor the class an argument. The @staticmethod decorator is placed above a method in the class body to designate it as a class method.

class WeatherForecast():

    def __init__(self, temperatures) -> None:
        self.temperatures = temperatures
    
    @staticmethod
    def convert_from_fahrenheit_to_celsius(farh):
        calculation = (5/9) * (farh - 32)
        return round(calculation, 2)
    
    def in_celsius(self):
        return [self.convert_from_fahrenheit_to_celsius(temp) for temp in self.temperatures]
    
wf = WeatherForecast([100, 90, 80, 70, 60, 50])
print(wf.in_celsius())

print(WeatherForecast.convert_from_fahrenheit_to_celsius(100))