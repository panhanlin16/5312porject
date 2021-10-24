import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
excel_path="D:/111hk/py/pj/"
excel_name="train.csv"
process_excel_name="processTrain.csv"
data = pd.read_csv(excel_path+excel_name)

for i in range(0,len(data)):
   if data.iloc[i,1]=="Male":
      data.iloc[i,1]=1
   else:
        data.iloc[i,1]=0
   num=data.iloc[i,3][-3:]
   num=int(num)-250
   data.iloc[i,3]=num
   if data.iloc[i,4]=="Entrepreneur":
       data.iloc[i,4]=1
   elif data.iloc[i,4]=="Salaried":
       data.iloc[i,4]=2
   elif data.iloc[i,4]=="Self_Employed":
       data.iloc[i,4]=3
   else:
       data.iloc[i,4]=4
   num1=data.iloc[i,5][-1:]
   num1=int(num1)
   data.iloc[i,5]=num1
   if pd.isna(data.iloc[i,7]):
       data.iloc[i,7]=0
   else:
       if data.iloc[i,7]=="Yes":
           data.iloc[i,7]=1
       else:
           data.iloc[i,7]=2 
   if data.iloc[i,9]=="Yes":
        data.iloc[i,9]=1
   else:
        data.iloc[i,9]=0 
   if i%100==0:
       print(i/100)

data.to_csv(excel_path+process_excel_name)