import csv
data1 = []
data2 = []
with open('./Classes/PRO-129-RefCode-main/final.csv', 'r') as f:
    read = csv.reader(f)
    for i in read :
        data1.append(i)

with open('./Classes/PRO-129-RefCode-main/archive_dataset_sorted1.csv', 'r') as d:
    read = csv.reader(d)
    for i in read :
        data2.append(i)

header1 = data1[0]
planetinfo1 = data1[1:]
header2 = data2[0]
planetinfo2 = data2[1:]

header = header1 + header2

data = []
for p,l in enumerate(planetinfo1):
    data.append(planetinfo1[p]+planetinfo2[p])

with open('data.csv', 'a+') as m:
    writer = csv.writer(m)
    writer.writerow(header)
    writer.writerows(data)