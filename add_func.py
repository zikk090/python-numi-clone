input_string = input("Please enter your calculation")

class Calculator:
    def add_numbers(self, input_string):
        numbers = []
        for item in input_string.split():
            try:
                numbers.append(float(item))
            except ValueError:
                pass
        return sum(numbers)
calculator = Calculator()
result = calculator.add_numbers(input_string)
print(result)  

#result = calculator.add_numbers("1 + 1 + 12")
#print(result)  
