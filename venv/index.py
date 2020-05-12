




def checkNum(inputNum):
    if int(inputNum) == 0:
        print(inputNum+" is neither prime nor composite.")
        main()
    elif int(inputNum) == 1:
        print(inputNum + " is neither prime nor composite.")
        main()
    else:
        calculate(inputNum)


def main():
    inputNum = input("Please Enter a Number : ")
    if inputNum.upper() == "EXIT":
        exit()
    if int(inputNum) < 0:
        print("Please Enter Positive Numbers only!!!")
        main()
    else:
        checkNum(inputNum)


main()