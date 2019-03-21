import csv
from tqdm import tqdm

count = 0
file = open("C:\\Users\\dburgess\\Google Drive\\Work\\Spreadsheets\\Level Tests\\LevelTest.csv")
csvFile = list(csv.reader(file))

for row in csvFile:
    count = count+1
    if row[0] == "WinPass":
        row[0] = '=if(IFERROR(search("Success",INDIRECT("G{}"))>0,0),"WIN Pass","WIN Fail")'.format(count)

count=0
for row in csvFile:
    count = count+1
    if row[1] == "MacPass":
        row[1] = '=if(IFERROR(search("Success",INDIRECT("H{}"))>0,0),"Mac Pass","Mac Fail")'.format(count)

with open("UpdatedCsv.csv", "w") as output:
    for row in tqdm(csvFile):
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(row)
