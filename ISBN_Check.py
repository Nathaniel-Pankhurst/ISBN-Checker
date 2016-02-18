#ISBN_Check
#
#Python based International Standard Book Number Checksum
#working on both 10 and 13 digit ISBN codes.
#
#Author: Nathaniel Pankhurst
#Date: 24/01/2016

def getISBN():
#Retrieves ISBN from user in form of String and validates the input.
        validate = False
        while not validate: 
                try:
                                ISBNstr = input("Please enter the ISBN: ")
                                ISBNVal = int(ISBNstr)
                                if len(ISBNstr) in [9, 12]:
                                        validate = True
                                else: 
                                        print("That ISBN is of incorrect length. Please try again.")
                except ValueError: 
                       print("Input was of invalid type, remember that ISBN codes consist of numbers 0 - 9 and nothing else. Please try again. ")
        return ISBNstr

def getDigits(ISBNstr):
#Defines the ISBN code as an array of Integers obtained through string manipulation.
        digitList = []
        digitStepper = 0
        while not (digitStepper == len(ISBNstr)):
                    digitList.append(int(ISBNstr[digitStepper]))
                    digitStepper = digitStepper + 1
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


def checkSum(ISBNstr, ISBN):
#Chooses checkSum dependant upon ISBN type, then returns finished ISBN with check digit. 
        if (len(ISBNstr) == 9):
                checkDigit = digit10(ISBN)
        if (len(ISBNstr) == 12):
                checkDigit = digit13(ISBN)
        ISBNstr = ISBNstr + "-" + str(checkDigit)
        return ISBNstr


def main():
#This is the main function. It is called upon launch of the program
#and calls functions to initiate the execution of the program.##
        finished = False
        while not finished:
            ISBN = []
            ISBNstr = getISBN()
            ISBN = getDigits(ISBNstr)
            finISBN = checkSum(ISBNstr, ISBN)
            print("The ISBN including the check digit is:"  + finISBN)
            isFinished = input("Would you like to check another ISBN? (y/n): ")
            if isFinished.lower() in ['y',  "yes"]:
                    finished = False
            elif isFinished.lower() in ['n', "no"]:
                    finished = True
            else:
                    print("that input was invalid try again.")
        print("Thank you for using our service. Come again.")

main()
