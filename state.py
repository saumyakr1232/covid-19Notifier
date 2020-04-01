from bs4 import BeautifulSoup
import requests


res = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(res, 'html.parser')
soup.encode('utf-8')


stateTable = soup.find("table", {"class":"table table-striped"}).get_text().strip().split("\n\n")
print(stateTable)
for i in stateTable:
    if(i.find("Bihar") >0):
        bihar = i.replace('\n','',1).split('\n')
    if(i.find("Uttar Pradesh") > 0):
        up = i.replace('\n','',1).split('\n')
    if(i.find("Delhi")>0):
        delhi = i.replace('\n', '', 1).split('\n')
    if(i.find("Punjab")> 0 ):
        punjab = i.replace('\n', '', 1).split('\n')
print(bihar)
print(up)
print(delhi)
print(punjab)
