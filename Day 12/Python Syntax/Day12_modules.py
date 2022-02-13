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

def rgb_color_gen():  
  color_rgb,a = (),[]
  for i in range(0,3):
    a.append(random.randint(0,255))
  color_rgb = tuple(a)
  return f'rgb{color_rgb}'

def list_of_hexa_colors():  
  hex_number = '#'
  for i in range(3):
    hex_number += hex(random.randint(0,255)).replace('0x','')
    #hex_number += str(re.split('0x',hex(random.randint(0,256))))
  return hex_number

def generate_colors(mode_color = 'hexa', num_color = 3): #default 
  color_range=[]
  if mode_color == 'hexa':
    for i in range(num_color):
      color_range.append(list_of_hexa_colors())
  else:
    for i in range(num_color):
      color_range.append(rgb_color_gen())    
  return color_range

def shuffle_list(list1):
  set_to_return = len(list1)
  return random.sample(list1,k = set_to_return)

def shuffle_list_9to7(list1):
  keyreturn = 7
  return random.sample(list1,k = 7)

