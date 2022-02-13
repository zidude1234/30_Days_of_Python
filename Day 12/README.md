#  💻 Lets Go!!🚀 🚀 🚀 

#  3️⃣0️⃣ Days of Python - Day Twelve

## 📚 Table of Contents
- [Objective](#objective)
  - [💻 Exercises - Day 12](#-exercises-day-12)
    - [Exercise: Level 1](#exercises-level-1)
    - [Exercise: Level 2](#exercises-level-2)
    - [Exercise: Level 3](#exercises-level-3)
- [Solution on Github](https://github.com/zidude1234/30_Days_of_Python/blob/main/Day%2012/Python%20Syntax/Day12%20Syntax.py)

## Objective
This repository contains the solution for the Day Twelve of the "30 Days of Python Challenge"!
Thanks @Asabaneh for the excellent Python Content! 👋🏻

## 💻 Exercises: Day 12

### Exercises: Level 1

1. Writ a function which generates a six digit/character random_user_id.
   ```py
     print(random_user_id());
     '1ee33d'
   ```
2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
   
```py
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
   
```py
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
```

### Exercises: Level 2

1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
1. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
1. Write a function generate_colors which can generate any number of hexa or rgb colors.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```

### Exercises: Level 3

1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


 [<< Day 11](../Day%2011/README.md) | [Day 123 >>](../Day%2013/README.md)


--#### [Go to Top of Page](#objective)
