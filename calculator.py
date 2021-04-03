# Loop 1 to find first number
while True:
    try:
        number = int(input('Give me a number: '))
        break
    except ValueError:
        print("Give me number!")

# Loop 2 to find second number
while True:
    try:
        number2 = int(input('Give me another number: '))
        break
    except ValueError:
        print("Give me number!")

print(number * number2)