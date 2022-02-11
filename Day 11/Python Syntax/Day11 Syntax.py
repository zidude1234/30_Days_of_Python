#Day Eleven of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 12 Feb 2022
# IDE: VSCode

# import the "sys" module
from ast import arguments
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math
# import the "re" module
import re

from formulalibrary import *

def main():
  os.system("cls") # clear console

  s1 = 'Day 11 Exercise level 1'
  s2 = 'Day 11 Exercise level 2'
  s3 = 'Day 11 Exercise level 3'
  s0 =  ''

  for i in range(20):
    s0 += "--"

  s = s0 + s1 + s0
  print(s)
    
  def add_two_numbers(int1,int2):
    return int1 + int2

  #1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
  print("Number 1")
  num1 = int(input("Enter number one:\n"))
  num2= int(input("Enter number two:\n"))
  print(f'The sum of {num1} and {num2} is {add_two_numbers(num1,num2)}')
  print('\n')

  #2 using modules to clean up code
  # Write a function that calculates area_of_circle.
  print("Number 2")
  rad1 = int(input("Enter radius of circle:\n"))
  dim1= input("Enter dimension of circle(cm/m/km):\n")
  print(area_of_circle(rad1,dim1))
  print('\n')

  #3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
  # Check if all the list items are number types. If not do give a reasonable feedback.
  print("Number 3")
  tp_list1 = (8,3,5,7,'j')
  tp_list2 = ('gh',5,4,32,40,68,95)
  tp_list3 = (5,24,7,0,3,5,7,6,'[7]')

  print(add_all_nums(tp_list1))
  print(add_all_nums(tp_list2))
  print(add_all_nums(tp_list3))

  print(add_all_nums(7,5,'j'))
  print('\n')
  
  #4 Write a function which converts °C to °F. 
  print("Number 4")
  print(convert_celsius_to_fahrenheit(1000))
  print(convert_celsius_to_fahrenheit('f'))
  print('\n')

  #5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
  print("Number 5")
  print(check_season('January'))
  print(check_season('January','April','Gregorian'))
  print('\n')

if __name__ == "__main__":
  main()
