from selenium import webdriver
from  bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
import requests
from openpyxl import Workbook
import time
import pandas as pd 

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://in.linkedin.com/jobs/view/software-engineer-golang-at-freecharge-2688620990?refId=yyBQfS69oaCvDTe%2BExrwSw%3D%3D&trackingId=pF3XR7%2FjsirqfPcuVBeVkw%3D%3D&trk=public_jobs_similar-jobs")
time.sleep(2)

see_more=driver.find_element_by_xpath("//button[@class='show-more-less-html__button show-more-less-html__button--more']")
see_more.click()

job_name=driver.find_element_by_xpath("//strong[text()='Title: Software Development Engineer - GoLang']")
print(job_name.text)

location_of_job=driver.find_element_by_xpath("//strong[text()='Location: Mumbai / Remote']")
print(location_of_job.text)

experience_of_job=driver.find_element_by_xpath("//strong[text()='Experience: 5+ Years']")
print(experience_of_job.text)

education_for_job=driver.find_element_by_xpath("//strong[text()='Education: Bachelor’s / Master’s in Software Engineering']")
print(education_for_job.text)

