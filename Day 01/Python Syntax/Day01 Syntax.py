#Day One of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 01 Feb 2022
# IDE: VSCode

# import the "sys" module
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math

def main():

    os.system("cls") # clear console
    #1. Print the python version details
    print("Python version", sys.version)
    print("Version info.",sys.version_info)
    print('\n')
    #Bonus
    print("Python Platfrom version",platform.python_version())

    print('\n')
    #2. Simple Operations
    #Define multiline variables a = 3 and b = 4
    a , b = 3, 4
    myString = "{} {} {} equals {}"

    #addition operation
    print ("a. Addition Operation:\t" + myString.format(a,'+',b, a+b))
    #subtraction operation
    print ("b. Subtraction Operation:\t" + myString.format(a,'-',b, a-b))
    #Multiply operation
    print ("c. Multiply Operation:\t" + myString.format(a,'*',b, a*b))
    #Modulo operation
    print ("d. Modulo Operation:\t" + myString.format(a,'%',b, a%b))
    #Division operation
    print ("e. Division Operation:\t" + myString.format(a,'/',b, a/b))
    #Exponent operation
    print ("f1. Exponent Operation:\t" + myString.format(a,'**',b, a**b))
    #Floor Division operation
    print ("g. Floor Division Operation:\t" + myString.format(a,'//',b, a//b))

    #Bonus - Exponent operation (import math module)
    print ("f2. Exponent Operation:\t" + myString.format(a,'pow',b, math.pow(a,b)))
    print('\n')

    #3. Strings

if __name__ == "__main__":
  main()
