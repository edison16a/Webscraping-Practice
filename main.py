import requests
from bs4 import BeautifulSoup
import pandas as pd



page = requests.get("https://lego--pichar.repl.co/lego.html")

soup = BeautifulSoup(page.text, 'html.parser')

lstJumbotron=[]

names = soup.findAll(class_='jumbotron')

for jumbotron in names:
  cleanj = jumbotron.get_text()
  lstJumbotron.append(cleanj)
  print(cleanj)


  








df=pd.DataFrame({'Product Name':lstJumbotron})

df.to_csv('jumbotron.csv', index=False, encoding='utf-8')