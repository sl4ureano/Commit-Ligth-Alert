#!/usr/bin/env python
"""
__author__ = "Adriano Laureano"
__copyright__ = "Copyright 2019"]
__license__ = "GPL"
__version__ = "2.0.0"
__maintainer__ = "@sl4ureano"
__email__ = "sl4ureano@outlook.com"
__status__ = "Production"
"""

from blink1.blink1 import Blink1
import time,os
import requests


class ClassCommit():
    def __init__(self,user,repository,token,time_refresh):        
        '''
        :param str user: Your user on github
        :param str repository str: Your repository on github
        :param str token str: Your personal access token on github
        :param int time_refresh int: Refresh time       
        '''
        self.user = user
        self.repository = repository
        self.token = token
        self.time_refresh = time_refresh
        self.temp_file = "temp.db"
    
    def Ligth(self):
        b1 = Blink1()
        b1.writePatternLine( 100, 'red',  3)
        b1.writePatternLine( 100, 'black',  4)
        b1.writePatternLine( 100, 'blue', 5)
        b1.play(3,5,15)
        time.sleep(3)
        b1.fade_to_color(100, 'black')
    
    def Refresh(self):
        try:
            request = requests.get('https://api.github.com/repos/{}/{}?access_token={}'.format(self.user,self.repository,self.token))
            data =  request.json()
            last_update = data['updated_at']
            try:
                with open(self.temp_file) as f:
                    last_commit = f.readline()            
            except FileNotFoundError:
                file_ = open(self.temp_file, 'w+')
                file_.write(last_update) 
                file_.close()
            if last_update != last_commit:
                print ("New Commit at " + last_commit)
                os.system('color 2')
                file_ = open(self.temp_file, 'w+')
                file_.write(last_update) 
                file_.close()
                self.Light()
                time.sleep(self.time_refresh)
                self.Main()
            else:
                time.sleep(self.time_refresh)
                self.Main()        
        except:
            print ("Request failed")
            os.system('color 4')
            time.sleep(self.time_refresh)
            self.Main()
    
    def Main(self):
        print ("Refresh at " + time.ctime())
        os.system('color 3')
        self.Refresh()

#How to Use
#commit = ClassCommit('sl4ureano','Commit-Ligth-Alert','fdcabe6726c162545b116e63b9045459ef56',5)
#commit.Main()