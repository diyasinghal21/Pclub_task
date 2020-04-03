import requests
import urllib.request
import time
from bs4 import *
import pandas
url = str(input("enter the url"))
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
person = []
proj= []
organization = []
data = soup.findAll('div', attrs = {'class':'md-padding archive-project-card__header archive-project-card__header--mod-0'}) 
for dat in data:
    i = 0
    for tag in dat.findChildren('div'):
        if i%2==0:
            proj.append(tag.text)
        else:
            organization.append(tag.text.split("Organization: ")[1])
        i = i + 1    
for dat in data:
    person.append(dat.h4.text.strip())
df = pandas.DataFrame(data={"Person Name": person, "Project": proj,"Organization": organization})
df.to_csv("./answer1.csv", sep=',',index=False)