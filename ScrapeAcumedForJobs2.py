#Title: Scrape Acumed Careers Webpage
#Course: Live Project
#School: The Tech Academy (Portland, OR)
#Author: Yuuna Kaparti


import urllib.request
import requests
import json
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re


url ="http://www.acumed.net/careers"
resource = requests.get(url)
soup = BeautifulSoup(resource.content, "lxml")
tableBody = soup.tbody

#Create json dicitionary
json_job_dictionary = {}
json_scrape_file = open("AcumedJsonListing", "w")


for i in range(1, len(tableBody.contents), 2 ):

    #job title
    Department = tableBody.contents[i].contents[5]
    department = Department.string.strip()
    if department == "Information Technology" :
        job_title = tableBody.contents[i].contents[1]
        jobtitle = job_title.string.strip()
        print ("Job Title: ", jobtitle)
        json_job_dictionary.update({"Job Title" : jobtitle})

        #job id
        job_id = ""
        print("Job Id: ", job_id)
        json_job_dictionary.update({"Job Id" : job_id})

        #job posting date
        date_posted = ""
        print('Job Posting Date: ', date_posted)
        json_job_dictionary.update({"Job Posting Date" : date_posted})

        #job location
        job_location = "Hillsboro, OR, USA"
        print ('Job Location: ', job_location)
        json_job_dictionary.update({"Job Location" : job_location})

        #company name
        company_name = "Acumed"
        print('Company Name: ', company_name)
        json_job_dictionary.update({"Company Name" : company_name})

        #job link
        job_link = "http://www.acumed.net/careers"
        print('Job Link: ', job_link)
        json_job_dictionary.update({"Job Link" :  job_link })
        
        #experience
        experience = "3 - 5 yrs"
        print('Experience: ', experience)
        json_job_dictionary.update({"Experience" : experience})

        #hours
        hours = "Full-time"
        print("Hours: ", hours)
        json_job_dictionary.update ({"Hours" : hours})

        #Languages Used
        languages_used = "SAP"
        print("Languages Used: ", languages_used)
        json_job_dictionary.update({"Languages used" : languages_used})

        #salary
        salary = ""
        print("Salary: ", salary)
        json_job_dictionary.update({"Salary" : salary})


        #Create JSON file
        json.dump(json_job_dictionary, json_scrape_file)
        new_object = json.dumps(json_job_dictionary, sort_keys=True, indent=4)
        print('JSON format: ', json.dumps(json_job_dictionary))
        print("\n")


json_scrape_file.close()



    




