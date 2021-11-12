import csv
from collections import Counter

with open('class104/SOCR-HeightWeight.csv', newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]

for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))

m=len(newData)
total=0

for x in newData:
    total=total+x

mean=total/m
print("Mean is: " + str(mean))

newData.sort()
if m%2==0:
    median1=float(newData[m//2])
    median2=float(newData[m//2-1])
    median=(median1+median2)/2
else:
    median=newData[m//2]
    print(m)
print("Median is :"+str(median))

data = Counter(newData)
modeDataForRange = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height,occurrence in data.items():
    if 50< float(height)<60:
        modeDataForRange["50-60"]+=occurrence
    elif 60<float(height)<70:
        modeDataForRange["60-70"]+=occurrence
    elif 70<float(height)<80:
        modeDataForRange["70-80"]+=occurrence

modeRange,modeOccurrence = 0,0

for range, occurrence in modeDataForRange.items():
    if occurrence > modeOccurrence:
        modeRange, modeOccurrence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence
mode = float((modeRange[0] + modeRange[1]) / 2)
print(f"Mode is -> {mode:2f}")