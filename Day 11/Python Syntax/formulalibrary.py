# Module to support the Day Eleven Challenge
# import the "sys" module
import math

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius, dimension):
    return (f'The area of a circle with radius {radius} {dimension} is {(math.pi * (radius ** 2)):.2f} {dimension}\N{SUPERSCRIPT TWO}') 

def add_all_nums(*args):
    templist = args
    sumx = 0
    if len(templist) == 1:
        sumtp = check_list(templist)
        for num in sumtp:
            sumx += num
        return (f'The sum of numbers {templist[0]} is {sumx}')
    else:
        for num in args:
            if type(num) != int:
                num = 0
            sumx += num
        return (f'The sum of numbers {args} is {sumx}') 

def check_list(args):
    templist = args
    revised_list = []
    #print("temp",templist) - the arguments are inserted as a tuple with length of 1
    for i in templist[0]:
        if type(i) == int:
            revised_list.append(i)
        else:
            print(f'In this list "{i}" is not a valid number. replaced with zero')
            revised_list.append(0)
    return tuple(revised_list)

def convert_celsius_to_fahrenheit(celsius):
    if type(celsius) == int or type(celsius) == float:
        fahr = (9 / 5 * celsius + 32)
        if fahr.is_integer():
            return (f'The temperature of {celsius} \N{DEGREE CELSIUS}  is {int(fahr):,} \u2109')
        else:
            return (f'The temperature of {celsius} \N{DEGREE CELSIUS}  is {fahr:,.2f} \u2109')
    else:
        return (f'invalid argument')



def check_season(* args):
    tp_response = ()
    tp_response = args
    templist = []
    print(args)
    for month in tp_response:
        if month in ('September', 'October','November'):
            print(f'The month of {month} is "Autumn"')
        elif month in ('December','January','February'):
            print(f'The month of {month} is "Winter"',end='')
        elif month in (f'March', 'April','May'):
            print(f'The month of {month} is "Spring"',end='')
        elif month in ('June', 'July', 'August'):
            print(f'The month of {month} is "Summer"')
        else:
            print(f'The month of {month} does not exist!')
        print('')
    return ""

