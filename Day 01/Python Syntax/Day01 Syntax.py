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
    s1 = 'Exercise level 1'
    s2 = 'Exercise level 2'
    s3 = 'Exercise level 3'

    s0 = codeString = ''
    codeString ='''
#Helloworld code of the 30 Day Challenge
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
      #1. Print the python version details
      print("Python version", sys.version)
      print("Version info.",sys.version_info)
     
      #Bonus
      print('Bonus -- Python Platfrom version',platform.python_version())

    
      #2. Simple Operations
      #Define multiline variables a = 3 and b = 4
      a , b = 3, 4
      myString = "{} {} {} equals {}"

      #addition operation
      print ("a. Addition Operation:	" + myString.format(a,'+',b, a+b))
      #subtraction operation
      print ("b. Subtraction Operation:	" + myString.format(a,'-',b, a-b))
      #Multiply operation
      print ("c. Multiply Operation:	" + myString.format(a,'*',b, a*b))
      #Modulo operation
      print ("d. Modulo Operation:	" + myString.format(a,'%',b, a%b))
      #Division operation
      print ("e. Division Operation:	" + myString.format(a,'/',b, a/b))
      #Exponent operation
      print ("f1. Exponent Operation:	" + myString.format(a,'**',b, a**b))
      #Floor Division operation
      print ("g. Floor Division Operation:	" + myString.format(a,'//',b, a//b))

      #Bonus - Exponent operation (import math module)
      print ("f2. 'Bonus -- Exponent Operation:	" + myString.format(a,'pow',b, math.pow(a,b)))
      

      #3. Strings
      #Greeting
      intro = 'Hello, My Name is '
      enjoy = 'I am enjoying 30 days of Python.'


      string1 = input("Please input your first name:"
      )
      
      string2 = input("Please input your last name:")
      
      
      string3 = input("Please input your country")
      

      print( intro + string1 + " " + string2 + " from " + 
      string3 + "." + enjoy)

      #4. Data Types
      #Assign data from variables a to h
      a, b, c, d, e, f, g, h = 10, 9.8, 3.14, 4 - 4j, ['Asabeneh', 'Python', 'Finland'],string1, string2, string3
      #use type(x)
      myString2 = "Data: {} is of data type:-	{}"
      print (myString2.format(a,type(a)))
      print (myString2.format(b,type(b)))
      print (myString2.format(c,type(c)))
      print (myString2.format(d,type(d)))
      print (myString2.format(e,type(e)))
      print (myString2.format(f,type(f)))
      print (myString2.format(g,type(g)))
      print (myString2.format(h,type(h)))
      
      
if __name__ == "__main__":
    main()''' 

    for i in range(20):
      s0 += "@:"
    
    s = s0 + s1 + s0

    print(s)
    #1. Print the python version details
    print("Python version", sys.version)
    print("Version info.",sys.version_info)
    print('\n')
    #Bonus
    print('Bonus -- Python Platfrom version',platform.python_version())

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
    print ("f2. 'Bonus -- Exponent Operation:\t" + myString.format(a,'pow',b, math.pow(a,b)))
    print('\n')

    #3. Strings
    #Greeting
    intro = 'Hello, My Name is '
    enjoy = 'I am enjoying 30 days of Python.'


    string1 = input("Please input your first name:\n")
    string2 = input("Please input your last name:\n")
    string3 = input("Please input your country\n")

    print( intro + string1 + " " + string2 + " from " + 
    string3 + "." + enjoy)

    #4. Data Types
    #Assign data from variables a to h
    a, b, c, d, e, f, g, h = 10, 9.8, 3.14, 4 - 4j, ['Asabeneh', 'Python', 'Finland'],string1, string2, string3
    #use type(x)
    myString2 = "Data: {} is of data type:-\t{}"
    print (myString2.format(a,type(a)))
    print (myString2.format(b,type(b)))
    print (myString2.format(c,type(c)))
    print (myString2.format(d,type(d)))
    print (myString2.format(e,type(e)))
    print (myString2.format(f,type(f)))
    print (myString2.format(g,type(g)))
    print (myString2.format(h,type(h)))
    
    #'''Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, 
    # create a python file helloworld.py and repeat questions 1, 2, 3 and 4. 
    # Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.'''

    s = s0 + s2 + s0
    print(s)
    current_path_string = os.path.dirname( __file__ )
    #find the index of the last '\'
    tempnum = current_path_string.rfind("\\")
    tempstr = "" 
    #extract the string up till that index
    for i in range(tempnum):
      tempstr += current_path_string[i]
    
    #Tempstr is up one Directory
    #navigate to it
    os.chdir(tempstr)
    #create a new path for the Hello World Folder and file

    foldername = "HelloWorld Folder"
    try:
        os.makedirs(foldername)    
        print("Directory " , foldername ,  " Created ")
    except FileExistsError:
        print("Directory " , foldername ,  " already exists") 
    
    newpath = os.path.join(tempstr, foldername)
    os.chdir(newpath)
    myfile = open("hello.world.py","w+")
    
     

    myfile.write(codeString)
    myfile.close()


if __name__ == "__main__":
  main()
