#Day Six of the 30 Day Challenge
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
from math import ceil

def main():

    os.system("cls") # clear console

    s1 = 'Exercise level 1'
    s2 = 'Exercise level 2'
    s0 =  ''

    for i in range(20):
      s0 += "@:"

    s = s0 + s1 + s0
    print(s)

    #1 Create an empty tuple
    mytuple = () 
    print("Number 1")
    print("Empty Tuple: ", mytuple)
   
    tuple2 = tuple()
    print("Empty Tuple: ", tuple2)
    print("\n")

    #2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
    print("Number 2")
    mytuple_bro = ("Luke Skywalker","Obi-Wan Kenobi","Mace Windu")
    mytuple_sis = ("Ahsoka Tahno","Leia Organa","Padme Amidala")
    print("Tuple - Brothers:", mytuple_bro)
    print("Tuple - Sisters:", mytuple_sis)
    print("\n")

    #3 Join brothers and sisters tuples and assign it to siblings
    print("Number 3")
    mytuple_siblings = mytuple_bro + mytuple_sis
    print("Tuple - Siblings:", mytuple_siblings)
    
    #method 2
    list_mytuple_siblings = list(mytuple_bro)
    list_mytuple_siblings.extend(mytuple_sis)
    print("Method 2- Using List to modify tuples workaround: ",tuple(list_mytuple_siblings))
    print("\n")

    #4 How many siblings do you have?
    print("Number 4")
    print("Number of Siblings:", len(mytuple_siblings))
    print("\n")

    #5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
    # Tuples cannot be modified
    print("Number 5")
    list_mytuple_family = list_mytuple_siblings.copy() #duplicate the old sibling list
    my_tuple_parents = tuple(("Master Yoda","Emperor Palpatine"))
    list_mytuple_family.extend(my_tuple_parents)
    print("Family Tuple: ",tuple(list_mytuple_family))
    print("\n")
    

    s = s0 + s2 + s0
    print(s)

    #1 Unpack siblings  and parents from family_members 
    print("Number 1")
    siblings, parents = list_mytuple_family[0:-2],list_mytuple_family[-2:]
    print(siblings)
    print(parents)
    print("\n")

    #2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp. 
    print("Number 2")
    fruits = ('banana', 'orange', 'mango', 'lemon')
    vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
    animal_products = ('fat', 'meat', 'milk','eggs')

    food_stuff_tp = fruits + vegetables + animal_products 
    print("Tuple 1: ",fruits)
    print("Tuple 2: ",vegetables)
    print("Tuple 3: ",animal_products)
    print("Combined Foodstuff Tuples: ",food_stuff_tp)
    print("\n")

    #3 Change the about food_stuff_tp tuple to a food_stuff_lt list 
    print("Number 3")
    food_stuff_lt = list(food_stuff_tp) 
    print("Combined Foodstuff Lists: ",food_stuff_lt)
    print("\n")

    #4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list. 
    print("Number 4")
    length_list = len(food_stuff_tp)
    if length_list % 2 == 1:
      startindex = ceil(length_list/2)-1
      endindex = startindex + 1
    else:
      startindex = ceil(length_list/2)-1
      endindex = startindex + 2 #endindex is not included
    print("List:",food_stuff_tp)
    print("Length:",len(food_stuff_tp))
    print("Middle Food Tuple:",food_stuff_tp[startindex:endindex])
    slicelist = list(food_stuff_tp)
    del slicelist[startindex:endindex]
    print("Sliced out Items: ",tuple(slicelist))
    print("\n")


    #5 Slice out the first three items and the last three items from food_staff_lt list
    print("Number 5")
    slicelist = list(food_stuff_tp)
    del slicelist[0:3]
    print("Foodstuff Tuples: ",food_stuff_tp)
    print("With First 3 out:",tuple(slicelist))
    print("\n")
    slicelist = list(food_stuff_tp)
    del slicelist[-3:]
    print("With Last  3 out:",tuple(slicelist))
    print("\n")

    #6 Delete the food_staff_tp tuple completely
    print("Number 6")
    del food_stuff_tp
    try: 
      print("Tuple with all items destroyed:",food_stuff_tp)
    except NameError as e:
      print("Tuple does not exist!")
      print (e)
    except:
      print("There is an error!")
    print("\n")

    #7 Check if an item exists in tuple:
    print("Number 7")
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    country = 'Estonia'
    if country in nordic_countries:
      print(f'Yes, {country} exists in {nordic_countries}')
    else:
      print(f'No, {country} does not exists in {nordic_countries}')
    country = 'Iceland'
    if country in nordic_countries:
      print(f'Yes, {country} exists in {nordic_countries}')
    else:
      print(f'No, {country} does not exists in {nordic_countries}')
    print("\n")


if __name__ == "__main__":
  main()
