# covid-19 notifiew world version 1.0
import requests
from bs4 import BeautifulSoup
from plyer import notification
import time


res = requests.get('https://www.worldometers.info/coronavirus').text
soup = BeautifulSoup(res, 'html.parser')
soup.encode('utf-8')
cases = soup.find("div",{"class" : "maincounter-number"}).get_text().strip()
print(cases)

def notifyMe(title, message,icon):
    notification.notify(
        title = title,
        message = message,
        app_icon = icon,
        timeout = 5
    )


while (True):
    notifyMe('total number of cases', cases, "F:\covid-19\head.ico")
    print("hii")
    time.sleep(20)
