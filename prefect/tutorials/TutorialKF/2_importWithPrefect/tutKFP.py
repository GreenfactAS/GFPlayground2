# tutorial by kevin Fortier https://www.youtube.com/watch?v=0IcN117E4Xo
import csv
from urllib.request import DataHandler
from prefect import task, flow

@task
def extract(path):
    with open(path,"r") as f:
        text = f.readline().strip()
        data = [int(i) for i in text.split(",")]
        return data
@task
def transform(data):
    tdata = [i+1 for i in data]
    return tdata

def load(data,path):
    with open(path,"w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)
        return

@flow(name="Hello-world")
def my_flow():
    data = extract("values.csv") 
    tdata = transform(data)
    result = load(tdata,"tvalues.csv")
    data2 = extract("values.csv",upstream_tasks=[result])
    print("RawData",data)
    print("Transformed Data",tdata)

flow.run()