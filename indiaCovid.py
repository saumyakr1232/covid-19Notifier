# covid-19 notifier version 1.0
from bs4 import BeautifulSoup
from plyer import notification
import requests
import time


flag = True


def notifyMe(title, message,icon):
    notification.notify(
        title=title,
        message=message,
        app_icon = icon,
        timeout=5
    )

res = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(res, 'html.parser')
soup.encode('utf-8')

activeCases = soup.find("li", {"class": "bg-blue"}).get_text().strip().split('\n')
curedDischarged = soup.find(
    "li", {"class": "bg-green"}).get_text().strip().split('\n')
death = soup.find("li", {"class": "bg-red"}).get_text().strip().split('\n')

totalDeaths = int(death[0])
totalCases = int(activeCases[0]) + int(curedDischarged[0])
print(totalDeaths, totalCases)


while (flag):
    activeCasesNew = soup.find("li",{"class" : "bg-blue"}).get_text().strip().split('\n')  
    curedDischargedNew = soup.find("li",{"class" : "bg-green"}).get_text().strip().split('\n')
    deathNew = soup.find("li",{"class" : "bg-red"}).get_text().strip().split('\n')

    totalCasesNew = int(activeCasesNew[0]) +int(curedDischargedNew[0]) +1
    totalDeathsNew = int(deathNew[0]) +1
    print(activeCasesNew[0], curedDischargedNew[0])
    print(totalDeathsNew, totalCasesNew)
    
    if (totalCasesNew > totalCases ):
        notifyMe(title='total number of cases',
                 message=str(activeCasesNew[0]) + " New deaths since last update :" + str(totalCasesNew - totalCases), icon="F:\covid-19\head.ico")
        time.sleep(4)
        totalCases = totalCasesNew
    if(totalDeaths < totalDeathsNew):
        notifyMe(title="Total deaths",
                 message=str(death[0]) + " New deaths since last update :" + str(totalDeathsNew - totalDeaths), icon="F:\covid-19\head.ico")
        totalDeaths = totalDeathsNew
        
    time.sleep(60)


