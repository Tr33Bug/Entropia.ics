import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# target URL
myUrl = 'https://entropia.de/'

# download the Page
uClient = uReq(myUrl)

pageHtml = uClient.read()

# close the Client
uClient.close()

# html parsing
pageSoup = soup(pageHtml, "html.parser")

rows = pageSoup.findAll("tr")

# create 2 dimensional array from source
array = ["null"] 
for i in range(0,len(rows)):
    rowsy = rows[i].findAll("td")
    array[i] = rowsy
    array.append("null") 

# delete all html flags in the Array
for i in range(1,len(array)):
    for x in range(0,len(array[i])):
       array[i][x] = array[i][x].text
       array[i][x]


exfile = open("termine.ics","w")
exfile.write("""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//217.160.0.72//NONSGML kigkonsult.se iCalcreator 2.26.9//
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Entropia
X-WR-CALDESC:
X-FROM-URL:https://github.com/Tr33Bug/Entropia.ics
X-WR-TIMEZONE:Europe/Berlin
BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:STANDARD
DTSTART:20191030T030000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RDATE:20201025T030000
TZNAME:CET
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:20190331T020000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RDATE:20200329T020000,20210328T020000
TZNAME:CEST
END:DAYLIGHT
END:VTIMEZONE
BEGIN:VEVENT
UID:tr33bug@gmail.com
DTSTAMP:20191030T204618Z
CATEGORIES:
CONTACT:
DESCRIPTION:
DTSTART;TZID=Europe/Berlin:20191108T103000
DTEND;TZID=Europe/Berlin:20191108T123000
LOCATION:zw. BVerfG und Schloss @ zw. BVerfG und Schloss
SEQUENCE:0
SUMMARY:„Containern ist kein Verbrechen“ – Kundgebung u.a. mit Grüne Jugend
URL:https://gruenekarlsruhe.de/Veranstaltung/containern-ist-kein-verbrechen
 -kundgebung-u-a-mit-gruene-jugend/
X-COST-TYPE:free
END:VEVENT
END:VCALENDAR

""")

# for i in range(1,len(array)):
#     for x in range(0,len(array[i])):
#        exfile.write(array[i][x] + "\n")

exfile.close();








# TODO: extract all important data from the calendar 
# TODO: what to do with Time 
# TODO: what to use to generate .ics file 
