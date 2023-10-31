from sys import *
from Arithmatic import *

def main():
    print("-------------- Automation Script ------------------")

    print("Automation Script Name :",argv[0])

    if(len(argv) == 2):
        if(argv[1] == "-h" or argv[1] == "-H"):
            print("This automation script is used to perform addition of two number")
            exit()

        elif(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage : Name_of_script First_Argument Second_Argument")
            print("Example : Demo.py 11 10")
            exit()

        else:
            print("There is no such option to handle")
            exit()

    if(len(argv) != 3):
        print("Invalid number of argument")
        exit()
    else:
        Ret = Addition(int (argv[1]), int(argv[2]))
        print("Addition is :",Ret)


if __name__ == "__main__":
    main()