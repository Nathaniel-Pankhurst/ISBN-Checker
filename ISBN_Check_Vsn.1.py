#ISBN_Check
#
#Python based International Standard Book Number Checksum
#working on both 10 and 13 digit ISBN codes.
#
#Author: Nathaniel Pankhurst
#Date: 23/01/2016

def getType():
#Defines the type of ISBN as an integer obtained through user input.
        validate = False
        while not validate:
                try: 
                    codeType = input("What type of ISBN is being used? 10, or 13 digit? (10/13): ")
                    codeType = int(codeType)
                    if codeType in [10, 13]:
                            validate = True
                    else:
                            print("There is no ISBN standard of that length. Try again.")
                except ValueError:
                       print("Input was of invalid type. Try again.")
        return codeType

def getDigits(codeType):
#Defines the ISBN code as an array of Integers obtained through user input.
        digitList = []
        digitStepper = 0
        while not (digitStepper == codeType - 1):
                try:
                    digitTest = input("whats is digit " + str(digitStepper + 1) + " in the ISBN?: ")
                    digitTest = int(digitTest)
                    if digitTest in range(0, 10, 1):
                            digitList.append(digitTest)
                            digitStepper = digitStepper + 1
                    else:
                            print("That digit is not possible to occur in an ISBN. Please try again")
                except ValueError:
                    print("Input was of invalid type. Try again.")
        return digitList

def digit10(ISBN):
#Works out checkDigit for 10 digit ISBN codes.
        addCount = 0
        addTotal = 0
        for i in range(10, 1, -1):
                addTotal = addTotal + ISBN[addCount] * i
                i = i + 1
                addCount = addCount + 1               
        checkDigit = 11 - (addTotal % 11) % 11
        return checkDigit
        


def digit13(ISBN):
#Works out checkDigit for 13 digit ISBN codes.
        addTotal = 0
        for i in range(0, 12, 1):
                if (i % 2 == 0):
                        addTotal = addTotal + ISBN[i] * 1
                if (i % 2 == 1):
                        addTotal = addTotal + ISBN[i] * 3
                i = i + 1
        remainder = addTotal % 10
        checkDigit = 10 - remainder
        return checkDigit

def finalISBN(codeType, ISBN, checkDigit):
#Combines the ISBN array and the checkDigit to make a string
        finISBN = ""
        finISBN = "-" + str(checkDigit)
        print("The ISBN including the check digit is: " + ''.join(str(x) for x in ISBN) + finISBN)

def checkSum(codeType, ISBN):
#Chooses checkSum dependant upon ISBN type, then returns finished ISBN with check digit. 
        if (codeType == 10):
                checkDigit = digit10(ISBN)
        if (codeType == 13):
                checkDigit = digit13(ISBN)
        finalISBN(codeType, ISBN, checkDigit)


def main():
#This is the main function. It is called upon launch of the program
#and calls functions to initiate the execution of the program.##
        ISBN = []
        codeType = getType()
        ISBN = getDigits(codeType)
        finISBN = checkSum(codeType, ISBN)

main()
