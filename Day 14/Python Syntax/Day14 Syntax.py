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
from functools import reduce

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
  
  def get_string_lists(list1):
      i = list(map(lambda x:x.split(),list1))
      returnlist = [e for element in i for e in element]
      return returnlist

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
  
  # 7 Use filter to filter out countries starting with an 'E'
  p(7)
  i = filter(lambda x:x.startswith('E') ,countries)
  print(list(i))
  pn() 
  
  #8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))


     
  #9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
  list1 = ["The cow jumped over the moon"]
  p(9)
  print(get_string_lists(list1))
  pn() 
  
  #10 Use reduce to sum all the numbers in the numbers list.
  p(10)
  def add_two_numbers( x , y):
    return x + y
  
  i = reduce(add_two_numbers,numbers)
  print(i)
  
  #11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
  def join_two_strings( a , b):
    return a + ', ' + b
  p(11)
  i = reduce(join_two_strings,countries[0:(len(countries)-1)]) #using functions
  print(f"using functions: {i}, and {countries[len(countries)-1]} are north European countries")


  #12  Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
  p(12)
  def categorize_countries(searchlist):
    for searchitem in searchlist:
      print(f'{searchitem}: ', end='')
      a = []
      for countrydata in countries_data.countries_data:
        if re.search(searchitem +"$",countrydata["name"]):
          a.append(countrydata["name"])
      print(a)
  pn()

  #13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
  p(13)
  def countStartLetters():
    tuple_list,num = [],[]
    for letterAlpha in string.ascii_uppercase: 
      count_letters, a = 0 , []
      for countrydata in countries_data.countries_data: 
        if re.search("^" + letterAlpha ,countrydata["name"]):
          count_letters +=1    
      tuple_list.append(tuple((letterAlpha,count_letters)))
    print(tuple_list)

    def get_first_ten_countries():
    countiri_first10 = []
    for countrydata in countries_data.countries_data[0:10]:
          countiri_first10.append(countrydata)
    return countiri_first10
 
   def get_last_ten_countries():
    countiri_last10 = []
    for countrydata in countries_data.countries_data[-10:]:
          countiri_last10.append(countrydata)
    return countiri_last10
  
  # 14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
  p(14)
  print(get_first_ten_countries())
  # Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
  p(15)
  print(get_last_ten_countries())



    
    
if __name__ == "__main__":
  main()
