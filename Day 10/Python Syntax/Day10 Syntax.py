#Day Three of the 30 Day Challenge
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
