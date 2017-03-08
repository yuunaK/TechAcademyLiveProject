from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
import selenium.webdriver.support.select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


#SECTION 1: CREATE WEBDRIVER OBJECT AND GET URL
#Specify target URL
url = "https://career4.successfactors.com/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d"
#Create a webdriver object for the Firefox browser
driver = webdriver.Firefox()
#Use the webdriver object to go to the specified URL
driver.get(url)


'''

#SECTION 2: LOCATE ALL TABLE <TABLE> ELEMENTS
#Test 1: locate the table elements in document and store to table.
#Produces a list.  Items in list can be accessed by index.
tables = driver.find_elements_by_tag_name("table")
#Print the number of items (table elements in URL) in tables.
print (len(tables))


#SECTION 3: LOCATE TABLE ROW <TR> ELEMENTS
#Test 2: locate table row (tr) elements in HTML document.
tableRow = driver.find_elements_by_tag_name("tr")
#print the number of tr elements (list items) in tableRow.
print(len(tableRow))

'''
#Test 3: Another way to accomplish same result as Test 2.
#Use webdriverwait method until to write a lambda function to
#find tr elements with class name "jobResultItem".
JobResultsArray = WebDriverWait(driver, 10, poll_frequency=0.5,ignored_exceptions=None).until(lambda x: x.find_elements_by_class_name("jobResultItem"))
LengthOfJobResultsArray = len(JobResultsArray)

'''

#Test 4: Print the text associated with the first item in the list
#jobResultItem which has an index value of 0.
print(jobResultItem[0].text)
#Test 5: Print the elements in the list jobResultItem.
#There will only be 10 items because the base state of the
#page has only 10 job openings listed and immediately accessible.
print (len(jobResultItem))
#Test 6: Print the text contents of the Job Result items
#on base page.  (A base page is the default state of the
#web page without user input, selection or modification.
for i in range(0, len(jobResultItem), 1):
    print(jobResultItem[i].text)
    print (type(jobResultItem[1].text))

'''

#SECTION 4: LOCATE SELECT <SELECT> ELEMENT AND USE IT TO NAVIGATE TO THE
#OPTION VALUE "50" TO LIST ALL JOBS ON ONE PAGE.
#Test 4: Navigate to the select box and collect options associated with the
#Select element.
listOfOptions = Select(driver.find_element_by_tag_name("select")).options
#Prints the number of options for the Selecct statement.
print(len(listOfOptions))
#Prints each of the option values...
for i in range(0, len(listOfOptions), 1):
      print("Option", i, ":", listOfOptions[i].text)

SelectedOption = Select(driver.find_element_by_tag_name("select")).select_by_value("50")



'''
#SECTION 5: PARSE JOB LIST FOR JOBS IN PORTLAND, OR
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
