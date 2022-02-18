#Day Fourteen of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 15 Feb 2022
# IDE: VSCode

# import the "sys" module
from ast import Num
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math
import re
from functools import reduce
import countries_data
import string
import string
import json
from collections import Counter

def main():

  os.system("cls") # clear console
  print("Higher Order Functions")
  def sum_numbers(nums):  # normal function
     return sum(nums)    # a sad function abusing the built-in sum function :<

  def higher_order_function(f, lst):  # function as a parameter
     summation = f(lst)
     return summation
  result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])

  print(result)       # 15
  print('\n')

 #normal greeting function

  def greeting():
    return 'Welcome to Python'
  def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
  g = uppercase_decorator(greeting)
  print("W1", g())          # WELCOME TO PYTHON
  
## Let us implement the example above with a decorator

#'''This decorator function is a higher order function
#that takes a function as a parameter'''
  def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
  @uppercase_decorator    #the key line

  def greeting2():
    return 'Welcome to Python'

  print("W2",greeting2())   # WELCOME TO PYTHON


# First Decorator
  def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
  def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

  @split_string_decorator
  @uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
  def greeting3():
    return 'Welcome to Python'
  print("W3",greeting3())   # WELCOME - TO -  PYTHON

  countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
  names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  def bannergreeting(day_name,exercise_name):
    daybanner = f'Exercise {day_name} '
    exercisebanner = f'Level {exercise_name} '
    front_end = f'--' * 20
    return combinebanners(front_end,daybanner,exercisebanner)
  
  

  def combinebanners(s0,s1,s2):
    return s0 + s1 + s2 + s0
  
  # A1 Define two function to make the banner

  # banner = bannergreeting(14,1)
  # print(banner)

  banner = bannergreeting
  print(banner(14,1))

  def p(num):
    print(f"Number {num}")
  
  def pn():
    print(f"\n")
  

  def countStartLetters():
    tuple_list,num = [],[]
    for letterAlpha in string.ascii_uppercase: #"[^0-9a-zA-Z]+
      count_letters, a = 0 , []
      for countrydata in countries_data.countries_data: 
        if re.search("^" + letterAlpha ,countrydata["name"]):
          count_letters +=1    
      tuple_list.append(tuple((letterAlpha,count_letters)))
      num.append(count_letters)
    print(tuple_list)
    print(num)
    

  def getcountries():
    countiri=[]
    for countrydata in countries_data.countries_data:
      countiri.append(countrydata["name"])
    return countiri
 

  
  countStartLetters()
  print(len(countries_data.countries_data))
  pn()
  countiri = getcountries()
  for i in countiri:
    print(f'{str(countiri.index(i)+1).zfill(5)}|{i}|')
  
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
  
  
  def get_string_lists(list1):
      i = list(map(lambda x:x.split(),list1))
      returnlist = [e for element in i for e in element]
      return returnlist
   
  def join_two_strings( a , b):
    return a + ', ' + b
  
  
  def categorize_countries(searchlist):
    for searchitem in searchlist:
      print(f'{searchitem}: ', end='')
      a = []
      for countrydata in countries_data.countries_data:
        if re.search(searchitem +"$",countrydata["name"]):
          a.append(countrydata["name"])
      print(a)
  pn()
  
  def sort_countries_name_capital(list_original):
    return sorted(list_original, key = lambda k: (k['name'],k['capital']))


  def sort_countries_popl(list1):
    countiri_sort_NC = []
    return sorted(list1,key=lambda k: (k['population']), reverse=True)
  
  
  
  
  
  def switch_dict_keys(list1):  #expand and switch dict keys
    res = {}
    for _lang, _country in list1:
      res.setdefault(_lang, []).append(_country)
    return res

  def sort_count_lang():
    def wrapper():
        list1 = countries_data.countries_data #1
        func  = extract_countries_lang(list1) #2
        func2,func2_tp = expand_dict_to_tuple(func)    #3A
        dict_func = switch_dict_keys(func2_tp)        #3B
        func3 = count_countries_lang(func2)   #4
        return func3
    return wrapper
  
  def extract_countries_lang(list1): #a list of dict items
    countiri_name_lang = []
    keys_shortlist = ['name', 'languages'] #reduce list to country and language only
    for dict_items in list1:
      dict_temporary = {x : dict_items[x] for x in keys_shortlist}
      countiri_name_lang.append(dict_temporary)
    print("Reduced Dict:", countiri_name_lang)
    pn
    return countiri_name_lang

  
  def expand_dict_to_tuple(list1):  #expand dict to become keys and value tuples
    countiri_expanded_lang, lang_list= [],[]
    for dict_object in list1:
        name_element = dict_object["name"]
        country_lang_tuple = ()
        if isinstance(dict_object['languages'],list):
            for value_element in dict_object['languages']:
                 v = ''
                 v = value_element
                 country_lang_tuple= (tuple((v,name_element)))
                 countiri_expanded_lang.append(country_lang_tuple)
        else:
            country_lang_tuple = (tuple((dict_object['languages'],name_element)))
            countiri_expanded_lang.append(country_lang_tuple)
    for i in countiri_expanded_lang:
        lang_list.append(i[0])
    return lang_list,countiri_expanded_lang

  def count_countries_lang(lang_list1):
    collector_lang = Counter(lang_list1)
    print(collector_lang)
    lang_count = collector_lang
  
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
  #i = [i.upper() for i in countries]
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
  i = filter(lambda x:len(x)>=6 ,countries)
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
  list2 = ["The cow jumped over the moon","The cat said hello"]
  p(9)

  i = map(lambda x:x.split(),list1)#[['The', 'cow', 'jumped', 'over', 'the', 'moon']]
  i2 = map(lambda x:x.split(),list2)#[['The', 'cow', 'jumped', 'over', 'the', 'moon'], ['The', 'cat', 'said', 'hello']

  i3 = map(lambda x:list(x.split()),list1) #[['The', 'cow', 'jumped', 'over', 'the', 'moon']] - same as above
  i4 = map(lambda x:list(x.split()),list2) #[['The', 'cow', 'jumped', 'over', 'the', 'moon'], ['The', 'cat', 'said', 'hello']]
 
  print(get_string_lists(list1)) #['The', 'cow', 'jumped', 'over', 'the', 'moon']
  print(get_string_lists(list2)) #['The', 'cow', 'jumped', 'over', 'the', 'moon','The', 'cat', 'said', 'hello']
  pn() 


  #10 Use reduce to sum all the numbers in the numbers list.
  p(10)
  def add_two_numbers( x , y):
    return x + y

  i = reduce(add_two_numbers,numbers) #using functions
  print("using functions", i)

  i2 = reduce(lambda x,y:x + y,numbers) #using lambda
  print("using lambda", i2)

  #11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

  p(11)
  i = reduce(join_two_strings,countries[0:(len(countries)-1)]) #using functions
  print(f"using functions: {i}, and {countries[len(countries)-1]} are north European countries")

  i2 = reduce(lambda x,y:x +", " + y,countries[0:(len(countries)-1)]) #using lambda
  print(f"using lambda: {i2}, and {countries[len(countries)-1]} are north European countries")
  
  #12  Declare a function called categorize_countries that returns a list of countries with some common pattern 
  
  searchlist = ["land","island","stan","ia"] #Ends with the suffix
  categorize_countries(searchlist)
  
  #13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
  p(13)
  
  
  # 14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
  p(14)
  print(get_first_ten_countries())
  # Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
  p(15)
  print(get_last_ten_countries())

  print(banner(14,3))
  #1. Sort countries by name, by capital, by population
  #this will be using the sorted method with keys used
  
  p(1)
  print("Sorting Countries on Name, Capital and Population")
  sorted_name_cap_pop = sort_countries_name_capital(countries_data.countries_data)
  for dict in sorted_name_cap_pop[0:50]:
    print(f'{dict},') 



  p(3)
  print("Sorting Countries on Population")
  sorted_popl = sort_countries_popl(countries_data.countries_data)
  for dict in sorted_popl[0:10]:
    print(dict) 








if __name__ == "__main__":
  main()
