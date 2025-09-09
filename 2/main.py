def main(number):
    
    sum = 0

    for x in range(len(str(number))):

        sum += number % 10
        number = number // 10
        ## או int((str(number))[x]), אני לא יודע את מותר במבחן

    print(sum)


main(int(input("enter a number:  ")))