import requests
from BeautifulSoup import BeautifulSoup
import time
import datetime
from twython import Twython
import csv

CONSUMER_KEY = '5shin2F19pX8B6Mz54oPI4qNZ'
CONSUMER_SECRET = 'wrZk1BwReYuL9WOeHH7viBSS9ChPzyty7YryB0DaLI8Afj0s4w'
ACCESS_TOKEN = '855555686448627712-FYvOuLcpQel7S9AA9kVQamz2aAGRb4S'
ACCESS_TOKEN_SECRET = 'WHdZWnfeTZOFEAc70aeJ1UXGqjdPm1fvNx8MGt74zlfn8'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

text = []

today = str(datetime.date.today().month)+'/'+str(datetime.date.today().day)+'/'+str(datetime.date.today().year)
url = "http://browse.calendar.gwu.edu/EventList.aspx?fromdate=%s&todate=%s&view=DateTime&display=Day&type=public" % (today, today)
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', id="tblEvents")

list_of_rows = []
for row in table.findAll('tr')[2:]:
    list_of_cells = []
    first_cell, second_cell = row.findAll('td')
    list_of_cells.append(first_cell.find('a').text)
    list_of_cells.append(second_cell.text)
    list_of_cells.append("http://browse.calendar.gwu.edu/"+second_cell.find('a')['href'])
    list_of_rows.append(list_of_cells)

outfile = open("events2.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["time", "text", "url"])
writer.writerows(list_of_rows)
outfile.close()
 
with open('events2.csv', 'r') as file:
	a = csv.DictReader(file)
	for row in a:
		msg = "%s at %s. URL: %s" % (row['text'], row['time'], row['url'])
		#if len(msg) > 140:
			# need to truncate it
			#msg = (msg[:140])
		twitter.update_status(status=msg)