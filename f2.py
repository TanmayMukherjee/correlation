import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    marks=[]
    dayspresent=[]
    with open(dataPath, encoding='utf-8')as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
             marks.append(float(row["Marks In Percentage"]))
             dayspresent.append(float(row["Days Present"]))
    return {"x": marks,"y":dayspresent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Marks In Percentage vs Days Present: ",correlation[0,1])

def setup():
    dataPath="Student Marks vs Days Present.csv"
    DataSource=getDataSource(dataPath)
    findCorrelation(DataSource)

setup()