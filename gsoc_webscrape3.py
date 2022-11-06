# import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 5)


# for years 2016 to 2021 (this is separate because these urls are from archives)
def company_name(url):
     driver.get(url)
     elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "name")))
     #first page 50 companies
     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
     tags1 = soup1.find_all("div", class_="name")


     #clicking button first time
     btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
     driver.execute_script('arguments[0].click()', btn)

     #second page 50 companies after button click
     soup2 = BeautifulSoup(driver.page_source, "html.parser")
     tags2 = soup2.find_all("div", class_="name")


     #clicking button second time
     btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
     driver.execute_script('arguments[0].click()', btn)

     #third page 50 companies after button click
     soup3 = BeautifulSoup(driver.page_source, "html.parser")
     tags3 = soup3.find_all("div", class_="name")


     #clicking button third time
     btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
     driver.execute_script('arguments[0].click()', btn)

     #fourth page 50 companies after button click
     soup4 = BeautifulSoup(driver.page_source, "html.parser")
     tags4 = soup4.find_all("div", class_="name")

     lis1 = []

     for tag in tags1:
         lis1.append(tag.text)
     for tag in tags2:
         lis1.append(tag.text)
     for tag in tags3:
         lis1.append(tag.text)
     for tag in tags4:
         lis1.append(tag.text)


     return lis1


#2022 current year function is different because its path is a little bit different
def company_name2022(url):
     driver.get(url)
     elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "name")))
     #first page 50 companies
     soup1 = BeautifulSoup(driver.page_source, 'html.parser')
     tags1 = soup1.find_all("div", class_="name")


     #clicking button first time
     btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
     driver.execute_script('arguments[0].click()', btn)

     #second page 50 companies after button click
     soup2 = BeautifulSoup(driver.page_source, "html.parser")
     tags2 = soup2.find_all("div", class_="name")


     #clicking button second time
     btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
     driver.execute_script('arguments[0].click()', btn)

     #third page 50 companies after button click
     soup3 = BeautifulSoup(driver.page_source, "html.parser")
     tags3 = soup3.find_all("div", class_="name")


     #clicking button third time
     btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
     driver.execute_script('arguments[0].click()', btn)

     #fourth page 50 companies after button click
     soup4 = BeautifulSoup(driver.page_source, "html.parser")
     tags4 = soup4.find_all("div", class_="name")

     lis1 = []

     for tag in tags1:
         lis1.append(tag.text)
     for tag in tags2:
         lis1.append(tag.text)
     for tag in tags3:
         lis1.append(tag.text)
     for tag in tags4:
         lis1.append(tag.text)


     return lis1




url1 = "https://summerofcode.withgoogle.com/programs/2022/organizations"
url2 = "https://summerofcode.withgoogle.com/archive/2021/organizations"
url3 = "https://summerofcode.withgoogle.com/archive/2020/organizations"
url4 = "https://summerofcode.withgoogle.com/archive/2019/organizations"
url5 = "https://summerofcode.withgoogle.com/archive/2018/organizations"
url6 = "https://summerofcode.withgoogle.com/archive/2017/organizations"

df1 = pd.DataFrame(company_name2022(url1))
df2 = pd.DataFrame(company_name(url2))
df3 = pd.DataFrame(company_name(url3))
df4 = pd.DataFrame(company_name(url4))
df5 = pd.DataFrame(company_name(url5))
df6 = pd.DataFrame(company_name(url6))

frames = [df1,df2,df3,df4,df5,df6]
data_log = pd.concat(frames)

print(data_log)
data_log.to_csv("first_file.csv", index=False)
df = pd.read_csv('first_file.csv')


