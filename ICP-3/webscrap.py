from bs4 import BeautifulSoup
import urllib.request
import os
#imported libraries
url="https://en.wikipedia.org/wiki/Deep_learning"
#parsing the source code
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
#Printing the page title
print(soup.title.string)
#finding the links in the page with 'a' tag and return the attribute 'href'
for link in soup.find_all('a'):
    print(link.get('href'))
#Extracting the information into a table
table = soup.find('table', {'class': "wikitable sortable plainrowheaders"})
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    header = row.find('th')
    for column in columns:
        print("<td's>: %s"%(column.text))
    print("<th's>: %s"%(header.text))


