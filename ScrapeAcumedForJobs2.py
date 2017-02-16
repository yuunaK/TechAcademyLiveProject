import requests
import urllib.request
import json
from bs4 import BeautifulSoup
import bs4 as bs
from html.parser import HTMLParser
import re


url = "https://www.acumed.net/careers?order=title&sort=desc"
source = urllib.request.urlopen(url)
soup = BeautifulSoup(source, "lxml")
tableBody = soup.tbody

#Create json dicitionary
json_job_dictionary = {}
json_scrape_file = open("AcumedJsonListing", "w")

#job posting date
date_posted = " "
print('Job Posting Date: ', re.sub('\s+',' ', date_posted))
json_job_dictionary.update({"Job Posting Date" : date_posted})

#job location
job_location = "Hillsboro, OR, USA"
print ('Job Location: ', re.sub('\s+', ' ', job_location))
json_job_dictionary.update({"Job Location": job_location})

#company name
company_name = "Acumed"
print('Company Name: ', re.sub('\s+', ' ', company_name))
json_job_dictionary.update({"Company Name": company_name})


for i in range(1, len(tableBody.contents), 2 ):
    Department = tableBody.contents[i].contents[5]
    department = Department.string.strip()
    if department == "Information Technology" :
        job_title = tableBody.contents[i].contents[1]
        jobtitle = job_title.string.strip()
        print (jobtitle)


