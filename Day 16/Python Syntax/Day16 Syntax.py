#Day Sixteen of the 30 Day Challenge
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
from datetime import datetime, date, timedelta,time

def main():
  os.system("cls") # clear console
  
  def p(num):
    print(f"Number {num}")
  
  def pn():
    print("\n")

  def bannergreeting(day_name,exercise_name):
    daybanner = f'Exercise {day_name} '
    exercisebanner = f'Level {exercise_name} '
    front_end = f'--' * 20
    return combinebanners(front_end,daybanner,exercisebanner)
  
  def combinebanners(s0,s1,s2):
    return s0 + s1 + s2 + s0

  banner = bannergreeting
  print(banner(16,1))


  #1 Get the current day, month, year, hour, minute and timestamp from datetime module
  pn()
  p(1)
  timeObject1 = datetime(2017, 11, 28, 23, 55, 59, 342380)
  print("day =", timeObject1.day)
  print("month =", timeObject1.month)
  print("year =", timeObject1.year)
  print("hour =", timeObject1.hour)
  print("minute =", timeObject1.minute)
  print("timestamp =", timeObject1.timestamp())
  pn()
  #2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
  p(2)
  print(timeObject1.strftime("%m/%d/%Y, %H:%M:%S"))
  pn()
  
  #3 Today is 5 December, 2019. Change this time string to time.
  p(3)
  date_string = "5 December, 2019"
  print("date_string =", date_string)
  date_object = datetime.strptime(date_string, "%d %B, %Y")
  print("date_object =", date_object)
  pn()

  #4 Calculate the time difference between a time and new year.
  p(4)
  newyeartime = datetime(2018, 1, 1, 00, 00, 00, 00)
  time_diff = newyeartime - timeObject1
  print("Time difference:",time_diff)
  pn()

  #5 Calculate the time difference between 1 January 1970 and now.
  p(5)
  oldtime = datetime(1970, 1, 1, 00, 00, 00, 00)
  time_diff =  timeObject1 - oldtime 
  print(time_diff)
  print(f"Time difference: {time_diff.days} days")
  pn()
  

if __name__ == "__main__":
  main()
