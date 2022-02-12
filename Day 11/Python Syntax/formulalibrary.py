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

def slope(x_coeff,intercept):
    if intercept <0:
        return(f'The slope of the equation y={x_coeff:-}x - {abs(intercept)} is {x_coeff}')
    elif intercept >0:
        return(f'The slope of the equation y={x_coeff:-}x + {intercept} is {x_coeff}')
    else:
        return(f'The slope of the equation y={x_coeff:-}x is {x_coeff}"')
   
def solve_quadratic_eqn(a_coeff,b_coeff,y_intercept):
    quotient = b_coeff **2 - 4 * a_coeff * y_intercept
    
    b_output = ' + ' + str(b_coeff) if(b_coeff > 0) else '- ' + str(abs(b_coeff))
    c_output = ' + ' + str(y_intercept) if(y_intercept > 0) else '- ' + str(abs(y_intercept))
    if quotient < 0:
        return(f'''Complex roots of {a_coeff:-}x\N{SUPERSCRIPT TWO}{b_output}x {c_output} are:        
        x\N{SUBSCRIPT ONE} =  {(-b_coeff+cmath.sqrt(quotient))/(2 * a_coeff) } 
        x\N{SUBSCRIPT TWO} = {(-b_coeff - cmath.sqrt(quotient))/(2 * a_coeff)}''')
    elif(quotient > 0):
        return(f'''Roots of {a_coeff:-}x\N{SUPERSCRIPT TWO}{b_output}x {c_output} are:        
        x\N{SUBSCRIPT ONE} = {(-b_coeff+math.sqrt(quotient))/(2 * a_coeff) } 
        x\N{SUBSCRIPT TWO} = {(-b_coeff - math.sqrt(quotient))/(2 * a_coeff)}''')
    else:
        return(f'''Roots of {a_coeff:-}x\N{SUPERSCRIPT TWO}{b_output}x {c_output} are:        
        x\N{SUBSCRIPT ONE} and x\N{SUBSCRIPT TWO} equals {(-b_coeff+math.sqrt(quotient))/(2 * a_coeff) } 
        ''')


def print_list(list_to_print):
    for ind_ex, list_item in enumerate(list_to_print):
        print(f'Item {ind_ex + 1}: {list_item}')

def reverse_list(list_to_reverse):
    reversedlist = []
    for i in range(len(list_to_reverse)):
        reversedlist.append(list_to_reverse[-(i+1)])
    return(f'The reverse of the list {list_to_reverse} is {reversedlist}"')

def capitalize_list_items(list_to_capitalise):
    capitaliseddlist = []
    for i in list_to_capitalise:
        i_splitted = i.split()
        if len(i_splitted) > 1:
            s = ''
            temp_list = []
            for k in i_splitted:
                s += k.capitalize() + ' '
            #temp_list.append(s)
            capitaliseddlist.append(s.strip())
        else:
            capitaliseddlist.append(i.capitalize())
    return(f'The capitalised form of the list {list_to_capitalise} is {capitaliseddlist}')

