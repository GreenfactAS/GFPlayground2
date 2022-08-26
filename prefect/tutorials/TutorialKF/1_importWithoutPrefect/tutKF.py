# tutorial by kevin Fortier https://www.youtube.com/watch?v=0IcN117E4Xo

def extract(path):
    with open(path,"r") as f:
        text = f.readline().strip()
        data = [int(i) for i in text.split(",")]
        return data

def transform(data):
    tdata = [i+1 for i in data]
    return tdata

def load(data,path):
    import csv
    with open(path,"w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)

data = extract("values.csv") 
tdata = transform(data)
print("RESULT:", data)
print("TRANSFORMED RESULT:", tdata)
load(tdata,"tvalues.csv")