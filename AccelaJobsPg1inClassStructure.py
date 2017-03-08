from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class AccelaOpenPositions():
    def CreateFirefoxWebDriver():
        driver = webdriver.Firefox()
        driver.get("https://career4.successfactors.com/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d")

    def CreateJobResultsArray():
        JobResultsArray = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=None).until(lambda x: x.find_elements_by_class_name("jobResultItem"))
        LengthOfJobResultsArray = len(JobResultsArray)

    def ParseForJobsInPortland():
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

        if JobLocation != "Portland, OR":
            print("Job Title: ", JobTitle)
            print("Job Id: ", JobId)
            print("Job Posting Date: ", JobPostingDate)
            print("Job Location: ", JobLocation)
            print("\n\n")

    






