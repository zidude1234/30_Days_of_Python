#Day TwentyOne of the 30 Day Challenge
# Introduction
# Author: dataBio
# Date: 28 Feb 2022
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
import numpy
import webbrowser
import matplotlib
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
  
  class DataStats:
    def __init__ (self, list1 = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]):
            self.data = list1
        
    def describe(self):
          return f''' 
Count: {self.count()} 
Sum: {self.sum()}
Min: {self.min()}
Max: {self.max()}
Range: {self.range()}
Mean: {self.mean():.2f}
Median: {self.median()}
Mode: {self.mode()}
Standard Deviation: {self.std():.0f}
Variance: {self.var():.2f}
Frequency Distribution:
{self.freq_dist()} 
          '''
    def __len(self):
          return self.count() 

    def count(self):
          return len(self.data)

    def sum(self):
          return sum(self.data)

    def min(self):
          return min(self.data)

    def max(self):
          return max(self.data)  

    def range(self):
          return max(self.data) - min(self.data)

    def mean(self):
          return statistics.mean(self.data)

    def median(self):
          return statistics.median(self.data)  
        
    def mode(self):
          parameters,mode_list = ['mode','count'],[]
          temp = []
          counttemp = []
          dict_mode = {'mode': 0 ,'count' : 0 }
          if (len(statistics.multimode(self.data))==1):
             uni_mode = statistics.multimode(self.data)
             dict_mode['mode'] = uni_mode[0]
             dict_mode['count'] = self.data.count(uni_mode[0])
             return dict_mode
          else:
             temp = statistics.multimode(self.data)
             counttemp = [self.data.count(i) for i in temp]
             mode_list.append(temp)
             mode_list.append(counttemp)
             dict_mode = list(zip(parameters,mode_list))
             return dict_mode

    def std(self):
          return statistics.stdev(self.data)

    def var(self):
          return statistics.variance(self.data) 
        
    def freq_dist(self):
          freq_list = []
          freq_c1 = collections.Counter(self.data).items()
          freq_collection = [(_freq, _value) for (_value,_freq) in freq_c1]
          freq_tuple = sorted(freq_collection,key = lambda k:k , reverse = True)
          sumX = len(self.data)
          for i in freq_tuple:
            tp = (i[0] * 100/sumX,i[1])
            freq_list.append(tp)
          s2 = f'Frequency distribution in percentage {freq_list}'
          return s2
    
  class PersonAccount:
      def __init__ (self, firstname='power', lastname='shell', income = {"Income1":250000,"Income2":20000,"Income3":3000}, expenses = {"Expense1":200000,"Expense2":5000,"Expense3":3000}):
          # self allows to attach parameter to the class
            self.firstname = firstname
            self.lastname = lastname
            self.income = income
            self.expenses = expenses
        
      def total_income(self):
          return sum(self.income.values())

      def total_expenses(self):
        return sum(self.expenses.values())
  
      def add_income(self):
        #self.income[new_income_tp[0]] = new_income_tp[1]
        pass

      def describe(self):
          return f''' 
Name {self.firstname} {self.lastname}
Income {self.income} 
Expenses: {self.expenses}
Total Income: {self.total_income()}
Total Expenses: {self.total_expenses()}
'''
      
    # You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class.
  ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

    # print('Count:', data.count()) # 25
    # print('Sum: ', data.sum()) # 744
    # print('Min: ', data.min()) # 24
    # print('Max: ', data.max()) # 38
    # print('Range: ', data.range() # 14
    # print('Mean: ', data.mean()) # 30
    # print('Median: ', data.median()) # 29
    # print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
    # print('Standard Deviation: ', data.std()) # 4.2
    # print('Variance: ', data.var()) # 17.5
    # print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
  banner = bannergreeting
  print(banner(21,1))

  data1 = DataStats()
  p(1)
  print(data1.describe())
  pn()

  personTest = PersonAccount()
  p(2)
  print(personTest.describe())
  pn()


  


  

    
if __name__ == "__main__":
  main()
