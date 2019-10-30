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


# TODO: extract all important data from the calendar 
# TODO: what to do with Time 
# TODO: what to use to generate .ics file 
