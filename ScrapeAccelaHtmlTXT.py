from bs4 import BeautifulSoup
import requests

url = "https://career4.successfactors.com/career?company=accela&career_ns=job_listing_summary&navBarLevel=JOB_SEARCH&_s.crb=qr%2fB9Umk1C5fQeUZS9x2%2fMkRHEg%3d"
ResponseObject = requests.get(url, timeout=0.30)

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

    
