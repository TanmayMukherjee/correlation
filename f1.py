import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    coffee=[]
    sleep=[]
    with open(dataPath, encoding='utf-8')as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x":coffee,"y":sleep}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Coffee in ml vs sleep in hours: ",correlation[0,1])

def setup():
    dataPath="cups of coffee vs hours of sleep.csv"
    DataSource=getDataSource(dataPath)
    findCorrelation(DataSource)

setup()