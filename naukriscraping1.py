import csv
from bs4 import BeautifulSoup
from selenium import webdriver

driver=webdriver.Chrome('/usr/bin/chromium-browser')
with open('naukriscraped.csv','a',newline='') as file:
	writer=csv.writer(file)
	writer.writerow(('JobTitle','CompanyName','KeySkills','Location','ExperienceRequired','Salary','PostedOn'))
	courses=["python",'machinelearning',"fullstack","aws","devops",'angular','react','bigdata','iot','blockchain','dataanalysis','digitalmarketing']
	for course in courses:	
		for i in range(1,5):
			url = 'https://www.naukri.com/'+course+'-jobs-'+str(i)
			driver.get(url)
			soup = BeautifulSoup(driver.page_source, 'html.parser')
			divs=soup.find('div', {'class':'container fl'})
			for div in divs.find_all('div', class_='row '):
				try:
					jobtitle=div.find('li',class_="desig").text
					organisation=div.find('span', class_='org').text
					experience=div.find('span',class_="exp").text
					location=div.find('span', class_='loc').text
					skills=div.find('span', class_='skill').text
					salary=div.find('span', class_='salary').text
					posted=div.find('span', class_='date').text

					if (jobtitle==None) and (organisation == None) and (experience == None) and (location == None) and (skills == None) and (salary == None) and (posted == None):
						continue
					else:
						if location in ['Hyderabad','Bengaluru','Chennai']:
							if 'ago' in posted.split(' '):
								if int(posted.split(' ')[0][0:2])<=15:
									writer.writerow((jobtitle,organisation,skills,location,experience,salary,posted))
							elif 'Ago' in posted.split(' '):
									writer.writerow((jobtitle,organisation,skills,location,experience,salary,posted))
							else:
								writer.writerow((jobtitle,organisation,skills,location,experience,salary,posted))
				except:
					pass
	file.close()
driver.close()