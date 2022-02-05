#Day Three of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 04 Feb 2022
# IDE: VSCode

# import the "sys" module
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math
import re



def main():

    os.system("cls") # clear console

    #1
    #Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
    print("Number 1")
    s1, s2, s3, s4 = 'Thirty', 'Days', 'Of', 'Python'
    s = s1 +" " + s2 + " " + s3 + " " + s4
    print(s)
    print("\n")
    

    #2
    #Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
    print("Number 2")
    s1, s2, s3 = 'Coding', 'For' , 'All'
    s =  s1 +" " + s2 + " " + s3
    print(s)
    print("\n")
    
    #3
    #Declare a variable named company and assign it to an initial value "Coding For All".
    company =  "Coding For All"
    
    #4
    print("Number 4")
    print(company)
    print("\n")

    #5
    print("Number 5")
    print(len(company))
    print("\n")

    #6
    # Change all the characters to uppercase letters using upper() method
    print("Number 6")
    print(company.upper())
    print("\n")

    #7
    # Change all the characters to uppercase letters using lower() method
    print("Number 7")
    print(company.lower())
    print("\n")

    #8
    # Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
    print("Number 8")
    print("Capitalize():", company.capitalize())  #First letter
    print("Title():", company.title())            #Title case
    print("Swapcase 1():", company.swapcase())      #Swapcase
    swap_company = company.swapcase()
    print("Swapcase 2():", swap_company.swapcase())      #Swapcase
    print("\n")
    
    #9
    # Cut(slice) out the first word of Coding For All string.
    print("Number 9")
    templist = company.split()
    print(templist[0]) 
    print("\n")

    #10
    #Check if Coding For All string contains a word Coding using the method index, find or other methods
    #find(): Returns the index of the first occurrence of a substring, if not found returns -1

    print("Number 10")
    searchstring = 'Coding'
    print(company.find(searchstring)) #0 is the beginning string
    print(searchstring in company)


    #11
    #Replace the word coding in the string 'Coding For All' to Python
    print("Number 11")
    str1 = 'Coding For All'
    print(str1.replace('Coding','Python'))
    
    #12
    #Change Python for Everyone to Python for All using the replace method or other methods
    #find(): Returns the index of the first occurrence of a substring, if not found returns -1
    print("Number 12")
    str1 = 'Python for Everyone'
    print(str1.replace('Everyone','All'))
   
    #13
    #Split the string 'Coding For All' using space as the separator (split()) 
    print("\n")
    print("Number 13")
    print('Coding For All'.split())
    print("\n")

    #14
    #Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma
    print("Number 14")
    s = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
    print(s.split(','))
    print("\n")
    
    #15
    #What is the character at index 0 in the string Coding For All.
    print("Number 15")
    print("Character at Index 0: ",'Coding For All'[0])
    print("\n")

    #16
    #What is the last index of the string Coding For All.
    s = 'Coding For All'
    print("Number 16")
    print("Character at Index last: ",s[len(s)-1])
    print("\n")
    
    #17
    #What character is at index 10 in "Coding For All" string.
    print("Number 17")
    print("Character at Index 10: ",s[10])
    print("\n")

    #18
    # Create an acronym or an abbreviation for the name 'Python For Everyone'.
    print("Number 18")
    s_acro, templist = '',str1.split()
    print(str1)
    for i in templist:
        s_acro += i[0]
    print("Acronym:",s_acro)
    print("\n")
    
    #19
    #Create an acronym or an abbreviation for the name 'Coding For All'.
    print("Number 19")
    s_acro, templist = '',company.split()
    print(company)
    for i in templist:
        s_acro += i[0]
    print("Acronym:",s_acro)
    print("\n")


    
    
    

if __name__ == "__main__":
  main()

