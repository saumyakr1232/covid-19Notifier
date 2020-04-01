# covid-19 notifier version 1.3
from bs4 import BeautifulSoup
from plyer import notification
import requests
import time


flag = True


def notifyMe(title, message, icon):
    notification.notify(
        title=title,
        message=message,
        app_icon=icon
    )


res = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(res, 'html.parser')
soup.encode('utf-8')

activeCases = soup.find("li", {"class": "bg-blue"}
                        ).get_text().strip().split('\n')
curedDischarged = soup.find(
    "li", {"class": "bg-green"}).get_text().strip().split('\n')
death = soup.find("li", {"class": "bg-red"}).get_text().strip().split('\n')


totalDeaths = int(death[0])
totalCases = int(activeCases[0]) + int(curedDischarged[0]) + int(death[0])
print(totalDeaths, totalCases)


stateTable = soup.find(
    "table", {"class": "table table-striped"}).get_text().strip().split("\n\n")
for i in stateTable:
    if(i.find("Bihar") > 0):
        bihar = i.replace('\n', '', 1).split('\n')
    if(i.find("Uttar Pradesh") > 0):
        up = i.replace('\n', '', 1).split('\n')
    if(i.find("Delhi") > 0):
        delhi = i.replace('\n', '', 1).split('\n')
    if(i.find("Punjab") > 0):
        punjab = i.replace('\n', '', 1).split('\n')


while (flag):
    res = requests.get('https://www.mohfw.gov.in/').text
    soup = BeautifulSoup(res, 'html.parser')
    soup.encode('utf-8')
    activeCasesNew = soup.find(
        "li", {"class": "bg-blue"}).get_text().strip().split('\n')
    curedDischargedNew = soup.find(
        "li", {"class": "bg-green"}).get_text().strip().split('\n')
    deathNew = soup.find("li", {"class": "bg-red"}
                         ).get_text().strip().split('\n')

    totalCasesNew = int(
        activeCasesNew[0]) + int(curedDischargedNew[0]) + int(deathNew[0])+1
    totalDeathsNew = int(deathNew[0]) + 1
    print(activeCasesNew[0], curedDischargedNew[0])
    print(totalDeathsNew, totalCasesNew)

    if (totalCasesNew > totalCases):
        notifyMe(title=f'Total number of cases : {totalCasesNew}',
                 message=f"New cases since last update : {totalCasesNew - totalCases}\n{bihar[1]} : Total cases = {bihar[2]} Deaths = {bihar[4]}\nUP : Total cases = {up[2]} Deaths ={up[4]}", icon="F:\covid-19\head.ico")

        time.sleep(10)

        totalCases = totalCasesNew
    if(totalDeaths < totalDeathsNew):
        notifyMe(title="Total deaths :" + str(deathNew[0]),
                 message=f"New cases since last update : {totalDeathsNew - totalDeaths}\n{bihar[1]} : Total cases = {bihar[2]} Deaths = {bihar[4]}\nUP : Total cases = {up[2]} Deaths ={up[4]} ", icon="F:\covid-19\head.ico")
        totalDeaths = totalDeathsNew

    time.sleep(60)

