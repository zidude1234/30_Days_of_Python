# Modules supporting the Day 12 Syntax

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
import random
import secrets
import string


pool_of_xters = string.ascii_letters + string.digits
def random_user_id():
  user_id = ''
  for i in range(6):
    user_id += random.choice(pool_of_xters)
  return user_id
  
def user_id_gen(num_of_xters,num_of_IDs):
  s = ''
  for i in range(num_of_IDs):
    for i in range(num_of_xters):
      s += random.choice(pool_of_xters)
    s +='\n'
  return s

  # Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
  # print(user_id_gen_by_user()) # user input: 5 5
  # #output:
  # #kcsy2
  # #SMFYb
  # #bWmeq
  # #ZXOYh
  # #2Rgxf
    
  # print(user_id_gen_by_user()) # 16 5
  # #1GCSgPLMaBAVQZ26
  # #YD7eFwNQKNs7qXaT
  # #ycArC5yrRupyG00S
  # #UbGxOFI7UXSWAyKN
  # #dIV0SSUTgAdKwStr
  # Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
  # print(rgb_color_gen())
  # # rgb(125,244,255) - the output should be in this form
  # Exercises: Level 2
  # Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
  # Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
  # Write a function generate_colors which can generate any number of hexa or rgb colors.
  #    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
  #    generate_colors('hexa', 1) # ['#b334ef']
  #    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
  #    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
  # Exercises: Level 3
  # Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
  # Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.