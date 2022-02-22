#Day Eighteen of the 30 Day Challenge
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
  print(banner(18,1))

  #1 What is the most frequent word in the following paragraph?
  paragraph = '''I love teaching. If you do not love teaching what else can you love. 
  I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
  
  split_words = re.split('\s+|\.',paragraph) 
  split_words = list(filter(None,split_words)) #because of the space filtered out
  print("Split Words:", split_words)
  
  words_collection = collections.Counter(split_words)
  print(words_collection)
  pn()
  
  word_tp = words_collection.items()
  word_tuple = [(b,a) for (a,b) in word_tp]
  word2 = sorted(word_tuple,key = lambda k: (k[0],k[1]), reverse=True)
  print("Final sorted Tuple:",word2)
  pn()
 
#2 Extract these numbers from this whole text and find the distance between the two furthest particles
  p(2)
  points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
  s1 = sorted(points,key = lambda k:int(k)) # ['-4', '-3', '-1', '-1', '0', '2', '4', '8']
  sorted_points = [int(i) for i in s1]
  print("original list:", points)
  print("sorted list:", sorted_points)
  print(f'distance = {max(sorted_points)} - {min(sorted_points)} = {max(sorted_points)-min(sorted_points)}')

    
if __name__ == "__main__":
  main()
