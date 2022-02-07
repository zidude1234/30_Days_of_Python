#Day Eight of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 07 Feb 2022
# IDE: VSCode

# import the "sys" module
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math
# import the "re" module
import re

def main():

  os.system("cls") # clear console
  
  s1 = 'Day 8 Exercise level 1'
  s0 =  ''

  for i in range(20):
    s0 += "--"

  s = s0 + s1 + s0
  print(s)
  #1. Create an empty dictionary called dog
  print("Number 1")
  dog= dict()
  print("Dog Dict: ", dog)
  print("\n")

  #2. Add name, color, breed, legs, age to the dog dictionary
  print("Number 2")
  dog["name"] = "Cujo"
  dog["breed"] = "St Bernard"
  dog["legs"] = 4
  dog["age"] = 7
  print("Dog Dict: ", dog)
  print("\n")

  #3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
  print("Number 3")
  student_dict = {"first_name":"Harry", "last_name":"Potter", "gender":"male", "age":17, "marital_status":"Single", 
  "skills":"wizardry","country":"England","city":"London","address":"100 Baker Street"}
  print(student_dict)
  print("\n")

  #4. Get the length of the student dictionary
  print("Number 4")
  print(len(student_dict))
  print("\n")


  #5. Get the value of skills and check the data type, it should be a list
  print("Number 5")
  print(student_dict["skills"])
  print(type(student_dict["skills"]))
  print("\n")


  #6. Modify the skills values by adding one or two skills
  print("Number 6")
  print(student_dict)
  student_dict["skills"]=("wizardry","quidditch","flying")
  print(student_dict)
  print("\n")

  #7 Get the dictionary keys as a list
  print("Number 7")
  print("Student Keys:", student_dict.keys())
  print("\n")

  #8 Get the dictionary values as a list
  print("Number 8")
  print("Student Value:", student_dict.values())
  print("\n")
  
  #9 Change the dictionary to a list of tuples using items() method
  print("Number 9")
  print("Student Items:", student_dict.items())
  student_list = list(student_dict.items ())
  print("Student Items as a List:",student_list)
  print("\n")

  #10 Change the dictionary to a list of tuples using items() method
  print("Number 10")
  student_tuples = tuple(student_dict.items ())
  print("Student Items as a Tuple:",student_tuples)
  print("\n")

  #11 Delete one of the items in the dictionary
  print("Number 11")
  print("Student Items before deletion",student_dict)
  del student_dict["marital_status"]
  print("Student Items before deletion",student_dict)
  print("\n")

  #12 Delete one of the dictionaries
  print("Number 12")
  del student_dict
  try:
    print(f"Student Dict",student_dict)
  except NameError as e:
    print("Dict does not exist")
    print(e)
  print("\n")

    
if __name__ == "__main__":
  main()
