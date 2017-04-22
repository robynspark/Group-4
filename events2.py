import csv
import requests
from BeautifulSoup import BeautifulSoup
import time
import datetime

today = str(datetime.date.today().month)+'/'+str(datetime.date.today().day)+'/'+str(datetime.date.today().year)
url = "http://browse.calendar.gwu.edu/EventList.aspx?fromdate=%s&todate=%s&view=DateTime&display=Day&type=public" % (today, today)
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', id="tblEvents")

list_of_rows = []
for row in table.findAll('tr')[2:]:
    list_of_cells = []
    # since each row has only two TD tags (cells), I assigned them to the result of row.findAll('td') and called them first_cell and second_cell
    # since we know that href links are always in the second cell, we can just reference it directly. You'll need to make the url a full path.
    first_cell, second_cell = row.findAll('td')
    list_of_cells.append(first_cell.find('a').text)
    list_of_cells.append("http://browse.calendar.gwu.edu/"+second_cell.find('a')['href'])
    list_of_cells.append(second_cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("events2.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["time", "url", "text"])
writer.writerows(list_of_rows)