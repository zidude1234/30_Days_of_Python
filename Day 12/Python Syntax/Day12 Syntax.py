#Day Twelve of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 12 Feb 2022
# IDE: VSCode

from Day12_modules import *

def main():

  s1 = 'Day 12 Exercise level 1'
  s2 = 'Day 12 Exercise level 2'
  s3 = 'Day 12 Exercise level 3'
  s0 =  ''

  for i in range(20):
    s0 += "--"

  s = s0 + s1 + s0
  print(s)
  os.system("cls") # clear console

  print("Bonus - Secrets hex:", secrets.token_hex(3))  #for passwords

  #1 Write a function which generates a six digit/character random_user_id.
  #   print(random_user_id());
  #   '1ee33d'
  
  # print(string.ascii_letters) # alphanumerics
  # print(string.digits)        # digits

  print("Number 1")
  print(random_user_id())
  print("\n")
  
  #2 Modify the previous task. Declare a function named user_id_gen_by_user. 
  # It doesn’t take any parameters but it takes two inputs using input(). 
  # One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

  print("Number 2")
  print(user_id_gen(5,5))
  #To get multi input use split()
  str_input = input("Enter the number of characters and number of IDs required seperated, -by a space or hyphen:\n")
  #split using white space
  a, b,*rest = [i for i in re.split(" |:|-\n",str_input)] 
  num_char, num_of_id = int(a), int(b)
  print('#output')
  print(user_id_gen(num_char, num_of_id))

  print("Number 3")
  print(rgb_color_gen())
  print('\n')

  #2 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
  # Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

  s = s0 + s2 + s0
  print(s) 
  
  print("Number 1")
  print(list_of_hexa_colors())
  print('\n')
  
  print("Number 2")
  print(generate_colors('hexa', 3))
  print(generate_colors('hexa', 1))
  print(generate_colors('rgb', 3))
  print(generate_colors('rgb', 1))
  print(generate_colors())
  print(generate_colors('rgb'))
  print('\n')  

  s = s0 + s3 + s0
  print(s)  
  # Exercises: Level 3
  # 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
  list1 = ['banana', 'cherry', 'apple']
  list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]

  print(shuffle_list(list1))
  print(shuffle_list(list2))
  
  # 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
  list3 = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(shuffle_list_9to7(list3))

      
   
if __name__ == "__main__":
  main()
