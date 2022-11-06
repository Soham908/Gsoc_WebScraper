import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 5)

driver.get("https://summerofcode.withgoogle.com/programs/2022/organizations")


elem2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "name")))

soup = BeautifulSoup(driver.page_source, 'html.parser')
tags = soup.find_all("div", class_="name")
print(tags)


for tag in tags:
    print(tag.text)

print(len(tags))
