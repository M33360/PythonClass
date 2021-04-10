symbols = ['+']

def checkNum(number):
    try:
        return int(number)
    except ValueError:
        if number not in symbols:
            raise ValueError
        return number

calculation = input('Calculation: ').split(' ')

for i in calculation:
    i = checkNum(i)
    if type(i) != int:
        if i == '+':
            index = calculation.index(i)
            number1 = int(calculation[index - 1])
            number2 = int(calculation[index + 1])
            print(number1 + number2)