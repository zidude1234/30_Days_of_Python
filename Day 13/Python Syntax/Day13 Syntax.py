#Day Three of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: xx Feb 2022
# IDE: VSCode

# import the "sys" module
from ast import comprehension
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math
import re
import copy

def main():

  os.system("cls") # clear console
  s1 = 'Day 13 Exercise level 1'
  s0 =  ''

  for i in range(20):
    s0 += "--"

  s = s0 + s1 + s0
  print(s)

  print("Number 1")
  numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
  list_neg_zero = [i for i in numbers if i <= 0]
  print("Original List:",numbers)
  print(list_neg_zero)
  print('\n')
  
  #2 Flatten the following list of lists of lists to a one dimensional list :
  print("Number 2")
  list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]] #This is a 3D List of lists
  level2 = [level2 for level1 in list_of_lists for level2 in level1]
  print("Level 1", level2)

  #3 Using list comprehension create the following list of tuples
  print("Number 3")
  list_of_tuples_of_number = [(i,1,i,i ** 2, i **3, i **4, i ** 5) for i in range(11)]
  print(list_of_tuples_of_number)
  print('\n')

  #4
  x = []
  for outerlist in countries:
     for inneritem in outerlist:
         temp_list = list(inneritem)
         temp_list.insert(1,temp_list[0][0:3])
         i = [i.upper() for i in temp_list]
         x.append(i)
  print(x)
  
  #5
  print('Number 5')
  key_dict = ['country','city']
  list_of_dict = []
  for outerlist in countries:
     for inneritem in outerlist:
         temp_list = list(inneritem)
         i = [i.upper() for i in temp_list]
         i_dict = dict(zip(key_dict,i))
         list_of_dict.append(i_dict)
  print("List of Dictionaries:", list_of_dict)

  #6
  names_to_compress = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
  print('Number 6')
  list003 = [second_tuple[0] + ' ' + second_tuple[1]  for first_tuple in names_to_compress for second_tuple in first_tuple ]
  print("Combined String List:", list003)
  print('\n' * 5)

