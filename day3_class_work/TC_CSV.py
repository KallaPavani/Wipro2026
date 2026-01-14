import csv
with open("Pavani.csv",'w',newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","ID","Age"])
    writer.writerow(["Teena",1,20])
    writer.writerow(["Veena",2,25])
    writer.writerow(["Reena",3,28])
