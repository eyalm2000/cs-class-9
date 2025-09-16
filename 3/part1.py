sum = 0
for x in range(10):
    inpt = int(input(f'Enter the {x+1} number:  '))
    sum = sum + inpt

print(f'The average is {sum / 10}!')