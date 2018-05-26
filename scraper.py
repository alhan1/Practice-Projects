from bs4 import BeautifulSoup
import requests
import re

page = requests.get("https://www.sport24.co.za/Soccer/ChampionsLeague/list-of-champions-league-winners-20170602")
soup = BeautifulSoup(page.content, 'html.parser')
Ps = soup.find(id = "article-body").getText()
Ps = re.sub('[0-9]+', '', Ps)
Ps = Ps.split(" ")
file = open("test.txt", "w")
for item in Ps:
	file.write("%s\n" %item)








