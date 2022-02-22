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

  print(banner(18,2))
  #1. Write a pattern which identifies if a string is a valid python variable    
  p(1)
  stringvar = ['first_name','first-name','1first_name','firstname']
  regexpattern_v = '^[A-Za-z_]\w*$'
  for i in stringvar:
    if re.match(regexpattern_v,i):
      print(i,"True")
    else:
      print(i,"False")

  print(banner(18,3))
  #1. Clean the following text. After cleaning, count three most frequent words in the string.   
  p(1)
  sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

  replace_pattern = '@|%|\$|&|;|#|!'
  
  def clean_text(sentence): 
    return re.sub(replace_pattern, '', sentence)

  def most_frequent_words(sentence): 
    seperate_words = list(filter(None,re.split('\s+|\.',sentence))) #this includes space with it.
    words_group = collections.Counter(seperate_words)
    w_tp = words_group.items()
    w_tp2 = [(b,a) for (a,b) in w_tp] 
    w_tuple = sorted(w_tp2,key = lambda k:k[0],reverse=True)
    return w_tuple[0:3]

  print(clean_text(sentence))
  a = clean_text(sentence)
  print(most_frequent_words(a))


  
if __name__ == "__main__":
  main()
