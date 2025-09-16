sum = 0
x = 1
print("Type '-1' to calculate the average!")
while True:

    inpt = int(input(f'Enter the {x} number:  '))
    if inpt == -1:
        break

    sum = sum + inpt
    x = x + 1

print(f'The average is {sum / (x-1)}!')