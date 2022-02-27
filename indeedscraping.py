# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
with open('indeedscraped.csv','a',newline="") as file:
	writer=csv.writer(file)
	writer.writerow(('JobTitle','CompanyName','Location','Summary','Salary','PostedOn'))
	courses=["python",'machine learning',"full stack","aws","devops",'angular','react','big data','iot','block chain','data analysis','digital marketing']
	for course in courses:
		course=course.replace(' ','+')
		for i in ['0','10','20','30','40']:
			url='https://www.indeed.co.in/jobs?q='+course+'&l=india&start='+str(i)
			driver.get(url)
			soup = BeautifulSoup(driver.page_source, 'html.parser')
			td=soup.find('td',id="resultsCol")
			div=td.find_all('div',class_="jobsearch-SerpJobCard row result clickcard")
			for i in div:
				jobtitle=i.find('a').text
				company=i.find('span',class_="company").text.strip()
				if i.find('div',class_="sjcl")==None:
					location=i.find('span',class_="location").text.strip()
				else:
					location=i.find('div',class_='location').text.strip()

				if i.find('div',class_='salarySnippet')==None:
					salary="Not Disclosed"
				else:
					salary=i.find('div',class_='salarySnippet').text.strip()
				summary=i.find('span',class_="summary").text.strip()
				try:
					postedon=i.find('span',class_='date').text.strip()
				except:
					postedon='Not Mentioned'
				
				if (jobtitle==None) and (company==None) and (location==None) and (salary==None) and (summary==None) and (postedon==None):
					continue
				else:
					writer.writerow((jobtitle,company,location,summary,salary,postedon))

	file.close()
driver.close()				