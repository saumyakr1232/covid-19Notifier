# covid-19 notifiew world version 1.1
import requests
from bs4 import BeautifulSoup
from plyer import notification
import time


res = requests.get('https://www.worldometers.info/coronavirus').text
soup = BeautifulSoup(res, 'html.parser')
soup.encode('utf-8')
cases = soup.find("div",{"class" : "maincounter-number"}).get_text().strip()
cases = int(cases.replace(',',''))



def notifyMe(title, message,icon):
    notification.notify(
        title = title,
        message = message,
        app_icon = icon,
        timeout = 5
    )

print(cases)
while (True):
    res = requests.get('https://www.worldometers.info/coronavirus').text
    soup = BeautifulSoup(res, 'html.parser')
    soup.encode('utf-8')
    newcases = soup.find("div", {"class": "maincounter-number"}).get_text().strip()
    newcases = int(newcases.replace(',', ''))
    print(newcases) 
    if (newcases > cases):
        notifyMe('total number of cases', str(newcases), "F:\covid-19\head.ico")
        cases = newcases
    time.sleep(20)
