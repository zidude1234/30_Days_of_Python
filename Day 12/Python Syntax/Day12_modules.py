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

  
