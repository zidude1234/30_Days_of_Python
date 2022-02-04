#Day Three of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 03 Feb 2022
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

def main():

    os.system("cls") # clear console

    #1
    myage = 21

    #2
    myheight = 2.15

    #3
    mycomplex = 4 + 7j

    #4
    print("Number 4")
    tri_base = int(input("Enter the base:\n"))
    tri_height = int(input("Enter the height:\n"))
    tri_area = tri_base * tri_height/2
    print("The area of the triangle is ",int(tri_area))
    print("\n")

    #5
    print("Number 5")
    tri_side_a = int(input("Enter side a:\n"))
    tri_side_b = int(input("Enter side b:\n"))
    tri_side_c = int(input("Enter side c:\n"))
    tri_peri = tri_side_a + tri_side_b + tri_side_c
    print("The perimeter of the triangle is ",int(tri_peri))
    print("\n")


    #6
    print("Number 6")
    rect_len = int(input("Enter the rectangle length:\n"))
    rect_width = int(input("Enter the rectangle width:\n"))
    rect_area = rect_len * rect_width
    print("The area of the rectangle is ",int(rect_area))

    rect_peri = (rect_len + rect_width) *2
    print("The perimeter of the rectangle is ",int(rect_peri))
    print("\n")

    #7
    print("Number 7")
    circ_radius = int(input("Enter the radius of the circle:\n"))
    circ_area = math.pi * circ_radius **2 
    circ_peri = math.pi * circ_radius * 2 
    print("The area of the circle is " + "{:.2f}".format(circ_area))
    print("The circumference of the circle is " + "{:.2f}".format(circ_peri))
    print("\n")

    #8
    print("Number 8")
    print("For the line equation y = 2x - 2") 
    slope8 = 2
    y = 0
    x_int8 = (y + 2)/2

    x = 0
    y_int8 = 2*x -2
    print("The slope of the equation ",slope8)
    print("X intercept ",x_int8)
    print("Y intercept ",y_int8)
    print("\n")

    #9
    print("Number 9")
    myString1 = "The Slope of points{} and {} equals {}"
    myString2 = "The Euclidian distance between points{} and {} equals {}"

    point1 = (2, 2)
    point2 = (6, 10)
    slope_9 = (point2[1]-point1[1]) /(point2[0]-point1[0])
    euclid_dist = ((math.pow(point2[1]-point1[1],2) + math.pow(point2[0]-point1[0],2))**0.5)
    print(myString1.format(point1,point2,"{:.2f}".format(slope_9)))
    print(myString2.format(point1,point2,"{:.2f}".format(euclid_dist)))
    print("\n")

   

    #10
    print("Number 10")
    if slope8 == slope_9:
      print("The slopes are equal")  
    else:
      print("The slopes are unequal") 
    print("\n")
    #11
    print("Number 11")
    check_key = 1
    try:
      x_value = int(input("Enter x value for the quadratic equation (y = x^2 + 6x + 9)\n"))
    except:
      print("Enter a valid integer")
      x_value = int(input("Enter x value for the quadratic equation (y = x^2 + 6x + 9)\n"))
    y_value = x_value **2 + 6*x_value + 9
    print ("The value of y is ",y_value)
    print("The next step is to iterate to find the x value where y value is zero") 
    while (check_key == 1):
      x_value = int(input("Enter x value for the quadratic equation (y = x^2 + 6x + 9)\n"))
      y_value = x_value **2 + 6*x_value + 9
      if (y_value == 0):
        check_key = 0
        print("The value at which y is zero is", x_value)
      else:
        print ("The value of y is " + str(y_value) + ", this is not equal to zero")
    print("\n")
    #12
    print("Number 12")
    str1, str2 = 'python','dragon'
    if len(str1)==len(str2):
      print(len(str1)==len(str2))
    else:
      print(len(str1)==len(str2))
    #13
    print("Number 13")
    x = re.search("on", str1)
    y = re.search("on", str2)
    if x and y:
      print("\"on\" appears in both " + str1 + " and " + str2)
    print("\n")
    #14
    print("Number 14")
    str4 = 'I hope this course is not full of jargon'
    if 'jargon' in str4:
          print("'jargon' found in \"" + str4 + "\"")
    else:
          print("jargon not found in \"" + str4 + "\"")
    print("\n")
    #15
    print("Number 15")
    if 'on' in str1 and 'on' in str2:
          print("'on' found in \"" + str1 + " and " + str2)
    else:
          print("'on' not found in \"" + str1 + " and " + str2)
    print("\n")
    #16
    print("Number 16")
    print("length of '"+ str1 + "' is:", len(str1))
    print("In float length of '"+ str1 + "' is:", float(len(str1)))
    print("In string length of '"+ str1 + "' is:", str(float(len(str1))))
    print("\n")
    #17
    print("Number 17")
    for i in range (1,11):
      result = ' is even' if i % 2 == 0 else ' is odd'
      #print(str(i) + result) - append strings
      print(f"{i} {result}") #- formatted string literals
    
    #18
    print("Number 18")
    #Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
    if (7//3 == int(2.7)):
      print('floor division of 7 by 3 is equal to the int converted value of 2.7')
    else:
      print("not equal")
    print('\n')

    #19
    print("Number 19")
    #Check if type of '10' is equal to type of 10
    if (type('10') == type(10)):
      print('Types "10" and 10 are equal')
    else:
      print('Types "10" and 10 are not equal')
    print('\n')

    #20
    print("Number 20")
    #Check if int('9.8') is equal to 10
    #this will throw an error as floating strings cannot be cast into integer
    #int("9") will work
    try:
      x = int('9.8') 
      if x == 10:
        print(f"{int('9.8')} is equal to {10}")
    except ValueError as e:
        print("Decimal strings cannot be made into int")
        print("\'int('9.8')\' is not equal to {10}")
    except:
        print("\'int('9.8')\' is not equal to {10}")
    print('\n')
    
    
    
    
if __name__ == "__main__":
  main()
