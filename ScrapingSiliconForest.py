#Title: Scrape Silicon Florist Website
#Course: Live Project
#School: The Tech Academy
#Author: Yuuna Kaparti



import requests
import json
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re



url = "http://www.siliconflorist.com/jobs/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
Table_Body = soup.tbody

json_job_dictionary = {}
json_scrape_file = open("SiliconFloristJsonListing.txt", "w") 

for i in range (1, 15, 2):
    #Job_Posting_Date
    date_posted = Table_Body.contents[i].contents[1]
    datepostedText = date_posted.string
    datepostedText = datepostedText.strip()
    print('Job Posting Date: ', re.sub('\s+',' ', datepostedText))
    json_job_dictionary.update({"Job Posting Date" : datepostedText})

    #Job_Title
    job_title = Table_Body.contents[i].contents[3].contents[1]
    jobtitleText = job_title.string
    print('Job Title: ', re.sub('\s+',' ', jobtitleText))
    json_job_dictionary.update({"Job Title": jobtitleText})

    #Company_Name
    company_name = Table_Body.contents[i].contents[3].contents[3]
    company_name = company_name.strip()
    print('Company Name: ', re.sub('\s+', ' ', company_name))
    json_job_dictionary.update({"Company Name": company_name})

    #Job_Location
    job_location = Table_Body.contents[i].contents[7]
    joblocationText = job_location.string
    joblocationText = joblocationText.strip()
    print ('Job Location: ', re.sub('\s+', ' ', joblocationText))
    json_job_dictionary.update({"Job Location": joblocationText})

    #Job_Links
    job_links = Table_Body.contents[i].contents[3].contents[1]
    JobLink = job_links.attrs
    print ('Job Link: ', JobLink)
    json_job_dictionary.update({"Job Link": JobLink})

    #Create a JSON file 
    json.dump(json_job_dictionary, json_scrape_file)
    new_object = json.dumps(json_job_dictionary, sort_keys=True, indent=4)
    print('JSON format: ', re.sub('\s+', ' ',json.dumps(json_job_dictionary)))
    print("\n")



    

json_scrape_file.close()
                                


#Note: In addition to the method used above to strip extra white space,
#you can also try the following strategies:
#example = " hello apple"
#example.strip() >> "hello apple"
#example.replace(" ", "")  >> "helloapple"
#" ".join(example.split())  >> "hello apple"
