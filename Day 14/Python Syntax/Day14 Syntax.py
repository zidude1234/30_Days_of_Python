#Day Fourteen of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 14 Feb 2022
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
  print("Higher Order Functions")
  
  def bannergreeting(day_name,exercise_name):
    daybanner = f'Exercise {day_name} '
    exercisebanner = f'Level {exercise_name} '
    front_end = f'--' * 20
    return combinebanners(front_end,daybanner,exercisebanner)
  
  def combinebanners(s0,s1,s2):
    return s0 + s1 + s2 + s0
  
  banner = bannergreeting
  print(banner(14,1))

  def p(num):
    print(f"Number {num}")
  
  def pn():
    print(f"\n")
  
  #4 Use for loop to print each country in the countries list
  p(4)
  i = [print(i) for i in countries]
  pn()

  #5 Use for to print each name in the names list.
  p(5)
  i = [print(i) for i in names]
  pn()

  #6 Use for to print each number in the numbers list
  p(6)
  i = [print(i) for i in numbers]
  pn()

  print(banner(14,2))
  #1 Use map to create a new list by changing each country to uppercase in the countries list
  p(1)
  i = map(lambda x:x.upper(),countries)
  print(list(i))
  pn()

  #2 Use map to create a new list by changing each number to its square in the numbers list
  p(2)
  i = map(lambda x:x**2,numbers)
  print(list(i))
  pn()

  #3 Use map to change each name to uppercase in the names list
  p(3)
  i = map(lambda x:x.upper(),names)
  print(list(i))
  pn() 

  #4 Use filter to filter out countries containing 'land'.
  p(4)
  i = filter(lambda x:re.search('land',x) ,countries)
  print(list(i))
  pn()

  #5 Use filter to filter out countries having exactly six characters.
  p(5)
  i = filter(lambda x:len(x)==6 ,countries)
  print(list(i))
  pn()

 
  #6 Use filter to filter out countries containing six letters and more in the country list.
  p(6)
  i = filter(lambda x:len(x)==6 ,countries)
  print(list(i))
  pn() 
  
  
  
if __name__ == "__main__":
  main()
