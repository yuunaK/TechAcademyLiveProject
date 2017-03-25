from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.common.action_chains import ActionChains
import requests


url = "https://jobs.adp.com/job-search-results/?category[]=Technology&location=USA&country=US&radius=200"
driver = webdriver.Firefox()
driver.get(url)
divElement = driver.find_element_by_css_selector("div#widget-jobsearch-results-pages > a:nth-last-child(2)")
print(divElement.text)
divElement.click()


payload = {"GET" : "/i?e=pv&url=https%3A%2F%2Fjobs.adp.com%2Fjob-search-results%2F%3Flocation%3DUSA%26country"\
           "%3DUS%26radius%3D200%26pg%3D3&page=Search%20Jobs%20at%20ADP%20-%20Search%20Careers%"\
           "20at%20ADP%20-%20Search%20ADP%20Jobs%20by%20Location%20%26%20Keyword&tv=js-2.4.3&tna=co&aid=adp"\
           "&p=web&tz=UTC&lang=en-US&cs=utf-8&f_java=1&res=1364x768&cd=16&cookie=1&eid=df539b96-3a51-4950-"\
           "8707-46bfcc8f5844&dtm=1489948336118&vp=1207x544&ds=1191x2373&vid=1&duid=23e2211b73def1ca&fp="\
           "2743786749&cx=eyJzY2hlbWEiOiJpZ2x1OmNvbS5zbm93cGxvd2FuYWx5dGljcy5zbm93cGxvdy9jb250ZXh0cy9qc29u"\
           "c2NoZW1hLzEtMC0wIiwiZGF0YSI6W3sic2NoZW1hIjoiaWdsdTpjb20uZ29vZ2xlLmFuYWx5dGljcy9jb29raWVzL2pzb25z"\
           "Y2hlbWEvMS0wLTAiLCJkYXRhIjp7Il9nYSI6IkdBMS4yLjIxNDQ2MTc0NDMuMTQ4OTk0NzUyMyJ9fV19 HTTP/1.1",
           "Accept" : "image/png, image/svg+xml, image/*;q=0.8, */*;q=0.5",
           "Referer" : " https://jobs.adp.com/job-search-results/?location=USA&country=US&radius=200&pg=3",
           "Accept-Language" : "en-US",
           "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
           "Host" : "d.hodes.com",
           "Connection" : "close",
           "Cookie" : "sp=34e1aadc-be5a-4247-909d-0c037e7d0cd3"
        }

RequestObject = requests.get(url, params=payload)



