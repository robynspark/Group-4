import csv
import requests
from BeautifulSoup import BeautifulSoup
import time
from datetime import datetime, date, time

#today = str(datetime.date.today().month)+'/'+str(datetime.data.today().day)+'/'+str(datetime.date.today().year)
#url = "http://browse.calendar.gwu.edu/EventList.aspx?fromdate=%s&%s&view=DateTime&display=Day&type=public % (today, today)"
url = "http://browse.calendar.gwu.edu/EventList.aspx?fromdate=4/18/2017&todate=4/18/2017&view=DateTime&display=Day&type=public"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', id="tblEvents")

list_of_rows = []
for row in table.findAll('tr')[2:]:
    list_of_cells = []
    for url in row.findAll('href'):
        list_of_cells.append.a.get_text(url)
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)    
    #for cell in row.findAll('td'):
        #if cell.find('a'):
            #link = cell.find('a')['href']
            #list_of_cells.append(link)
            #list_of_cells.append(cell.html)
        #else:
            #list_of_cells.append(cell.html)
    #list_of_rows.append(list_of_cells)

outfile = open("events2.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["time", "url", "text"])
writer.writerows(list_of_rows)








