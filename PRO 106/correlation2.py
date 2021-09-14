from typing import Sized
import plotly.express as px
import csv
import numpy as np
def getDataSource(dataPath):
    coffee=[]
    sleep=[]
    with open(dataPath) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"])) 
            sleep.append(float(row["sleep in hours"]))
    return {"x": coffee,"y": sleep}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between cups of coffee vs hours of sleep",correlation[0,1])

def setup():
    dataPath="cups of coffee vs hours of sleep.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)

setup()