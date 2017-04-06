
import csv
import requests
from BeautifulSoup import BeautifulSoup

url = "http://browse.calendar.gwu.edu/EventList.aspx?fromdate=4/1/2017&todate=4/1/2017&view=DateTime&display=Day&type=public"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("events.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "url", "text"])
writer.writerows(list_of_rows)

#okay, so I've tried running different urls (for just one day: http://browse.calendar.gwu.edu/EventList.aspx?fromdate=4/1/2017&todate=4/1/2017&view=DateTime&display=Day&type=public) and for multiple days: http://browse.calendar.gwu.edu/EventList.aspx?fromdate=4/6/2017&todate=5/5/2017&view=DateTime)
#and I've tried adjusting the code to scrape just the text and the url and the text
#but it still isn't scraping any data, even though the code runs fine. Is this because there are too many tables in those pages? If so, how can I narrow it to the tables I want?