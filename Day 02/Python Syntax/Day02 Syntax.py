#Day Two of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 02 Feb 2022
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
    def comparelength(int1,int2):
        if int1 > int2:
          print("First Name is longer than Last Name")
        elif int1 < int2:
          print("First Name is shorter than Last Name")
        else:
          print("First Name and Last Names have same length")

    os.system("cls") # clear console
    s0, s1 = "", 'Exercise level 1'
    s2 = 'Exercise level 2'

    for i in range(20):
      s0 += "@:"
    
    s = s0 + s1 + s0
    print(s)

    tempstr = os.path.curdir
    foldername = "Variable Folder"
    try:
        os.makedirs(foldername)    
    except FileExistsError:
        print("Directory " , foldername ,  " already exists") 
    newpath = os.path.join(tempstr, foldername)
    os.chdir(newpath)
    try:
        myfile = open("variables.py","w+")
        myfile.close()
        print("File \'" + myfile.name + "\' created or updated")
    except:
        print("Error updating or writing to file") 

    #Write a python comment saying 'Day 2: 30 Days of python programming'

    fname, lastname = "John","Constantine"  
    fullname = fname + ' '   + lastname
    mycountry = "gitland"
    mycity = "gitville"
    myage = 18
    myyear = 2022
    is_married = False
    is_true = True
    is_lighton= True

    myString2 = "Variable: {} is of data type:-\t{}"
    s = s0 + s2 + s0
    print(s)
    #1. Check data types of the variables

    print (myString2.format(fname,type(fname)))
    print (myString2.format(lastname,type(lastname)))
    print (myString2.format(fullname,type(fullname)))
    print (myString2.format(mycountry,type(mycountry)))
    print (myString2.format(mycity,type(mycity)))
    print (myString2.format(myage,type(myage)))
    print (myString2.format(myyear,type(myyear)))
    print (myString2.format(is_married,type(is_married)))
    print (myString2.format(is_true,type(is_true)))
    print (myString2.format(is_lighton,type(is_lighton)))

    #2
    print ("Length of firstname: \""+ fname+"\" is "+ str(len(fname)))

    #3
    print ("Length of fullname: \""+ fullname+"\" is "+ str(len(fullname)))
    lenfirst, lenlast = len(fname), len(lastname)
    comparelength(lenfirst,lenlast)
    
    #4
    num_one, num_two = 5,4
    total = num_one+ num_two
    var_diff = num_one-num_two
    var_product = num_one*num_two
    var_remainder = num_one%num_two
    var_exp = num_one**num_two
    var_floor_div = num_one//num_two

    print(total)
    print(var_diff)
    print(var_product)
    print(var_remainder)
    print(var_exp)
    print(var_floor_div)

    #5
    circleRadius = 30
    area_of_circle = math.pi * 30 ** 2
    circum_of_circle = math.pi * 30 * 2

    try:
      userradius = int(input("Enter a user-defined circle radius:\n"))
    except:
      print("Enter a valid number!\n")
      userradius = int(input("Enter a user-defined circle radius:\n"))
    print("Area of Circle with radius "+str(userradius) + " meters is " + "{:.2f}".format(math.pi * userradius ** 2))

    #6
    string1 = input("Please input your first name:\n")
    string2 = input("Please input your last name:\n")
    string3 = input("Please input your country\n")
    string4 = input("Please input your age\n")

    #7
    help('keywords')


if __name__ == "__main__":
  main()
