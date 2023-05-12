input_string = input("Please enter your calculation:")

class Calculator:
    def __init__(self):
        self.words = {"plus": "+"}
    
    def add_numbers(self, input_string):
        numbers = []
        for item in input_string.split():
            if item in self.words:
                numbers.append(self.words[item])
            else:
                try:
                    numbers.append(float(item))
                except ValueError:
                    pass
        return sum(numbers)
#result = calculator.add_numbers("1 + 1 + 12")
#print(result)  
