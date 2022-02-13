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

  #calculate_slope which return the slope of a linear equation
  print("Number 6")
  num1 = int(input("Enter the x-coefficient:\n"))
  num2 = int(input("Enter the y-intercept:\n"))
  print(slope(num1,num2))
  print('\n')
  
  #Write a function which calculates solution set of a quadratic equation
  print("Number 7")
  print(solve_quadratic_eqn(1,7,10))
  print('\n') 

  #Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
  print("Number 8")
  print_list(list(tp_list1)) 
  print('\n')

  #9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
  print("Number 9")
  print(reverse_list(list(tp_list1)))
  print('\n')
  
 #10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
  list_words = ['bETTer beliEVE','cOLD COLd HeART', 'pEACHES in Georgia','sACrifICe']
  print("Number 10")
  print(f'The capitalised form of the list {list_words} is \n {capitalize_list_items(list_words)}')
  print('\n')
  
  #11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
  print("Number 11")
  list_mo_hits = []
  list_mo_hits = capitalize_list_items(list_words)
  print(add_items(list_mo_hits,"Take My Breath"))
  print('\n')
  
  #12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it  
  print("Number 12")
  print(remove_item(food_stuff, 'Mango'))
  print(remove_item(numbers, 3))
  print(remove_item(numbers, 10))
  print('\n')
  
  #13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
  print("Number 13")
  print(sum_all_numbers(5))  # 15
  print(sum_all_numbers(10)) # 55
  print(sum_all_numbers(100)) # 5050
  print('\n')
  
  #14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
  print("Number 14")
  print(sum_odd_numbers(5))  # 9
  print(sum_odd_numbers(10)) # 25
  print(sum_odd_numbers(100)) # 2500
  print('\n')
  
  #15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
  print("Number 15")
  print(sum_even_numbers(5))  # 6
  print(sum_even_numbers(10)) # 30
  print(sum_even_numbers(100)) # 2550
  print('\n')
  
  s = s0 + s2 + s0
  print(s)


  #1 Declare a function named evens_and_odds . It takes a positive integer as parameter and 
  # it counts number of evens and odds in the number.
    # print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
  print("Number 1")
  print(evens_and_odds(100))

  #2 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
  print("Number 2")
  print(my_factorial(5))
  print("\n")
  
  #3 Call your function is_empty, it takes a parameter and it checks if it is empty or not
  print("Number 3")
  
  s = ''
  listnew = []
  b = NULL
  d = 25
  e = ["5",6,9]
  list_check = list((s,listnew,b,d,e))
  print(list_check)
  print(is_empty(list_check))
  print("\n")

  print("Number 4")
  listdata = [4,3,5,8,'i']
  print_statistics(my_statistics(listdata))
  listdata2 = [4,3,5,8,5]
  print_statistics(my_statistics(listdata2))
  
  s = s0 + s3 + s0
  print(s)
  #1. Write a function called is_prime, which checks if a number is prime.
  print("Number 1")
  print(numberIsPrime(121))
  print('\n')

  #2 Write a functions which checks if all items are unique in the list.
  print("Number 2")
  print(listIsUnique(listdata2))
  listdata3 = ['1',2,1,"The dog flew over the moon",7,"The dog flew over the moon"]
  print(listIsUnique(listdata3))
  print(listIsUnique(listdata))
  print('\n')

  #3 Write a function which checks if all the items of the list are of the same data type.
  print(sameListType(listdata))
  print(sameListType(listdata2))
  
  #4 Write a function which check if provided variable is a valid python variable
  var_name = input("Enter desired variable name:\n")
  print(checkValidvariable(var_name))












































  
if __name__ == "__main__":
  main()
