#Day Seventeen of the 30 Day Challenge
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
import collections
import datetime

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
  print(banner(17,1))

  names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
  #Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively
  *nordic,es, ru = names

  print("names:",names)
  print("nordic:",nordic)
  


  

    
if __name__ == "__main__":
  main()
