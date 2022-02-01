#Day One of the 30 Day Challenge
# Introduction

# import the "sys" module
import sys
# import the "os" module
import os


def main():

    os.system("cls") # Windows4
    #1. Print the python version details
    print("Python version", sys.version)
    print("Version info.",sys.version_info)

    #2. Simple Operations
    #Define multiline variables a = 3 and b = 4
    a , b = 3, 4
    myString = "{} {} {} equals {}"

    #addition operation
    print (myString.format(a,'+',b, a+b))

if __name__ == "__main__":
  main()
