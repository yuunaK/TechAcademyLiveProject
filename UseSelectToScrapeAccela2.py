#Title: Scrape the Accela Website For Open Positions
#Course: Live Project
#School: The Tech Academy (Portland, OR)
#Author: Yuuna Kaparti

#Program Summary:
#With static webpages, it is possible to use Python and Beautiful
#Soup to harvest data from a site. Beautiful Soup relies on
#locating elements using the DOM tree.
#You cannot use these methods when trying to scrape a dynamic
#webpage. You have to develop a different model to accomplish
#this task.

#In order to scrape the Accela Website for open positions in
#Portland, OR, I had to learn how to use Selenium to locate
#elements as well as find information located on a server.

#The tools and technologies I used included Python 3.5 (64
#bit), Selenium, and Web Proxy.

#First, we have to download either Firefox or Chrome.
#In theory we could have also downloaded PhantomJS if
#you wanted to have a displayless browser.

#Second, we have to install driver associated with the
#browser - in my case, I downloaded geckodriver.

#Third, go to command prompt window, navigate to the C:
#and pip install selenium.

#Now you are ready to write the program.
#Step 1:
#Specify target URL, create a Firefox webdriver object
#and get the URL (i.e. request the web page).

#Step 2:
#Wait for page to load. Use Selenium Web Driver methods
#to locate elements.  What is interesting about these
#methods is that they do not seem as DOM dependent.
#In other words, you do not have to use a container
#or parent element to find children or descendant elements.
#You can directly access an element (or elements) using
#tag name, class name, id, etc.

#Step 3:
#If data that is required is readily available at this
#point, go ahead and process the data.
#If you need to interact with the web page to get the
#information you need, you will need to use webdriver's
#support libraries to find methods to help you execute
#any desired tasks.

#Step 4:
#Locating elements on the new/ reloaded / refreshed
#page.
#Option 1: Wait for page to fully load, locate elements
#and proceed as before.
#Option 2: Switch to a new page, locate elements, etc.
#These two options work if the the information is accessible
#on the client device.
#If the infomation is on the server, you will need to
#replicate JavaScript functions on the server to access
#the data. This is where the Web Proxy and requests.post
#method fill a critical role.  Using web proxy, you can get
#post information. Next, put post infomation in dictionary
#format. Feed this into the requests.post method(url,
#postDictionary).  At this point, you can use webdriver
#methods to locate elements again.

#Step 5:
#Put processed data into JSON format.


#To Wrap Up:
#When web scraping with Python,
#we need to get the web document. To do this, we can
#use requests.get. Alternatively, we can use selenium
#webdriver to do this same task when working with dynamic
#webpages - webpages that are wrapped in JavaScript and Ajax.
#To locate elements we can use Beautiful Soup or
#Selenium Webdriver. Each will have its own set of methods.
#Each uses different models to access elements.  Selenium
#locates elements fairly directly, although the XPath method
#may traverse the Document Object Tree.  With Beautiful Soup,
#elements are located using the DOM tree.

#The difficulty I encountered while attempting
#to scrape the Accela website was getting past the Selenium
#Webdriver event that refreshes the page.

#As long as I continued to use models that assumed an object on
#the client device, I was not able to scrape the document. Whether it
#was Beautiful Soup or Selenium Webdriver, I was not able to scrape
#the website.  If it was the case that neither Selenium Webdriver
#nor Beautiful Soup could be used successfully to get the desired
#information, I had to change my model from (1)client device to server
#and (2) I needed to shift focus from Beautiful Soup and Selenium Webdriver
#to Python.  Lastly, I had to take into account that the webpage was being
#refreshed using scripts embeded in the HTML. These scripts redirect
#the client request to another program which then furnishes the page
#with the requested information.

#This is where Python's requests library and the use of a Web Proxy come
#into the picture. The Web Proxy is a program that sits between the client
#device and the server and monitors the instructions being passed between the
#application on the client device and the server side component of the
#application. Using a web proxy application, such as Burp Suite (the free
#download version) it is possible to observe the instructions that are exchanged
#as you perform different actions on the webpage.  You can copy
#and paste information the client component of the application is sending
#to the server into your program using requests.post.  This will allow
#your program to access data visible on the screen. This implies that
#for dynamic webpages, data visible on the screen remains on the server.
#Beautiful Soup can scrape information from the page which teh server sends
#to the client device.  Selenium Webdriver works with the document object
#on the server. The use of requests.post allows the program to access
#the information being displayed on the screen via its built-in capacity
#to handle redirection. This will refresh the object on the server to reflect
#page visible on the screen. At this point, you can scrape the document
#object on the server using Selenium Webdriver methods.



#Import Modules
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
import re



#SECTION 1: CREATE WEBDRIVER OBJECT AND GET URL
#Specify target URL
url = "https://career4.successfactors.com/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d"
#Create a webdriver object for the Firefox browser
driver = webdriver.Firefox()
#Use the webdriver object to go to the specified URL
driver.get(url)

#SECTION 1A: CREATE (SET-UP)JSON DICTIONARY AND AN EXTERNAL FILE
#TO WHICH WE WILL WRITE THE JSON DICTIONARY.
json_job_dictionary = {}
json_scrape_file = open("AccelaJsonListing", "w")


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
#Navigates to dropbox to select "50" in order to display 50 job listings per page.
SelectedOption = Select(driver.find_element_by_tag_name("select")).select_by_value("50")



#SECTION 4: WE PARSE THE JOB LISTINGS FOR JOBS IN PORTLAND, OR.
#USE SELENIUM WITH THE PYTHON REQUESTS LIBRARY AND WEB PROXY POST
#INFORMATION IN ORDER TO HANDLE A SITUATION WHERE JOB LISTINGS ARE STORED
#ON THE SERVER.

try:

      #This is a dictionary. Python Dictionary syntax: {'key' : 'value', 'key' : 'value'}
      #This information in the dictionary is obtained by using Web Proxy and looking at
      #data produced by JavaScript functions that are automatically executing when the
      #page is displayed.
      
      payload = {'POST' : "/xi/ajax/remoting/call/plaincall/careerJobSearchControllerProxy.search.dwr HTTP/1.1",
               'Host' : 'career4.successfactors.com' ,
               'Accept' : "*/*",
               'viewId' : "/ui/rcmcareer/pages/careersite/career.jsp.xhtml",
               'Accept-Encoding' : "gzip, deflate" ,
               'Accept-Language' : "en-us",
               'Content-Type' : "text/plain",
               'Origin' : "https://career4.successfactors.com",
               'X-Ajax-Token' : "tKsdT%2fvpdrnWDCWhIeZM76Xl83M%3d" ,
               'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
               'Referer' : "https://career4.successfactors.com/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d",
               'Content-Length' : "753",
               'Connection' : "close",
               'Cookie' : "BIGipServerPMOD-CAREER4.SUCCESSFACTORS.COM-80=3424322570.20480.0000; JSESSIONID=55C33770949CC8ED5A33A7163F5D97B8.pc4bcar13t",

               'callCount' :'1',
               'page' :'/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d',
               'httpSessionId' : 'scriptSessionId=80A8BD291A8E635A37D57F13E5D1F423216',
               'c0-scriptName' : 'careerJobSearchControllerProxy',
               'c0-methodName' : 'search',
               'c0-id' : '0',
               'c0-e2' : 'number:3',
               'c0-e3' : 'number:20',
               'c0-e4' : 'boolean:false',
               '0-e5' :  'number:50',
               'c0-e6' : 'number:11',
               'c0-e7' : 'number:39',
               'c0-e1' : 'Object_Object:{currentPage:reference:c0-e2, endRow:reference:c0-e3, highPaginationForWorkbench:reference:c0-e4,pageSize:reference:c0-e5, startRow:reference:c0-e6, totalCount:reference:c0-e7}',
               'c0-e8' : 'string:JOB_POSTING_DATE',
               'c0-e9' : 'string:DESC',
               'c0-param0' : 'Object_Object:{pagination:reference:c0-e1, sortByColumn:reference:c0-e8, sortOrder:reference:c0-e9}',
               'batchId' : '2'
               }

      ResponseObject = requests.post(url, data=payload)
      JobResultsArray = driver.find_elements_by_class_name("jobResultItem")
      LengthOfJobResultsArray = len(JobResultsArray)
      print(LengthOfJobResultsArray)
      JobLinkArray = driver.find_elements_by_class_name("jobTitle")
      


      for i in range(0, LengthOfJobResultsArray, 1):
            JobItem = JobResultsArray[i].text
            JobItemLength = len(JobItem)
            #print(JobItemLength)
            JobItem = JobItem[0: (JobItemLength - 15)]
            #print(JobItem)
            #Job Title
            JobTitle = JobItem[0:(JobItem.index("\n"))]
            #print(JobTitle)
            #Job Item Id
            x = JobItem.index("ID")
            x = x + 3
            y = JobItem.index("Posted")
            y = y-2
            JobId = JobItem[x:y]
            #print(JobId)
            #Job Posting Date
            t = y + 9
            z = y + 18
            JobPostingDate = JobItem[t:z]
            #print(JobPostingDate)
            #Job Location
            L1 = z + 4
            L2 = JobItem.rfind("-")
            JobLocation = JobItem[L1:L2]
            #print(JobLocation)
            #Job Link
            JobLink = JobLinkArray[i].get_attribute("href")


            

            #Use regular expression methods to compare job locations
            #You cannot use string comparison - doesn't work in this
            #situation. It may have something to do with the fact that
            #this infomation is outside a "python" language environment.
            LocationMatch = re.search("Portland, OR", JobLocation)
            if LocationMatch:
                  #Job Title
                  print("Job Title: ", JobTitle)
                  json_job_dictionary.update({"Job Title" : JobTitle})
                  #Job Id
                  print("Job Id: ", JobId)
                  json_job_dictionary.update({"Job Id" : JobId})
                  #Job Posting Date
                  print("Job Posting Date: ", JobPostingDate)
                  json_job_dictionary.update({"Job Posting Date" : JobPostingDate})
                  #Job Location
                  print("Job Location: ", JobLocation)
                  json_job_dictionary.update({"Job Location" : JobLocation})
                  #Company Name
                  CompanyName = "Accela"
                  print("Company Name: ", CompanyName)
                  json_job_dictionary.update({"Company Name" : CompanyName})
                  #Job Link
                  print("Job Link: ", JobLink)
                  json_job_dictionary.update({"Job Link" : JobLink})
                  #Experience
                  Experience = ""
                  print("Experience: ", Experience)
                  json_job_dictionary.update({"Experience" : Experience})
                  #Hours
                  Hours = ""
                  print("Hours: ", Hours)
                  json_job_dictionary.update({"Hours" : Hours})
                  #Languages Used
                  Languages_Used = ""
                  print("Languages Used: ", Languages_Used)
                  json_job_dictionary.update({"Languages Used" : Languages_Used})
                  #Salary
                  Salary = ""
                  print("Salary: ", Salary)
                  json_job_dictionary.update({"Salary" : Salary})

                  print("\n")

                  #Write the json_job_dictionary, internal to the program,
                  #to json_scrape_file, the internal handle for the
                  #the external file AccelaJsonListing.
                  json.dump(json_job_dictionary, json_scrape_file)

                  #Create a json.dumps variable. Print job data in JSON format to console
                  new_object = json.dumps(json_job_dictionary, sort_keys=True)
                  print("JSON format: ", new_object)
                  print("\n\n")
finally:

      driver.close()
      driver.quit()
      json_scrape_file.close()

      
      
