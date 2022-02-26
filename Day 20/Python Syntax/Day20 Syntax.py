#Day Twenty of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 25 Feb 2022
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
  print(banner(20,1))
  
  def top_words_in_english(all_text, num_extract = 10):
    list_words,templist = [],[]
    seperate_words = list(filter(None,re.split('\s+|\.',all_text)))
    words_group = collections.Counter(seperate_words)
    w_tp = words_group.items()
    w_tp2 = [(b,a) for (a,b) in w_tp] 
    w_tuple = sorted(w_tp2,key = lambda k:k[0],reverse=True)
    return w_tuple[0:num_extract]
  
  def cleanuprange(cellrange):
    cell1 = []
    m = re.findall('\d+', cellrange)
    for i in m:
      cell1.append(int(i))
    return tuple(cell1)

  #1.Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
  p(1)
  romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
  r_j_response = requests.get(romeo_and_juliet)
  print(r_j_response.status_code) 
  print(r_j_response.headers)     
  text_to_search = r_j_response.text
  print(top_words_in_english(text_to_search))
  
  #2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
        # the min, max, mean, median, standard deviation of cats' weight in metric units.
        # the min, max, mean, median, standard deviation of cats' lifespan in years.
        # Create a frequency table of country and breed of cats
  
  p(2)
  cat_api = 'https://api.thecatapi.com/v1/breeds'
  response = requests.get(cat_api)
  print(response.status_code) 
  c1 = response.json()
  print(len(c1)) #67 breeds
  
  #"weight" := { "imperial" := "8 - 15" , "metric" := "4 - 7"} 
  #use the values: ('7  -  10', '3 - 5') pick the metric
  a,cat_weight,cat_life,cat_country_breed = [],[],[],[]
  for cat_data in c1:
    w = tuple(cat_data["weight"].values())[1]
    l = cat_data["life_span"]
    c = cat_data["origin"]
    a.append(list((w,l,c))) #['5 - 8', '13 - 15', 'United States'] weight in kg, years and country
  
  catdata_stat = []
  for i in a:
    templist = []
    templist.append(cleanuprange(i[0]))  #[(5,8),(13,15), 'United States'] weight in kg, years and country
    templist.append(cleanuprange(i[1]))
    templist.append(i[2])
    catdata_stat.append(templist)

  c_data_for_statistics = []
  for i in catdata_stat:
    templist = []
    templist.append(statistics.mean(i[0])) 
    templist.append(statistics.mean(i[1]))
    templist.append(i[2])
    c_data_for_statistics.append(templist) #[6.5, 14, 'United States']]
  
  for i in c_data_for_statistics:
    c_weight.append(i[0])
    c_years.append(i[1])
    c_freq.append(i[2])
  print(f"""the following are the statistics:
  min: {min(c_weight)} kg \t max {max(c_weight)} kg
  mean: {statistics.mean(c_weight):.1f} kg \t median {statistics.median(c_weight)} kg
  standard deviation: {statistics.stdev(c_weight):.3f} kg """)

  


  

    
if __name__ == "__main__":
  main()
