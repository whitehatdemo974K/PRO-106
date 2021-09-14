import plotly.express as px
import csv
import numpy as np
def getDataSource(dataPath):
    marks=[]
    attendance=[]
    with open(dataPath) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"])) 
            attendance.append(float(row["Days Present"]))
    return {"x": marks,"y": attendance}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Student Marks vs Days Present",correlation[0,1])

def setup():
    dataPath="Student Marks vs Days Present.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)

setup()