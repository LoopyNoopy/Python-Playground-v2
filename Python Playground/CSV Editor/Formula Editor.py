import csv
from tqdm import tqdm

def levelTestFormula():
    count = 0
    file = open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\UpdatedCsv.csv")
    csvFile = list(csv.reader(file))

    for row in csvFile:
        count = count+1
        if row[1] == "WIN Pass":
            row[1] = '=Switch(INDIRECT("G{}"),"Success","Pass", "Fail","Fail", "N/A","N/A", "To Test")'.format(count)
        if row[1] == "WIN Fail":
            row[1] = '=Switch(INDIRECT("G{}"),"Success","Pass", "Fail","Fail", "N/A","N/A", "To Test")'.format(count)
    count=0
    for row in csvFile:
        count = count+1
        if row[2] == "Mac Pass":
            row[2] = '=Switch(INDIRECT("H{}"),"Success","Pass", "Fail","Fail", "N/A","N/A", "To Test")'.format(count)
        if row[2] == "Mac Fail":
            row[2] = '=Switch(INDIRECT("H{}"),"Success","Pass", "Fail","Fail", "N/A","N/A", "To Test")'.format(count)

    with open("C:\\Users\\dburgess\\Google Drive\\Work\\Spreadsheets\\Level Tests\\UpdatedFormula.csv", "w") as output:
        for row in tqdm(csvFile):
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(row)

def setupFormula():
    count = 0
    levelCSV = open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedFormula - Level Test.csv")
    levelFile = list(csv.reader(levelCSV))
    
    for row in levelFile:
        count = count+1
        if row[1] == "Pass" or row[1] == "Fail" or row[1] == "N/A" or row[1] == "To Test":
            #Win
            row[0] = '=ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!G{}".format(count)+'")))'
            row[1] = '=ISNUMBER(FIND("Fail",INDIRECT("'+"'Level Test'!G{}".format(count)+'")))'
            row[2] = '=ISNUMBER(FIND("N/A",INDIRECT("'+"'Level Test'!G{}".format(count)+'")))'
            row[3] = "=NOT(OR(C{}=True,B{}=True,A{}=True))".format(count, count, count)
            #Mac
            row[4] = '=ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!G{}".format(count)+'")))'
            row[5] = '=ISNUMBER(FIND("Fail",INDIRECT("'+"'Level Test'!G{}".format(count)+'")))'
            row[6] = '=ISNUMBER(FIND("N/A",INDIRECT("'+"'Level Test'!G{}".format(count)+'")))'
            row[7] = "=NOT(OR(E{}=True,F{}=True,G{}=True))".format(count, count, count)

    with open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedSetup.csv", "w") as output:
        for row in tqdm(levelFile):
                writer = csv.writer(output, lineterminator='\n')
                writer.writerow(row)

setupFormula()