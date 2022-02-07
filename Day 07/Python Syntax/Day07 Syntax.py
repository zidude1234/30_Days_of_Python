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
  print("Adding new set to set - update removes duplicates: \n",it_companies)
  print("\n")
  
  #4 Remove one of the companies from the set it_companies
  print("Number 4")
  it_companies.remove("Netflix")
  print("Remove Netflix from set: ",it_companies)
  print("\n")


  #5 What is the difference between remove and discard
  print("Number 5")
  print("""The remove() method will
  raise an error if the specified item does not exist,
  and the discard() method will not.""")
  print("\n")

  s = s0 + s2 + s0
  print(s)

  #1 Join A and B
  print("Number 1")
  print("Set A: ",A)
  print("Set B: ",B)
  new_set = A.copy()
  new_set.update(B)
  print("A updated with B: ",new_set)
  new_set1 = A.copy()
  print("Method 2 using Union():", A.union(B))
  print("\n")

  #2 Find A intersection B
  print("Number 2")
  print("Set A: ",A)
  print("Set B: ",B)
  new_set = A.intersection(B)
  print("A intersection B: ",new_set)
  print("\n")


  #3 Is A subset of B
  print("Number 3")
  print("Set A: ",A)
  print("Set B: ",B)
  new_set = A.copy()
  if new_set.issubset(B):
    print("A is a subset of B")
  elif B.issubset(new_set):
    print("B is a subset of A")
  else:
    print("No subset of each other")
  print("\n")

  #4 Are A and B disjoint sets
  print("Number 4")
  print("Set A: ",A)
  print("Set B: ",B)
  new_set = A.copy()
  if new_set.isdisjoint(B):
    print("A and B is disjoint")
  else:
    print("A and B is not disjoint")
  print("\n")

  #5 Join A with B and B with A
  print("Number 5")
  print("Set A: ",A)
  print("Set B: ",B)
  new_set = {}
  new_set = A.union(B)
  print("A joined with B: ",new_set)
  new_set = B.union(A)
  print("B joined with A: ",new_set)
  print("\n")

  #6 What is the symmetric difference between A and B 
  # It means that it returns a set that contains all items from both sets, 
  # except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
  print("Number 6")
  print("Set A: ",A)
  print("Set B: ",B)
  new_set = {}
  new_set = A.symmetric_difference(B)
  print("A symmetric difference: ",new_set)
  print("Bonus:difference of A and B ",A.difference(B))
  print("\n")
  print("The difference is an emppty set as A is contained within B")
  print("\n")
  # print("Number 2")
  # print("Set A: ",A)
  # print("Set B: ",B)
  # new_set = A.copy()
  # new_set.intersection(B)
  # print("A intersection B: ",new_set)
  # print("\n")
   
  #7 Delete the sets completely
  print("Number 7") 
  del A
  del B
  try:
    print(f"Set A: ,{A} - Set B: ,{B}")
  except NameError as e:
    print("Set does not exist")
    print(e)
  print("\n")

  # Exercises: Level 3
  # Convert the ages to a set and compare the length of the list and the set, which one is bigger?
  # Explain the difference between the following data types: string, list, tuple and set
  # I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.


  s = s0 + s3 + s0
  print(s)

  #Convert the ages to a set and compare the length of the list and the set, which one is bigger?
  # Explain the difference between the following data types: string, list, tuple and set
  # "I am a teacher and I love to inspire and teach people". How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
  print("Number 1")
  age_list = [22, 19, 24, 25, 26, 24, 25, 24]
  age_set = set(age_list) #should remove duplicates
  print(f"Age Set: {age_set} \nAge List: {age_list}")
  if len(age_list) < len(age_set):
    print("Set is bigger")
  elif len(age_list) > len(age_set):
    print("List is bigger")
  else:
    print("Equal lengths")

  print("\n")

  print("Number 2")
  print("List items are ordered, changeable, allow duplicates and use square brackets")
  print("Tuple items are ordered, unchangeable, allow duplicates and use round brackets")
  print("Sets are unordered,unindexed, unchangeable, do not allow duplicates and use curly braces")
  print("Dicts are ordered,indexed with key names, changeable, do not allow duplicates and use curly braces")
  print("\n")


  print("Number 3")
  s = "I am a teacher and I love to inspire and teach people"
  liststring = s.split()
  print(liststring)
  set_string = set(liststring)
  print(f"Unique words in the string: {len(set_string)}\nTotal words in the sentence: {len(liststring)}")
  print("\n")

if __name__ == "__main__":
  main()
