from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#SECTION ONE: CREATE A WEBDRIVER OBJECT AND DOWNLOAD URL
#Specify target URL
url = "https://career4.successfactors.com/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d"
#Create a webdriver object for the Firefox browser
driver = webdriver.Firefox()
#Use the webdriver object to go to the specified URL
driver.get(url)


#SECTION 2: DETERMINE NUMBER OF JOB LISTING PAGES
#Using WebDriver's find_element method to locate list element
#that contains a span element which INDICATES number of job
#listing pages present.
numberOfPages = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=None).until(lambda a: a.find_element_by_id("33:_pageIndex"))
#Get text from span element inside list element.
numberOfPages = numberOfPages.text
#print(numberOfPages)
#Slice the string to retrieve just number of job listing pages.
#Convert this string to an int
#Verify the conversion using type
#print(type(int(numberOfPages[8])))
numberOfPages = int(numberOfPages[8])



#SECTION 3: WRITE A WHILE LOOP THAT WILL REPEAT THE FOLLOWING ACTIONS:
#(1) GO TO PAGE ONE WITH JOB OPENINGS ON THE ACCELA WEBSITE.
#(2) LOCATE <TR> ELEMENTS WHICH HAVE A CLASS 'jobResultItem'.
#(3) STORE ALL SUCH <TR> ELEMENTS IN AN ARRAY.
#(4) USE A FOR LOOP TO GO OVER EACH ELEMENT IN THE JobResultsArrray.
#(5) FOR EACH ITEM IN THE ARRAY, USE A FOR LOOP TO RETRIEVE AND STORE DATA.
#(6) CHECK DATA TO SEE IF LOCATION IS IN PORTLAND, OR.
#(7) PRINT ALL JOBS IN PORTLAND, OR TO CONSOLE AND JSON FILE.
#(8) GO TO PAGE TWO OF JOB LISTINGS AND REPEAT STEPS (2) - (7).




i = 1
while (i < numberOfPages):

        # LOCATE <TR> ELEMENTS WHICH CONTAIN JOB OPENING INFORMATION AND
        # STORE IN AN ARRAY.
        JobResultsArray = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=None).until(lambda x: x.find_elements_by_class_name("jobResultItem"))
        LengthOfJobResultsArray = len(JobResultsArray)

        for i in range(1, LengthOfJobResultsArray, 1):
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

        #Using WebDriver's By method to locate anchor element
        #paginationAnchor = driver.find_element(By.CLASS_NAME, "paginationArrow.sapIcon")
        paginationAnchor = WebDriverWait(driver, 30, poll_frequency=0.5,ignored_exceptions=None).until(lambda x: x.find_element(By.CLASS_NAME, "paginationArrow.sapIcon"))
        paginationAnchor.click()
        driver.implicitly_wait(10)
        i = i + 1







