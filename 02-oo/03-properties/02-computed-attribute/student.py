class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.__weight_in_kg = weight_in_kg
        self.__height_in_m = height_in_m

    @property
    def bmi(self):
        return self.__weight_in_kg / self.__height_in_m**2
    @property
    def category(self):
        bmi = self.bmi
        if bmi < 18.5:
            return "underweight"
        elif bmi < 25:
            return "normal"
        else: return "overweight"
calc = BMICalculator(weight_in_kg=80, height_in_m=1.80)
print(calc.bmi)
print(calc.category)