#Day Fifteen of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 18 Feb 2022
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

  def p(num):
    print(f"Number {num}")
  
  def pn():
    print(f"\n")

  def bannergreeting(day_name,exercise_name):
    daybanner = f'Exercise {day_name} '
    exercisebanner = f'Level {exercise_name} '
    front_end = f'--' * 20
    return combinebanners(front_end,daybanner,exercisebanner)
  
  def combinebanners(s0,s1,s2):
    return s0 + s1 + s2 + s0

  banner = bannergreeting
  print(banner(15,1))

  p(1)
  print('Syntax Error\n')
  try:
    #print 'hello world' #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
    pass
  except SyntaxError as e:
    print("Syntax Error")
    print(e)
  finally:
    print("This happened at least")
  pn

  p(2)
  print('\nName Error')
  try:
    print(age) #'age' is not defined
  except NameError as e:
    print("Name Error")
    print(e)
  
  p(3)
  print('\nIndex Error')
  numbers = [1, 2, 3, 4, 5]
  try:
    print(numbers[5])
  except IndexError as e:
    print("Index Error")
    print(e)

  p(4)
  print('\nModule Error')
  try:
    import maths
  except ModuleNotFoundError as e:
    print("ModuleNotFoundError")
    print(e)

  p(5)
  print('\nAttribute Error')
  try:
    import math
    print(math.PI)
  except AttributeError as e:
    print("Maybe you mean pi?")
    print(e)
  
  p(6)
  print('\nKey Error')
  users = {'name':'Asab', 'age':250, 'country':'Finland'}
  try:
    print(users['county'])
  except KeyError as e:
    print("Check your dict key")
    print(e)

  p(7)
  print('\nType Error')
  try:
    x = 4 + '3'
    print(x)
  except TypeError as e:
    print("check the type of the data")
    print(e)

  p(8)
  print('\nZero Div Error')
  try:
    x = 10/0
    print(x)
  except ZeroDivisionError as e:
    print("Error - You divided by zero")
    print(e)
  

    
if __name__ == "__main__":
  main()
