#Day Nine of the 30 Day Challenge
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
from math  import ceil

def main():

  os.system("cls") # clear console

  s1 = 'Day 9 Exercise level 1'
  s2 = 'Day 9 Exercise level 2'
  s3 = 'Day 9 Exercise level 3'
  s0 =  ''

  for i in range(20):
    s0 += "--"

  s = s0 + s1 + s0
  print(s)

  #1 Get user input using input(“Enter your age: ”). 
  # If user is 18 or older, give feedback: You are old enough to drive. 
  # If below 18 give feedback to wait for the missing amount of years. 
  print("Number 1")
  age_cap = 18
  age = int(input("Enter your age:\n"))
  print('You are old enough to learn to drive.') if age > 18 else print (f'You need {age_cap - age} more years to learn to drive.') 
  # first condition met, 'A is positive' will be printed
  print('\n')  

  #2 Compare the values of my_age and your_age using if … else
  print("Number 2")
  age = int(input("Enter your age, I am 25:\n"))
  my_age = 25
  if age < my_age:
      print("You are 1 year younger than me") if my_age - age == 1 else print(f'You are {my_age - age} years younger than me.') 
  elif age > my_age:
      print("You are 1 year older than me") if age - my_age == 1 else print(f'You are {age - my_age} years older than me.')
  else:
    print("We are equal in ages")
  print('\n')  

  #3 Get two numbers from the user using input prompt. 
  # If a is greater than b return a is greater than b, 
  # if a is less b return a is smaller than b, else a is equal to b.
  print("Number 3")
  num1 = int(input("Enter number one:\n"))
  num2 = int(input("Enter number two:\n"))
  if num1 < num2:
      print(f'{num1} is smaller than {num2}')
  elif num1 > num2:
      print(f'{num1} is greater than {num2}')
  else:
    print(f'{num1} is equal to {num2}')
  print('\n') 

  s = s0 + s2 + s0
  print(s)
  #1 Write a code which gives grade to students according to theirs scores:

  # 80-100, A
  # 70-89, B
  # 60-69, C
  # 50-59, D
  # 0-49, F

  print("Number 1")
  score = int(input("Enter the student score:\n"))
  if score in range(80,101):
      print(f'Your score: {score} has a grade of "A"')
  elif score in range(70,80):
      print(f'Your score: {score} has a grade of "B"')
  elif score in range(60,70):
      print(f'Your score: {score} has a grade of "C"')
  elif score in range(50,60):
      print(f'Your score: {score} has a grade of "D"')
  else:
      print(f'Your score: {score} has a grade of "F"')
  print('\n') 

  print("Number 2")
  month = input("Enter the month of the year:\n")
  if month in ('September', 'October','November'):
      print(f'The month of : {month} is "Autumn"')
  elif month in ('December','January','February'):
      print(f'The month of : {month} is "Winter"')
  elif month in ('March', 'April','May'):
      print(f'The month of : {month} is "Spring"')
  elif month in ('June', 'July', 'August'):
      print(f'The month of : {month} is "Summer"')
  else:
      print(f'The month of : {month} does not exist!')
  print('\n')

  #3. The following list contains some fruits:
  # fruits = ['banana', 'orange', 'mango', 'lemon']
  # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list') 
  print("Number 3")
  fruits = ['banana', 'orange', 'mango', 'lemon']
  #f1 = set(fruits)
  fr = input("Enter a fruit:\n")
  print("That fruit already exist in the list") if fr in fruits else fruits.append(fr)
  print("Updated fruit list:", fruits)
  print('\n')

  person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':  {
        'street': 'Space street',
        'zipcode': '02210'
                }
  }
  s = s0 + s3 + s0
  print(s)

#1 Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#2 Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#3 If a person skills has only JavaScript and React, print('He is a front end developer'), 
    # if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
    # if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
    # else print('unknown title') - for more accurate results more conditions can be nested!
#4 If the person is married and if he lives in Finland, print the information in the following format:
  print("Number 1")
  if person.get("skills"):
      print('skills exist') 
      skill_list = person['skills']
      length_list = len(skill_list)
      if length_list % 2 == 1:
        startindex = ceil(length_list/2)-1
        endindex = startindex + 1
        print("Middle skill:",str(skill_list[startindex:endindex]))
      else:
        startindex = ceil(length_list/2)-1
        endindex = startindex + 2 #endindex is not included
        print("Middle skills:",skill_list[startindex:endindex])
  else:
      print("skills does not exist")
  print('\n')
  #print('skills exist') if person.get("skills") else print("skills does not exist")

  print("Number 2")
  if 'Python' in  skill_list:
    print("Python is a skills present in the dictionary")
  else:
    print("Python is a skills NOT present in the dictionary")
  print('\n')

  print("Number 3")
  if skill_list == ["JavaScript","React"]:
    print("He is a front end developer")
  elif set(skill_list) == set(["Node", "Python", "MongoDB"]):
    print("He is a back end developer")
  elif set(skill_list) == set(( 'React', 'Node', 'MongoDB', 'Python','JavaScript',)):
    print("He is a full stack developer")
  else:
    print("Unknown Skillset")
  print('\n')

  print("Number 4")
  if person.get("is_married"):
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")
  else:
    print("He is not married")
  print('\n')



if __name__ == "__main__":
  main()

