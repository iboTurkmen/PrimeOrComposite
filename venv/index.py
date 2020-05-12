
def prime(inputNum):
    factors = ""
    iteration = 1
    for number in range(2, int(inputNum)):
        iteration += 1
    print(inputNum + " is prime number and factors are -> " + inputNum)
    print("With 1st method number of iteration  is: " + str(iteration))
    main()


def composite(inputNum):
    factors = ""
    iteration = 1
    for number in range(2, int(inputNum)):
        iteration += 1
        if int(inputNum) % number == 0:
            factors += str(number)+","
    print(inputNum+" is composite number and factors are -> "+factors+inputNum)
    print("With 1st method number of iteration  is: " + str(iteration))
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