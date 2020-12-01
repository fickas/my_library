import pandas as pd
import sys
import os

my_github_name = 'uo-puddles'  #this is one of my github accounts
my_library_name = 'uo_puddles' #this is name of repository I keep on github - easy to set up!
clone_url = f'https://github.com/{my_github_name}/{my_library_name}.git'  #create the url to get the library

path  =  '/' # "/path/to/store/your/cloned/project" 
clone = "git clone gitolite@<server_ip>:/your/project/name.git" 

#os.system("sshpass -p your_password ssh user_name@your_localhost")
os.chdir(path) # Specifying the path where the cloned project needs to be copied
os.system(clone_url) # Cloning

import uo_puddles.uo_puddles as up

def hello():
  print('hello')
  
def dead_week(number):
  return number
