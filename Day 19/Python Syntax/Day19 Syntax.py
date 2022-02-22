#Day Nineteen of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 22 Feb 2022
# IDE: VSCode

# import the "sys" module
from importlib.resources import path
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math
# import the "re" module
import re
import collections
import datetime
from itertools import chain

def main():
  os.system("cls") # clear console
  
  def p(num):
    print(f"Number {num}")

  def pn(num = 1):
    print(f"\n" * num)

  def bannergreeting(day_name,exercise_name):
    daybanner = f'Exercise {day_name} '
    exercisebanner = f'Level {exercise_name} '
    front_end = f'--' * 20
    return combinebanners(front_end,daybanner,exercisebanner)
  
  def combinebanners(s0,s1,s2):
    return s0 + s1 + s2 + s0

  banner = bannergreeting
  print(banner(19,1))

  #1 Write a function which count number of lines and number of words in a text. 
  #  a) Read obama_speech.txt file and count number of lines and words 
  #  b) Read michelle_obama_speech.txt file and count number of lines and words 
  #  c) Read donald_speech.txt file and count number of lines and words 
  #  d) Read melina_trump_speech.txt file and count number of lines and words
  
  p(1)
  #python file is in Day19/Python Syntax folder
  #data file is in Day19/data folder
  
  fulldir = os.path.dirname(__file__)
  rootdir = fulldir.rsplit('\\',1) 
  newpath=rootdir[0]+'\\data\\'
 
  _obamapath = "".join([newpath,'obama_speech.txt'])
  _michpath = "".join([newpath,'michelle_obama_speech.txt'])
  _trumppath = "".join([newpath,'donald_speech.txt'])
  _melapath = "".join([newpath,'melina_trump_speech.txt'])
  #1A 
  f1 = open(_obamapath)
  Lines = f1.readlines() #All Lines
  Linenum = 0
  for linetext in Lines:
    Linenum +=1
  filename = _obamapath.rsplit('\\',1)[1]
  print(f"{filename} has {Linenum} lines")
  f1.close()

  f2 = open(_michpath)
  Lines = f2.readlines() #All Lines
  Linenum = 0
  for linetext in Lines:
    Linenum +=1
  filename = _michpath.rsplit('\\',1)[1]
  print(f"{filename} has {Linenum} lines")
  f2.close() 

  f3 = open(_trumppath)
  Lines = f3.readlines() #All Lines
  Linenum = 0
  for linetext in Lines:
    Linenum +=1
  filename = _trumppath.rsplit('\\',1)[1]
  print(f"{filename} has {Linenum} lines")
  f3.close() 
  
  
  f4 = open(_melapath)
  Lines = f4.readlines() #All Lines
  Linenum = 0
  for linetext in Lines:
    Linenum +=1
  filename = _melapath.rsplit('\\',1)[1]
  print(f"{filename} has {Linenum} lines")
  f4.close() 
  
  
  
  
  
  
if __name__ == "__main__":
  main()
