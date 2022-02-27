import sqlite3
import csv
import datetime
import os
folder1 = os.getcwd()

print(datetime.datetime.today().date)

with open(folder1+'/indeedscraped.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        title = str(row[0].strip())
        company_name = str(row[1].strip())
        location = str(row[2].strip())
        description = str(row[3].strip())
        job_type = '1'
        company_description = str(row[1].strip())
        website = str("www."+company_name+".com")
        filled = False
        created_at = datetime.datetime.now().strftime("%m-%d-%Y")
        last_date = (datetime.datetime.now()+datetime.timedelta(days=15)).strftime("%m-%d-%Y")
        user = 1
        conn = sqlite3.connect(folder1+"/db.sqlite3")
        cursor = conn.execute("select * from jobsapp_job")
        for row in cursor.fetchall():
        	print(row)
        conn.execute("""INSERT into jobsapp_job (title,company_name,location,description,type,company_description,website,filled,created_at,last_date) values({},{},str({}),{},{},{},{},{},{},{})""".format(title,str(company_name),location,description,job_type,company_description,website,filled,created_at,last_date))