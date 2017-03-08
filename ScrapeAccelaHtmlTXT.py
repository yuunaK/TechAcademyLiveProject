from bs4 import BeautifulSoup

AccelaFile = open("C://Program Files/Python35/Python Projects/AccelaOpenPositions.html")
AccelaFile = AccelaFile.read()
AccelaSoup = BeautifulSoup(AccelaFile, "lxml")
type(AccelaSoup)
                  
