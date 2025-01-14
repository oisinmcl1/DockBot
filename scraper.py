import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# start a session
session = requests.Session()

# login urls and info
email = os.environ['EMAIL']
password = os.environ['PW']
loginUrl = "https://login.esbnetworks.ie/"
info = {"username:": email, "password:": password}

# send post to login
response = session.post(loginUrl, data=info)

if response.ok:
  print("Successful login")
else:
  print(f"Failed login: {response.status_code}")
