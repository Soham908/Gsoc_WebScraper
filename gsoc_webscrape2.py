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
url = "https://summerofcode.withgoogle.com/programs/2022/organizations"
url = "https://summerofcode.withgoogle.com/archive/2018/organizations"
driver.get(url)

elem3 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "name")))
# url = "http://localhost/img"
soup = BeautifulSoup(driver.page_source, 'html.parser')
tags1 = soup.find_all("div", class_="name")

btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
driver.execute_script('arguments[0].click()', btn)

elem3 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "name")))


soup2 = BeautifulSoup(driver.page_source, "html.parser")
tags3 = soup2.find_all("div", class_="name")

for tag in tags1:
    print(tag.text)
for tag in tags3:
    print(tag.text)

