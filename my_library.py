import pandas as pd
import numpy as np
import sys
import os
import math

os.system('python -m spacy download en_core_web_md')
import en_core_web_md
nlp = en_core_web_md.load()
def nlp_test(s):
      return nlp(s)
  
my_github_name = 'uo-puddles'
my_library_name = 'uo_puddles'
clone_url = f'git clone https://github.com/{my_github_name}/{my_library_name}.git'  #create the url to get the library
os.system(clone_url) # Cloning

import uo_puddles.uo_puddles as up

def hello():
  print('hello')
  
def dead_week(number):
  return number
