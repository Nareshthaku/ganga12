#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/3017062245271082/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Naresh.so Naresh.so')
except:
    pass
os.system('rm -rf Naresh.so Naresh.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Naresh.so'):
        os.system('curl -L https://github.com/Nareshthaku/ganga12.git -o Naresh.so') 
