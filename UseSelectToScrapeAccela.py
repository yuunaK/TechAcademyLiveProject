from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.select


#Specify target URL
url = "https://career4.successfactors.com/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d"
#Create a webdriver object for the Firefox browser
driver = webdriver.Firefox()
#Use the webdriver object to go to the specified URL
driver.get(url)

tables = driver.find_elements_by_tag_name("table")
lenOfTables = len(tables)

innerTable = tables[1]
print(innerTable)

tableRow = driver.find_elements_by_tag_name("tr")
unorderedList = driver.find_element_by_class_name("flatten pagination useIconFonts")
ListItemsPerPage = driver.find_element_by_class_name("per_page")



#Navigate to the select box and collect options associated witht the
#Select element.
listOfOptions = Select(driver.find_element_by_tag_name("select")).options
#Prints the number of options for the Selecct statement.
lenListOfOptions = (len(listOfOptions))
print(lenListOfOptions)
print (type(listOfOptions))
#Prints each of the option values...
for i in range (0, lenListOfOptions, 1):
    print(listOfOptions[i].text)


