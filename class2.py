import csv
from re import X
with open("class2.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)   
totalmarks=0
totalentry=len(filedata)
for newdata in filedata:
    totalmarks+=float(newdata[1])
Mean=totalmarks/totalentry
print("Mean is ="+str(Mean))    
import pandas as pd 
import plotly.express as ps
df=pd.read_csv("class2.csv")
fig=ps.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[
    dict(type="line",y0=Mean,y1=Mean,x0=0,x1=totalentry)
])
fig.update_yaxes(rangemode="tozero")
fig.show()