import requests
import json
from bs4 import BeautifulSoup
from html.parser import HTMLParser


url = "http://www.siliconflorist.com/jobs/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
#rows = soup.find_all("tr")
#print (rows)

#print (soup.contents)

#Table_Tag = soup.table
#print (Table_Tag.contents)
#print (Table_Tag.contents[3])


Table_Body = soup.tbody
for i in range (1, 15, 2):
    job_links = Table_Body.contents[i].contents[3].contents[1]
    JobLink = job_links.attrs
    print(JobLink)
    




#lengthTable_Body = len(list(Table_Body.children))
#print (lengthTable_Body)

                            
#date_posted = Table_Body.contents[1].contents[1]
#datepostedText = date_posted.string
#print (Table_Body.contents[1].contents[1])
#print(datepostedText)

#job_title = Table_Body.contents[1].contents[3].contents[1]
#jobtitleText = job_title.string
#print(jobtitleText)

#company_name = Table_Body.contents[1].contents[3].contents[3]
#companynameText = company_name.string
#print(companynameText)


#job_location = Table_Body.contents[1].contents[7]
#joblocationText = job_location.string
#print(joblocationText)


#job_links = soup.select("td > a")
#print (job_links)

#joblinks = job_links[0]
#print(joblinks)

#print(joblinks.attrs)

    



