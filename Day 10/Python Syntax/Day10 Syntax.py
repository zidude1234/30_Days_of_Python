#Day Tenof the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 09 Feb 2022
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

  s1 = 'Day 10 Exercise level 1'
  s2 = 'Day 10 Exercise level 2'
  s3 = 'Day 10 Exercise level 3'
  s0 =  ''

  for i in range(20):
    s0 += "--"

  s = s0 + s1 + s0
  print(s)

  #1 Iterate 0 to 10 using for loop, do the same using while loop. 
  print("Number 1")
  print("Using For Loop from 0 to 10")
  for i in range(0,11):
    print(i)
  
  print(s0)
  print("Using While Loop from 0 to 10")
  i = 0
  while i <= 10:
    print(i)
    i +=1
  

  print('\n') 

  #2 Iterate 10 to 0 using for loop, do the same using while loop. 
  print("Number 2")
  print("Using For Loop from 10 to 0")
  for i in range(0,11):
    print(10 - i)
  
  print(s0)
  print("Using While Loop from 10 to 0")
  i = 10
  while i >= 0:
    print(i)
    i -=1 
  print('\n')

  #3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

  print("Number 3 -method 1 using multiplier")
  #method 1 using multiplier
  for i in range(1,8):
    print('#'*i)
  print('\n') 

  print("Number 3B - #method 2 using nested if")
  #method 2 using nested if
  for i in range(1,8):
    for j in range(0,i):
      if(j == i-1):
        print('#')
      else:
        print('#', end='')
      #if(j == i-1):
  print('\n') 


#4 Use nested loops to create the following:
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #

  print("Number 4")
  no = 8
  for i in range(0,no):
    for j in range(0,no):
      if(j == no-1):
        print('#')
      else:
        print('#', end='')
  print('\n')

#5. Print the following pattern:

    # 0 x 0 = 0
    # 1 x 1 = 1
    # 2 x 2 = 4
    # 3 x 3 = 9
    # 4 x 4 = 16
    # 5 x 5 = 25
    # 6 x 6 = 36
    # 7 x 7 = 49
    # 8 x 8 = 64
    # 9 x 9 = 81
    # 10 x 10 = 100

  print("Number 5")
  no = 11
  for i in range(0,no):
    print(f'{i} * {i} = {i * i}')
  print('\n')
  
  
  #6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
  print("Number 6")
  list1 = ['Python', 'Numpy','Pandas','Django', 'Flask']
  for i in range(0,len(list1)):
    print(f'{list1[i]}')
  print('\n')

  #7 Use for loop to iterate from 0 to 100 and print only even numbers.
  list100 = []
  print("Number 7")
  for i in range (0,101):
    list100.append(i)
  evenlist = [i for i in list100 if i % 2 == 0]
  print("Evenlist:",evenlist)
  print('\n')

  #8 Use for loop to iterate from 0 to 100 and print only odd numbers.
  print("Number 8")
  oddlist = [i for i in list100 if i % 2 == 1]
  print("Oddlist:", oddlist)
  print('\n')


  #1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
  s = s0 + s2 + s0
  print(s)
  sum100 = 0
  print("Number 1")
  for i in list100:
    sum100 += i
  print("The sum of all numbers is {sum100}.")
  print('\n')

  #2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
  sumeven100 = sumodd100 = 0
  print("Number 2")
  for i in oddlist:
    sumodd100 += i
  for i in evenlist:
    sumeven100 += i
  print(f"The sum of all evens is {sumeven100}. And the sum of all odds is {sumodd100}.")
  print('\n')
  
  
  # Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
  # This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
  # Go to the data folder and use the countries_data.py file.
      # What are the total number of languages in the data
      # Find the ten most spoken languages from the data
      # Find the 10 most populated countries in the world

  #1 
  land_countries = []
  s = s0 + s3 + s0
  print(s)
  print("Number 1")
  land_countries = [i for i in countries if re.search('land',i)]
  print(f"There are {len(land_countries)} Countries with 'land' in them:, {land_countries}.")
  print('\n')

  #2 
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print("Number 2")
  for i in range(1,len(fruits)+1):
    print(f"{fruits[-i]}")
  print('\n')
  
  




  
  
  
  
if __name__ == "__main__":
  main()
