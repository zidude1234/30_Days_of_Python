#Day Nineteen of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 22 Feb 2022
# IDE: VSCode

# import the "sys" module
from importlib.resources import path
import sys
# import the "os" module
import os
# import the "platform" module
import platform
# import the "platform" module
import math
# import the "re" module
import re
import collections
import datetime
from itertools import chain
import json
import csv

def main():
  os.system("cls") # clear console
  
  def p(num):
    print(f"Number {num}")

  def pn(num = 1):
    print(f"\n" * num)

  def bannergreeting(day_name,exercise_name):
    daybanner = f'Exercise {day_name} '
    exercisebanner = f'Level {exercise_name} '
    front_end = f'--' * 20
    return combinebanners(front_end,daybanner,exercisebanner)
  
  def combinebanners(s0,s1,s2):
    return s0 + s1 + s2 + s0
  
  def topten_languages(country_data, num_lang=5):
    list_lang = []
    for data in country_data:
      lang_count = data["languages"]
      list_lang.append(lang_count)
    list_flat = [i for level1 in list_lang for i in level1]
    lang_collection = collections.Counter(list_flat)
    top10_lang_collection = lang_collection.most_common(num_lang)
    print(f'The {num_lang} most common lanaguages are;')
    for i in top10_lang_collection:
      print(i)
    return ""

  def topten_pop(country_data, num_countries=10):
    list_lang_country_pop,templist = [],[]
    for data in country_data:
      keyitems = ['name',"languages","population"]
      lang_count_pop = {k:data[k] for k in keyitems}
      templist.append(lang_count_pop)
    list_lang_country_pop = sorted(templist, key = lambda k: k["population"], reverse=True)
    print(f'The {num_countries} most populated countries are;')
    for i in list_lang_country_pop[0:num_countries]:
      print(i)
    return ""
  
  def top_words_in_english(fname, num_extract = 5):
    filename = "".join([newpath,fname])
    f1 = open(filename)
    all_text = f1.read()
    seperate_words = list(filter(None,re.split('\s+|\.',all_text)))
    words_group = collections.Counter(seperate_words)
    w_tp = words_group.items()
    w_tp2 = [(b,a) for (a,b) in w_tp] 
    w_tuple = sorted(w_tp2,key = lambda k:k[0],reverse=True)
    return w_tuple[0:num_extract]
  
  def compare_files_for_similarity(fileX,fileY):
    temp1 = open(fileX)
    file1 = list(filter(None,re.split('\s+|\.',temp1.read())))
    temp1.close()
    temp2 = open(fileY)
    file2 = list(filter(None,re.split('\s+|\.',temp2.read())))
    dict1 = {x : file1.count(x) for x in file1}
    dict2 = {x : file2.count(x) for x in file2}
    similars = set(file1).intersection(set(file2))
    rate1 = sum(dict1[w] for w in similars)/len(file1)
    rate2 = sum(dict2[w] for w in similars)/len(file2)
    print("The rate of similarity is: ", rate1*rate2*100, '%')
    print("The similar words are: ", similars)
    return ''
  
  banner = bannergreeting
  print(banner(19,1))

  #1 Write a function which count number of lines and number of words in a text. 
  #  a) Read obama_speech.txt file and count number of lines and words 
  #  b) Read michelle_obama_speech.txt file and count number of lines and words 
  #  c) Read donald_speech.txt file and count number of lines and words 
  #  d) Read melina_trump_speech.txt file and count number of lines and words
  
  p(1)
  #python file is in Day19/Python Syntax folder
  #data file is in Day19/data folder
  
  fulldir = os.path.dirname(__file__)
  rootdir = fulldir.rsplit('\\',1) 
  newpath=rootdir[0]+'\\data\\'
 
  _obamapath = "".join([newpath,'obama_speech.txt'])
  _michpath = "".join([newpath,'michelle_obama_speech.txt'])
  _trumppath = "".join([newpath,'donald_speech.txt'])
  _melapath = "".join([newpath,'melina_trump_speech.txt'])
  #1A 
  f1 = open(_obamapath)
  Lines = f1.readlines() #All Lines
  Linenum = 0
  for linetext in Lines:
    Linenum +=1
  filename = _obamapath.rsplit('\\',1)[1]
  print(f"{filename} has {Linenum} lines")
  f1.close()

  f2 = open(_michpath)
  Lines = f2.readlines() #All Lines
  Linenum = 0
  for linetext in Lines:
    Linenum +=1
  filename = _michpath.rsplit('\\',1)[1]
  print(f"{filename} has {Linenum} lines")
  f2.close() 

  f3 = open(_trumppath)
  Lines = f3.readlines() #All Lines
  Linenum = 0
  for linetext in Lines:
    Linenum +=1
  filename = _trumppath.rsplit('\\',1)[1]
  print(f"{filename} has {Linenum} lines")
  f3.close() 
  
  
  f4 = open(_melapath)
  Lines = f4.readlines() #All Lines
  Linenum = 0
  for linetext in Lines:
    Linenum +=1
  filename = _melapath.rsplit('\\',1)[1]
  print(f"{filename} has {Linenum} lines")
  f4.close() 
  pn(2)
  p(2)
  with open('country_data.json') as file_object:
    c_data = json.loads(json.load(file_object))
    print(topten_languages(c_data,3))
    print(topten_languages(c_data,10))
    file_object.close()
  
  pn()
  p(3)
  #3 Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
  print(topten_pop(c_data,3))
  print(topten_pop(c_data,10))
  
  #4 Extract all incoming email addresses as a list from the email_exchange_big.txt file.
  p(4)
  _email_exchangepath = "".join([newpath,'email_exchanges_big.txt'])
  emailpattern = '^From.[\w([\w\.]+\s?\w*\+?@\w+\.?\w*\.?\w*\.?\w*' #from emails


  with open(_email_exchangepath) as file_object:
      Lines = file_object.readlines() 
      List_emails,str_response_from = [],''
      linenum = 0
      for linetext in Lines:
        from_emails = re.findall(emailpattern2,linetext)
        linenum += 1
        if from_emails:
          s2 = f"'From Email' noted on line {linenum} : {from_emails}"
          str_response_from += s2 + '\n'
      with open("from_emails.txt",'w+') as file_object1:
        file_object1.write(str_response_from)
      file_object1.close()
      file_object.close() 
 
  p(5)
  print(top_words_in_english('obama_speech.txt', 10))
  pn()
  
  p(6)
  print(top_words_in_english('donald_speech.txt', 10))
  print(top_words_in_english('melina_trump_speech.txt', 10))
  print(top_words_in_english('michelle_obama_speech.txt', 10))
  pn()
  
  p(7)
  print(compare_files_for_similarity(_michpath,_melapath))
  pn()
  
  p(8)
  print(top_words_in_english('romeo_and_juliet.txt', 10))
  pn()

  p(9)
  strings_list = ['"Python or python"','"JavaScript or javaScript or javascript"','"Java"']
  stringlist = ['[P|p]ython','([J|j]avaScript|[J|j]avascript)',r'\bJava\b'] #regex pattern
  _hackerpath = "".join([newpath,'hacker_news.csv'])
  for i in stringlist:
    searchstring = strings_list[stringlist.index(i)]
    linecount, linestring = 0,0
    with open(_hackerpath) as hackerfile:
      csv_data = csv.reader(hackerfile,delimiter = ',')
      for row in csv_data:
        linecount +=1 
        rowstring = ', '.join(row)
        if(re.findall(i,rowstring)):
            linestring +=1
    print(f'Hackerfile has {linecount} rows with {searchstring} found in {linestring} lines.')
    
    
    
if __name__ == "__main__":
  main()
