import csv
from tqdm import tqdm

def levelTestFormula():
    count = 0
    file = open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedFormula - Level Test.csv")
    csvFile = list(csv.reader(file))

    for row in csvFile:
        count = count+1
        if row[1] == "Pass" or row[1] == "Fail" or row[1] == "N/A" or row[1] == "To Test" or row[1] == "Retest" or row[1] == "#N/A":
            row[1] = '=IFS(INDIRECT("Setup!B{}")=True,"Pass",INDIRECT("Setup!C{}")=True,"Fail",INDIRECT("Setup!D{}")=True,"N/A",INDIRECT("Setup!E{}")=True,"Retest")'.format(count,count,count,count)
    count=0
    for row in csvFile:
        count = count+1
        if row[2] == "Pass" or row[2] == "Fail" or row[2] == "N/A" or row[2] == "To Test" or row[2] == "Retest" or row[2] == "#N/A":
            row[2] = '=IFS(INDIRECT("Setup!F{}")=True,"Pass",INDIRECT("Setup!G{}")=True,"Fail",INDIRECT("Setup!H{}")=True,"N/A",INDIRECT("Setup!I{}")=True,"Retest")'.format(count,count,count,count)

    with open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedFormula.csv", "w") as output:
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
            row[4] = '=ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!H{}".format(count)+'")))'
            row[5] = '=ISNUMBER(FIND("Fail",INDIRECT("'+"'Level Test'!H{}".format(count)+'")))'
            row[6] = '=ISNUMBER(FIND("N/A",INDIRECT("'+"'Level Test'!H{}".format(count)+'")))'
            row[7] = "=NOT(OR(E{}=True,F{}=True,G{}=True))".format(count, count, count)

    with open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedSetup.csv", "w") as output:
        for row in tqdm(levelFile):
                writer = csv.writer(output, lineterminator='\n')
                writer.writerow(row)
def setupLevel2Count():
    count = 0
    levelCSV = open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedFormula - Setup.csv")
    levelFile = list(csv.reader(levelCSV))

    for row in levelFile:
        count = count+1
        if row[1] == "TRUE" or row[1] == "FALSE":
            #Win
            row[9] = '=AND(INDIRECT("'+"'Level Test'!A{}".format(count-2)+'")=2,ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!G{}".format(count-2)+'"))))'
            #Mac
            row[10] = '=AND(INDIRECT("'+"'Level Test'!A{}".format(count-2)+'")=2,ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!H{}".format(count-2)+'"))))'
            #print('=AND(INDIRECT("'+"'Level Test'!A{}".format(count)+'")=2,ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!H{}".format(count)+'"))))'

    with open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedSetup2.csv", "w") as output:
        for row in tqdm(levelFile):
                writer = csv.writer(output, lineterminator='\n')
                writer.writerow(row)
levelTestFormula()