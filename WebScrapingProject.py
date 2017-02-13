
#Import module to fetch a webpage
import requests
#Import json to put data into json syntax
import json
#import Beautiful Soup to make webpage into a
#navigable object
from bs4 import BeautifulSoup
#import html parser to parse data 
from html.parser import HTMLParser

class WebScrapeApplication():
    url = "http://www.siliconflorist.com/jobs/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    jobs = soup.find_all("tr")
    print (jobs)


    while soup.tr.next_sibling:
        while soup.tr.children:
            while soup.tr.children("td nth-of-type(1)"):
                PostingDate = td.string
            while soup.tr.children("td nth-of-type(4)"):
                JobLocation = td.string
            while soup.tr.children("td nth-of-type(2)"):
                JobLink = td.a[href]
                JobTitle = td.a.string
                CompanyName = td.string


    file = open("SiliconFloristJobListing", "w")
    output = {"JobPostingDate" : PostingDate, "Job Location" : JobLocation,
              "Job Link" : JobLink, "Job Title" : JobTitle,
              "Company Name" : CompanyName}
    json.dump(output, file)
    file.close()


def main():
    
   mainloop()
