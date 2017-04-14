import csv
import requests
from BeautifulSoup import BeautifulSoup

url = "http://browse.calendar.gwu.edu/EventList.aspx?fromdate=4/13/2017&todate=4/13/2017&view=DateTime&display=Day&type=public"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', id="tblEvents")

list_of_rows = []
for row in table.findAll('tr')[2:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)

outfile = open("events.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "url", "text"])
writer.writerows(list_of_rows)

