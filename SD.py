import math
import csv
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
data=filedata[0]
#finding Mean
def Mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int (x)   
    mean=total/n
    return mean
squaredlist=[]
for number in data:
    a=int (number)-Mean(data)
    a=a**2        
    squaredlist.append(a)  
#SUM OF SQUARES
SUM=0
for i in squaredlist:
    SUM=SUM+i    
result=SUM/(len(data)-1)
sd=math.sqrt(result)
print(sd)