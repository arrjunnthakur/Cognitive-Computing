#Ques 5
import pandas as pd
data=pd.read_csv('file.csv')

data.drop(4,axis=0,inplace=True)  #Row 4 deleted
data.drop("RNO",axis=1,inplace=True) #Column 3 deleted
print(data)

import csv

with open('employees.csv','w',newline='') as file:
  writer=csv.writer(file)
  writer.writerow(["Employee_ID","Name","Department","Age","Salary","Years_of_Experience","Joining_Date","Gender","Bonus","Rating"])
  writer.writerow([101,"Alice","HR",29,50000,4,"2020-03-15","Female",5000,4.5])
  writer.writerow([102,"Bob","IT",34,70000,8,"2017-07-19","Male",7000,4.0])
  writer.writerow([103,"Charlie","IT",41,65000,10,"2013-06-01","Male",6000,3.8])
  writer.writerow([104,"Diana","Marketing",28,55000,3,"2021-02-10","Female",4500,4.7])
  writer.writerow([105,"Edward","Sales",38,60000,12,"2010-11-25","Male",5000,3.5])
