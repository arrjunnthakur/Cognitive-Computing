import csv

with open('file.csv','w',newline='') as file:
  writer=csv.writer(file)
  writer.writerow(["SNO","NAME","RNO"])
  writer.writerow([1,"abc",11])
  writer.writerow([2,"def",12])
  writer.writerow([3,"ghi",13])
  writer.writerow([4,"jkl",14])
  writer.writerow([5,"mno",15])
  writer.writerow([6,"pqr",16])

import pandas as pd
pd.read_csv('file.csv',nrows=5)