#Title: Scrape Acquia Careers Webpage
#Course: Live Project
#School: The Tech Academy (Portland, OR)
#Author: Yuuna Kaparti




#Import modules
import urllib.request
import requests
import json
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re



#Download html document and convert into Beautiful Soup object
url ="http://www.acquia.com/careers/open-positions"
resource = requests.get(url)
soup = BeautifulSoup(resource.content, "lxml")

#Create json dictionary
json_job_dictionary = {}
json_scrape_file = open("AcquiaJsonListing", "w")


#Parse View Jobs section of the Document for Jobs in Portland, OR.
view_jobs = soup.find("div", class_="view-jobs")

for i in range(1, len(view_jobs), 2):
    jobSection = view_jobs.contents[i]
    sectionTitle = jobSection.find("h3")
    sectionTitle = sectionTitle.string.strip()
    if sectionTitle != ("Finance" , "G&A Ops" , "Marketing" ,
                        "Products" , "Sales" , "Talent"):
        unorderedList = jobSection.contents[3]
        for j in range(2, len(unorderedList), 2):
            listItem = unorderedList.contents[j]
            location = listItem.contents[3]
            location = location.string.strip()
            if location == "Portland, OR":

                #Job Location
                print("Location: ", location)
                json_job_dictionary.update({"Location" : location})

                #Job Title
                job = listItem.contents[1].string.strip()
                print(job)
                json_job_dictionary.update({"Job Title" : job})

                #Job Id
                job_id = ""
                print("Job Id: ", job_id)
                json_job_dictionary.update({"Job Id" : job_id})

                #Job Posting Date
                date_posted = ""
                print('Job Posting Date: ', date_posted)
                json_job_dictionary.update({"Job Posting Date" : date_posted})

                #Company Name
                company_name = "Acquia"
                print('Company Name: ', company_name)
                json_job_dictionary.update({"Company Name" : company_name})

                #Job Link
                job_link = listItem.contents[1].contents[0].get('href')
                print('http://www.acquia.com'+job_link)
                json_job_dictionary.update({"Job Link" : job_link})

                #Experience
                experience = ""
                print('Experience: ', experience)
                json_job_dictionary.update({"Experience" : experience})

                #Hours
                hours = ""
                print("Hours: ", hours)
                json_job_dictionary.update ({"Hours" : hours})

                #Languages Used
                languages_used = ""
                print("Languages Used: ", languages_used)
                json_job_dictionary.update({"Languages used" : languages_used})

                #Salary
                salary = ""
                print("Salary: ", salary)
                json_job_dictionary.update({"Salary" : salary})

                print('\n')

                #Create JSON file
                json.dump(json_job_dictionary, json_scrape_file)
                new_object = json.dumps(json_job_dictionary, sort_keys=True, indent=4)
                print('JSON format: ', json.dumps(json_job_dictionary))
                print("\n")


json_scrape_file.close()
    


    
    

    
    
