import pandas as pd
import numpy as np
import sys
import os
import math

#bring in spacy. Note might want to comment this out if don't like wait time.
os.system('python -m spacy download en_core_web_md')
import en_core_web_md
nlp = en_core_web_md.load()

#bring in uo-puddles
my_github_name = 'uo-puddles'
my_library_name = 'uo_puddles'
clone_url = f'git clone https://github.com/{my_github_name}/{my_library_name}.git'  #create the url to get the library
os.system(clone_url) # Cloning
import uo_puddles.uo_puddles as up

#put your functions below
def hello():
  print('hello')

