#Day TwentyTwo of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 01 Mar 2022
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
import collections
import datetime
from itertools import chain
import json
import csv
import numpy as np
import webbrowser
import matplotlib as plt
import requests
import statistics
import pandas as pd
from bs4 import BeautifulSoup


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

  banner = bannergreeting
  print(banner(22,1))

  #1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
  p(1)
  boston_uni_url = 'http://www.bu.edu/president/boston-university-facts-stats/'
  bu_response = requests.get(boston_uni_url)
  bu_response_content = bu_response.content # we get all the content from the website
  soup = BeautifulSoup(bu_response_content,features='lxml')# beautiful soup will give a chance to parse
  print(soup.title) # <title>BU Facts &amp; Stats | Office of the President</title>
  print(soup.title.get_text()) # BU Facts & Stats | Office of the President
  print(bu_response.status_code)
  
  
  #Get Data tables in Website
  bu_stats = soup.find_all(class_="facts-wrapper")
  table_stat_dictlist,txt_items_combined,txt_values_combined = [],[],[]
  for i in bu_stats:
    txt_t_items = [j.get_text() for j in i.find_all(class_="text")]
    txt_t_values = [j.get_text() for j in i.find_all(class_="value")]
    txt_items_combined.append(txt_t_items)
    txt_values_combined.append(txt_t_values)
    table_stat_dictlist.append(dict(zip(txt_t_items,txt_t_values)))
  with open("bu_stats.json",'w') as bu_json:
    json.dump(table_stat_dictlist,bu_json)   #write to file

  #2 Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
  ml_url = 'https://archive.ics.uci.edu/ml/datasets.php'

  response = requests.get(ml_url)
  content = response.content # we get all the content from the website
  soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
  print(response.status_code)
  tables = soup.find_all('table', {'cellpadding':'3'}) #<table cellpadding=3>
  table = tables[0]
  s = ''
  for td in table.find('tr').find_all('td'):
    s += td.text
  
  with open("ml_stats.json",'w') as ml_json:
    json.dump(s,ml_json)   #write to file
  
  #3 Scrape the presidents table and store the data as json
  uspres_url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
  response = requests.get(uspres_url)
  content = response.content 
  soup = BeautifulSoup(content, 'html.parser') 
  print(soup.title) 
  print(soup.title.get_text()) 
  print(response.status_code)

  tables = soup.find_all('table', class_ = "wikitable sortable") 
  pres_table = tables[0] # the result is a list, we are taking out data from it

  for td in pres_table.find_all('td'):
      s += td.text
  
  with open("us_presidents.json",'w') as us_pres_json:
    json.dump(s,us_pres_json)
    
if __name__ == "__main__":
  main()
