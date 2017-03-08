from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
import selenium.webdriver.support.select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import requests
import json
from bs4 import BeautifulSoup
import re
import time


#SECTION 1: CREATE WEBDRIVER OBJECT AND GET URL
#Specify target URL
url = "https://career4.successfactors.com/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d"
#Create a webdriver object for the Firefox browser
driver = webdriver.Firefox()
#Use the webdriver object to go to the specified URL
driver.get(url)


#SECTION 2: USE WEBDRIVERWAIT TO LOCATE TABLE ROW ELEMEMT <tr class="jobResultItem">
#Test 3: Another way to accomplish same result as Test 2.
#Use webdriverwait method until to write a lambda function to
#find tr elements with class name "jobResultItem".
JobResultsArray = WebDriverWait(driver, 10, poll_frequency=0.5,ignored_exceptions=None).until(lambda x: x.find_elements_by_class_name("jobResultItem"))
LengthOfJobResultsArray = len(JobResultsArray)


#SECTION 3: LOCATE SELECT <SELECT> ELEMENT AND USE IT TO NAVIGATE TO THE
#OPTION VALUE "50" TO LIST ALL JOBS ON ONE PAGE.
#Test 4: Navigate to the select box and collect options associated with the
#Select element.
listOfOptions = Select(driver.find_element_by_tag_name("select")).options
#Prints the number of options for the Select statement.
print(len(listOfOptions))
#Prints each of the option values...
for i in range(0, len(listOfOptions), 1):
      print("Option", i, ":", listOfOptions[i].text)

SelectedOption = Select(driver.find_element_by_tag_name("select")).select_by_value("50")

try:
    WebDriverWait(driver, 30)
    
    jobArray = driver.find_elements(By.CLASS_NAME, "jobResultItem")
    print(len(jobArray))
    print(jobArray)


    
    

    

    
finally:

      driver.close()

      '''
soup = BeautifulSoup(resource.text, "html.parser")
#When working with Selenium, use select in
      #order to get a list.
      Table1 = soup.select("table")
      Table2 = soup.table.table
      print (type(Table1))
      print (len(Table1))
      print(type(Table2))
      print(Table2)
      


      


      
    tableArray = driver.find_elements_by_tag_name("table")
    JobResultsArray = driver.find_elements(By.CLASS_NAME, "jobResultItem")
    LengthOfJobResultsArray = len(JobResultsArray)
    print(LengthOfJobResultsArray)

    for i in range(0, LengthOfJobResultsArray, 1):
        #Store each item's text value
        JobItem = JobResultsArray[i].text
        #Get length of text string
        JobItemLength = len(JobItem)
        #Strip "Select Action *" from Job Item string
        JobItem = JobItem[0:(JobItemLength - 15)]
        #Job Title
        JobTitle = JobItem[0:(JobItem.index("\n"))]
        #Job Id
        x = JobItem.index("ID")
        x = x + 3
        y = JobItem.index("Posted")
        y = y - 2
        JobId = JobItem[x:y]
        #Job Posting Date
        t = y + 9
        z = y + 18
        JobPostingDate = JobItem[t:z]
        #Job Location
        L1 = z + 4
        L2 = JobItem.rfind("-")
        JobLocation = JobItem[L1:L2]

        if JobLocation == "Portland, OR":
            print("Job Title: ", JobTitle)
            print("Job Id: ", JobId)
            print("Job Location: ", JobLocation)
            print("\n\n")

'''
