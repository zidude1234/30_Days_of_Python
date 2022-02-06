#Day Five of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 05 Feb 2022
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
  listOne = []
  print("Number 1")
  print(listOne)
  print('\n')
  
  #2
  listOne = ["Name","Age",3,465,"Country","City","Asabeneh",250,["Halo","Mario Bros", "Street Fighter"], ('Coding', 'For' , 'All')]
  print("Number 2")
  print(listOne)
  print('\n')

  #3 Find the length of your list
  print("Number 3")
  print(f'listOne Length :{len(listOne)}')
  print('\n')
  
  #4 Get the first item, the middle item and the last item of the list
  print("Number 4")
  print(f'first item :{listOne[0]}')
  print(f'last item :{listOne[len(listOne)-1]}')
  middle_item = listOne[ceil(len(listOne)/2)]
  print(f'Middle item with index ({listOne.index(middle_item)}) : {listOne[ceil(len(listOne)/2)]}')
  print('\n')
  
  #5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
  mixed_data_types = list(("dataBio",99,"3.2m","Complicated","50 Git Street"))
  print("Number 5")
  print(mixed_data_types)
  print('\n')


  #6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
  it_companies = list(("Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"))
  print("Number 6")
  print("List Declared")
  print('\n')

  #7 Print this list
  print("Number 7")
  print(it_companies)
  print('\n')

  #8 Print the number of companies in the list
  print("Number 8")
  for item_i in it_companies:
    print(f'\tCompany {(it_companies.index(item_i))+1}: {item_i}')
  print('\n')

  #9 Print the first, middle and last company
  print("Number 9")
  print(f'first company :{it_companies[0]}')
  print(f'middle company :{it_companies[3]}')
  print(f'last company :{it_companies[len(it_companies)-1]}')
  print('\n')

  #10 Print the list after modifying one of the companies
  it_companies [0] = "Metaverse"
  print("New List:", it_companies)
  
  #11 Add an IT company to it_companies
  print("Number 11")
  it_companies.append("Dell")
  print("Updated List:",it_companies)
  print('\n')

  #12 Insert an IT company in the middle of the companies list
  print("Number 12")
  middleindex = ceil((len(it_companies)/2))
  it_companies.insert(middleindex,"HP")
  print("Updated List:", it_companies)
  print('\n')

  #13 Change one of the it_companies names to uppercase (IBM excluded!)
  it_companies2 = []
  print("Number 13")
  for i in it_companies:
    it_companies2.append(i.upper())
  print("Uppercase List:", it_companies2)
  print('\n')

  #14 Join the it_companies with a string '#;
  print("Number 14")
  it_companies = ['Metaverse', 'Google', 'Microsoft', 'Apple', 'HP', 'IBM', 'Oracle', 'Amazon', 'Dell'] 
  it_companies = it_companies + ["#;"]
  print("Itcompanies:", it_companies)
  print('\n')

  #15 Check if a certain company exists in the it_companies list. - HP
  print("Number 15")
  print("HP item is at index: ",it_companies.index("HP"))
  print('\n')


  #16 Sort the list using sort() method
  sortorder = []
  print("Number 16")
  print("Unsorted:",it_companies)
  it_companies.sort()
  print("Sorted:",it_companies)

  #17 Reverse the list in descending order using reverse() method
  print("Number 17")
  it_companies = ['Metaverse', 'Google', 'Microsoft', 'Apple', 'HP', 'IBM', 'Oracle', 'Amazon', 'Dell', '#;']
  print("Unsorted:",it_companies)
  it_companies.sort(reverse=True)
  print("Reverse Sorted:",it_companies)
  print('\n')
  
  #18 Slice out the first 3 companies from the list
  print("Number 18")
  it_companies = ['Metaverse', 'Google', 'Microsoft', 'Apple', 'HP', 'IBM', 'Oracle', 'Amazon', 'Dell', '#;']
  slicelist = it_companies[0:3:]
  print("Slice:",slicelist)
  print('\n')
  
  #19 Slice out the last 3 companies from the list
  print("Number 18")
  slicelist = it_companies[-3::]
  print("Slice:",slicelist)
  print('\n')

  #20 Slice out the middle IT company or companies from the list
  print("Number 20")
  length_list = len(it_companies)
  if length_list % 2 == 1:
    startindex = ceil(length_list/2)-1
    endindex = startindex + 1
  else:
    startindex = ceil(length_list/2)-1
    endindex = startindex + 2
  print("List:",it_companies)
  print("Middle Company(s):",it_companies[startindex:endindex])
  print('\n')

  #21 Remove the first IT company from the list
  modifiedlist = it_companies.copy()
  print("Number 21")
  modifiedlist.pop(0)
  print("Original List:",it_companies)
  print(modifiedlist)
  print('\n')
  
  #22 Remove the middle IT company or companies from the list
  modifiedlist = []
  modifiedlist = it_companies.copy()
  length_list = len(it_companies)
  print("Number 22")
  print("Original List:",it_companies)
  if length_list % 2 == 1:
    startindex = ceil(length_list/2)-1
    modifiedlist.pop(startindex)
    print("Odd list with middle removed:",modifiedlist)
  else:
    startindex = ceil(length_list/2)-1
    endindex = startindex + 2 #endindex is not included
    del modifiedlist[startindex:endindex]
    print("Even list with middle removed:",modifiedlist)
  print('\n')

  #23 Remove the last IT company from the list
  print("Number 23")
  modifiedlist = []
  modifiedlist = it_companies.copy()
  print("Original List:",it_companies)
  modifiedlist.pop()
  print("List with last item removed:",modifiedlist)
  print('\n')


  #24 Remove all IT companies from the list
  print("Number 24")
  modifiedlist = []
  modifiedlist = it_companies.copy()
  del modifiedlist[0:len(it_companies)]
  print("Original List:",it_companies)

  #25 Destroy the IT companies list
  print("Number 25")
  modifiedlist = []
  modifiedlist = it_companies.copy()
  del modifiedlist
  print("Original List:",it_companies)
  try: 
    print("List with all items destroyed:",modifiedlist)
  except NameError as e:
    print("List does not exist!")
    print (e)
  except:
    print("There is an error!")
  print('\n')
  print("List with all items removed:",modifiedlist)

  #26 Join the following lists:
  # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
  # back_end = ['Node','Express', 'MongoDB']
  print("Number 26")
  front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
  back_end = ['Node','Express', 'MongoDB']
  print("Front End",front_end)
  print("Back End",back_end)
  front_end.extend(back_end)
  print("Front End Extended",front_end)
  print('\n')

  #27 After joining the lists in question 26. 
  # Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
  print("Number 27")
  full_stack = front_end.copy()
  print(f"Original Full Stack: {full_stack}")
  index_insert = full_stack.index("Redux") + 1
  full_stack.insert(index_insert,"Python")
  index_insert += 1
  full_stack.insert(index_insert,"SQL")
  print(f"Final Full Stack: {full_stack}")
  print('\n')

  print("Number 1")
  ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
  print(f"Original Age List : {ages}")
  modifiedlist = []
  modifiedlist = ages.copy()
  modifiedlist.sort()
  print(f"a1. Sorted Full Stack: {modifiedlist}")
  print(f"a2. Max value - Full Stack: {max(modifiedlist)}")
  print(f"a3. Min value - Full Stack: {min(modifiedlist)}")
  list_of_minmax = list((min(modifiedlist),max(modifiedlist)))
  modifiedlist.extend(list_of_minmax)
  print(f"b. With Min and Max ages added: {modifiedlist}")
  length_list = len(modifiedlist)
  if length_list % 2 == 1:
    median_index = ceil(length_list/2)-1
    print(f"c. Median age: {modifiedlist[median_index]}")
  else:
    median_index = ceil(length_list/2)-1
    print(f"c. Median age: {(modifiedlist[median_index]+modifiedlist[median_index+1])/2}")
  sum = 0
  for i in modifiedlist:
    sum += i
  average_age = (sum/length_list)
  print(f"d. Average age: {(sum/length_list):.2f}")
  print(f"e. range of age: {max(modifiedlist)} - {min(modifiedlist)} = {max(modifiedlist) - min(modifiedlist)}")
  print(f"f. absolute of min less average is : {abs(min(modifiedlist)-average_age)}, compared to absolute of max less average of {abs(max(modifiedlist)-average_age)}")  
  
  #27 After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
  print("Number 27")
  full_stack = front_end.copy()
  print(f"Original Full Stack: {full_stack}")
  index_insert = full_stack.index("Redux") + 1
  full_stack.insert(index_insert,"Python")
  index_insert += 1
  full_stack.insert(index_insert,"SQL")
  print(f"Final Full Stack: {full_stack}")
  print('\n')

print("Number 1")
  ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
  print(f"Original Age List : {ages}")
  modifiedlist = []
  modifiedlist = ages.copy()
  modifiedlist.sort()
  print(f"a1. Sorted Full Stack: {modifiedlist}")
  print(f"a2. Max value - Full Stack: {max(modifiedlist)}")
  print(f"a3. Min value - Full Stack: {min(modifiedlist)}")
  list_of_minmax = list((min(modifiedlist),max(modifiedlist)))
  modifiedlist.extend(list_of_minmax)
  print(f"b. With Min and Max ages added: {modifiedlist}")
  length_list = len(modifiedlist)
  if length_list % 2 == 1:
    median_index = ceil(length_list/2)-1
    print(f"c. Median age: {modifiedlist[median_index]}")
  else:
    median_index = ceil(length_list/2)-1
    print(f"c. Median age: {(modifiedlist[median_index]+modifiedlist[median_index+1])/2}")
  sum = 0
  for i in modifiedlist:
    sum += i
  average_age = (sum/length_list)
  print(f"d. Average age: {(sum/length_list):.2f}")
  print(f"e. range of age: {max(modifiedlist)} - {min(modifiedlist)} = {max(modifiedlist) - min(modifiedlist)}")
  print(f"f. absolute of min less average is : {abs(min(modifiedlist)-average_age)}, compared to absolute of max less average of {abs(max(modifiedlist)-average_age)}")


  countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe']


  print("Number 2A")
  length_list = len(countries)
  if length_list % 2 == 1:
    startindex = ceil(length_list/2)-1
    endindex = startindex + 1
  else:
    startindex = ceil(length_list/2)-1
    endindex = startindex + 2 #endindex is not included
  print("Middle Country(ies):",countries[startindex:endindex])
  print('\n')
  
  print("Number 2B")
  listA = listB = country_dup = []
  country_dup = countries.copy()
  if length_list % 2 == 1:
    startindex = ceil(length_list/2)
    del country_dup[startindex:]
    listA = country_dup.copy()
    country_dup = countries.copy()
    del country_dup[0:startindex:]
    listB = country_dup.copy()
  else:
    startindex = ceil(length_list/2)
    del country_dup[startindex:]
    listA = country_dup.copy()
    country_dup = countries.copy()
    del country_dup[0:startindex:]
    listB = country_dup.copy()
  print(f"First List has {len(listA)} items: {listA}")
  print('\n'*2)
  print(f"Second List has {len(listB)} items: {listB}")
  print('\n')
    
  print("Number 2C")
  c1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
  ch,ru,usa,*scandic = c1
  print("ch:",ch)
  print("ru:",ru)
  print("usa:",usa)
  print("scandic countries:",scandic) 
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
  main()
