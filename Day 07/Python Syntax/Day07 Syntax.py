#Day Seven of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 06 Feb 2022
# IDE: VSCode

# import the "sys" module
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math

#set uses curly braces also just like dicts but does not key:values
# they are unordered
#Converting list to set removes duplicates
def main():

  os.system("cls") # clear console
  it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
  A = {19, 22, 24, 20, 25, 26}
  B = {19, 22, 20, 25, 26, 24, 28, 27}
  age = [22, 19, 24, 25, 26, 24, 25, 24]

  s1 = 'Day 7 Exercise level 1'
  s2 = 'Day 7 Exercise level 2'
  s3 = 'Day 7 Exercise level 3'
  s0 =  ''

  for i in range(20):
    s0 += "--"

  s = s0 + s1 + s0
  print(s)

  #1 Find the length of the set it_companies
  print("Number 1")
  print(len(it_companies))
  print("\n")

  #2  Add 'Twitter' to it_companies
  print("Number 2")
  print("original set: ",it_companies)
  it_companies.add("Twitter")
  print("Adding twitter to set: ",it_companies)
  print("\n")
  
  #3 Insert multiple IT companies at once to the set it_companies - use update
  print("Number 3")
  print("original set: ",it_companies) #- add Netflix, Dell, Alibaba
  newset = set(("Netflix","Dell", "Alibaba","Amazon"))
  it_companies.update(newset)
  print("Adding new set to set - update removes duplicates: ",it_companies)
  print("\n")
  
  #4 Remove one of the companies from the set it_companies
  it_companies.remove("Netflix")
  print("Removed set: ",it_companies)


  #5 What is the difference between remove and discard
  print("""The remove() method will 
  raise an error if the specified item does not exist, 
  and the discard() method will not.""")

  s = s0 + s2 + s0
  print(s)

  #1 Join A and B
  print("Number 1")
  print("Set A: ",A)
  print("Set B: ",B)
  new_set = A.copy()
  new_set.union(B)
  print("A Union B: ",new_set)
  print("\n")
