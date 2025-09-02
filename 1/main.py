num = input("number:   ")
result = num[0]

for x in range (1, (len(num))):
    digit = num[x]
    if int(digit) < int(result):
        result = digit
print(result)