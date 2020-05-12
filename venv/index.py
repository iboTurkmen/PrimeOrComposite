import math


def prime(inputNum):
    method1 = 1
    method2 = 1
    i = 2
    for number in range(2, int(inputNum)):
        method1 += 1
    while int(inputNum) > 1 and i <= math.sqrt(int(inputNum)):
        while int(inputNum) / i:
            method2 += 1
            break
        method2 += 1
        break
    print(inputNum + " is prime number and factors are -> " + inputNum)
    print("With 1st method number of iteration  is: " + str(method1))
    print("With 2st method number of iteration  is: " + str(method2))
    main()


def composite(inputNum):
    factors = ""
    method1 = 1
    method2 = 1
    i = 2
    for number in range(2, int(inputNum)):
        method1 += 1
        if int(inputNum) % number == 0:
            factors += str(number)+","
    while int(inputNum) > 1 and i <= math.sqrt(int(inputNum)):
        while int(inputNum) / i:
            method2 += 1
            break
        method2 += 1
        break
    print(inputNum+" is composite number and factors are -> "+factors+inputNum)
    print("With 1st method number of iteration  is: " + str(method1))
    print("With 2st method number of iteration  is: " + str(method2))
    main()


def checkNum(inputNum):
    if int(inputNum) == 0:
        print(inputNum+" is neither prime nor composite.")
        main()
    elif int(inputNum) == 1:
        print(inputNum + " is neither prime nor composite.")
        main()
    else:
        if int(inputNum) == 2:
            print(inputNum + " is prime number and factors are -> " + inputNum)
            print("With 1st method number of iteration  is: 1")
            main()
        else:
            for number in range(2, int(inputNum)):
                if int(inputNum) % number == 0:
                    composite(inputNum)
                    break
                else:
                    prime(inputNum)
                    break


def main():
    print("For Exit please enter 'EXIT' or 'exit'")
    inputNum = input("Please Enter a Number : ")
    if inputNum.upper() == "EXIT":
        exit()
    if inputNum == "":
        main()
    if int(inputNum) < 0:
        print("Please Enter Positive Numbers only!!!")
        main()
    else:
        checkNum(inputNum)


main()