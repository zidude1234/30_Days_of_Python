#Day Four of the 30 Day Challenge
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
    
    #20
    #Use index to determine the position of the first occurrence of C in Coding For All.
    print("Number 20")
    print(company.index("C")+1) 
    print("\n")

    #21
    #Use index to determine the position of the first occurrence of F in Coding For All.
    print("Number 21")
    print(company.index("F")+1) 
    print("\n")

    #22
    #Use rfind to determine the position of the last occurrence of l in Coding For All People.
    print("Number 22")
    print("Last occurrence of the word 'l':",company.rindex("l")+1) 
    print("\n")

    #Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
    # 'You cannot end a sentence with because because because is a conjunction'
    print("Number 23")
    newstr = 'You cannot end a sentence with because because because is a conjunction'
    print("first occurrence of the word 'because':",newstr.index("because")+1) 
    print("\n")
    
    #24
    #Use rindex to find the position of the last occurrence of the word because in the following sentence: 
    # 'You cannot end a sentence with because because because is a conjunction'
    print("Number 24")
    print("last occurrence of the word 'because':",newstr.rindex("because")+1) 
    print("\n")


    #25
    #Slice out the phrase 'because because because' in the following sentence: 
    # 'You cannot end a sentence with because because because is a conjunction'
    print("Number 25")
    templist = newstr.split('because')
    templist2 = []
    print("Original Word:",newstr)
    print("Split List before spaces",templist)
    for i in templist:
      if i != ' ':
        templist2.append(i.strip()) #remove all leading or lagging spaces
    newword = ' '.join(templist2) #use space to join each list item
    print("Split List after spaces",templist2)
    print("Final word:",newword)
    print("\n")

    #26
    #Find the position of the first occurrence of the word 'because' in the following sentence: 
    # 'You cannot end a sentence with because because because is a conjunction''
    print("Number 26")
    x = re.search('because',newstr)
    print("first index of because",x.span())
    print("\n")

    #27 slice out the phrase 'because because because' in the following sentence: 
    # 'You cannot end a sentence with because because because is a conjunction'
    print("Number 27")
    print("Final word:",newword)
    print("\n")

    #28 Does 'Coding For All' start with a substring Coding?
    print("Number 28")
    print("'Coding For All' Starts with 'Codng'? T/F:",company.startswith('Coding'))
    print("\n")

    #29  Does 'Coding For All' end with a substring coding?
    print("Number 29")
    print("'Coding For All' Ends with 'Codng'? T/F:",company.endswith('Coding'))
    print("\n")


    #30 '   Coding For All      ', remove the left and right trailing spaces in the given string.
    print("Number 30")
    s_temp ='   Coding For All      '
    print("Original Word:",s_temp)
    print(":Striped String:",s_temp.strip())
    print("\n")


    #31 Which one of the following variables return True when we use the method isidentifier():
    # - 30DaysOfPython
    # - thirty_days_of_python
    print("Number 31")
    a,b =  '30DaysOfPython','thirty_days_of_python'
    print(f"is {a} a valid identifier?T/F: {a.isidentifier()}")
    print(f"is {b} a valid identifier?T/F: {b.isidentifier()}")
    print("\n")

    
    #32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
    # Join the list with a hash with space string.
    print("Number 32")
    hashspace = '# '
    list_libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
    print(hashspace.join(list_libraries))
    print("\n")
    
    #33 Use the new line escape sequence to separate the following sentences.
    #     I am enjoying this challenge.
    #     I just wonder what is next.
    print("Number 33")
    a, b = 'I am enjoying this challenge','I just wonder what is next'
    templist = a.split()
    print(a)
    for i in templist:
      print(i)
    print("\n")    
    
    templist = b.split()
    print(b)
    for i in templist:
      print(i)
    print("\n")


    #34 Use a tab escape sequence to write the following lines.
    # Name      Age     Country   City
    # Asabeneh  250     Finland   Helsinki
    
    #using dict
    myDict = dict(Name = "Asabeneh",Age = 250,Country = "Finland",City = "Helsinki")
    #myDict2 = {"Name":"Asabeneh","Age": 250,"Country":"Finland","City":"Helsinki"}
    print("Number 34")
    print("My Dict",myDict)
    #print(myDict2)
    
    item_string = ''
    for i in myDict.keys():
      item_string += str(i) + '\t'
    print(item_string)

    value_string = ''
    for i in myDict.values():
      value_string += str(i) + '\t'
    print(value_string) 
    
    #35
    #Use the string formatting method to display the following:
    #radius = 10
    #area = 3.14 * radius ** 2
    # The area of a circle with radius 10 is 314 meters square.   
    rad, area,area_string  = 10,0,'area = 3.14 * radius ** 2'
    print("Number 35")
    print("radius =", rad)
    print(area_string)
    print(f'The area of a circle with radius {rad} is {int(3.14 * rad **2)} meters square')
    print('\n')
    
    #36
    #Make the following using string formatting (interpolation) methods:
        # 8 + 6 = 14
        # 8 - 6 = 2
        # 8 * 6 = 48
        # 8 / 6 = 1.33
        # 8 % 6 = 2
        # 8 // 6 = 1
        # 8 ** 6 = 262144
     
    int1, int2 = 8,6
    print(f'{int1} + {int2} = {int1 + int2}')
    print(f'{int1} - {int2} = {int1 - int2}')
    print(f'{int1} * {int2} = {int1 * int2}')
    print(f'{int1} / {int2} = {(int1 / int2):.2f}')
    print(f'{int1} % {int2} = {int1 % int2}')
    print(f'{int1} // {int2} = {int1 // int2}')
    print(f'{int1} ** {int2} = {(int1 ** int2):,}')
      
    
    

if __name__ == "__main__":
  main()

