from blink1.blink1 import Blink1
import time
import requests

user = "sl4ureano" 
repo = "Commit-Ligth-Alert"
access_token = ""

def Light():
    b1 = Blink1()
    b1.writePatternLine( 100, 'red',  3)
    b1.writePatternLine( 100, 'black',  4)
    b1.writePatternLine( 100, 'blue', 5)
    b1.play(3,5,15)
    time.sleep(3)
    b1.fade_to_color(100, 'black')

def Verify():
    try:
        request = requests.get('https://api.github.com/repos/{}/{}?access_token={}'.format(user, repo,access_token))
    except:
        print "Request failed"
        time.sleep(10)
        Main()
    data =  request.json()
    update = data['updated_at']
    with open('lastcommit.txt') as f:
        lastcommit = f.readline()
    if update != lastcommit:
        print "New Commit"
        file = open("lastcommit.txt","w")
        file.write(update)
        file.close()
        Light()
        time.sleep(10)
        Main()
    else:
        time.sleep(10)
        Main()

def Main():
    print "Verify news Commits"
    Verify()

Main()
