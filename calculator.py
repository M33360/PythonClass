# Loop 1 to find first number
while True:
    # Try to get the first number
    try:
        number = int(input('Give me a number: '))
        break
    # If the input is not a number, ask again
    except ValueError:
        print("Give me number!")

# Loop 2 to find second number
while True:
    # Try to get the second number
    try:
        number2 = int(input('Give me another number: '))
        break
    # If the input is not a number, ask again
    except ValueError:
        print("Give me number!")

# Multiply the two number
print(number * number2)