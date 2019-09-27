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
    return()

def setupFormula():
    count = 0
    levelCSV = open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedFormula - Level Test.csv")
    levelFile = list(csv.reader(levelCSV))
    
    for row in levelFile:
        count = count+1
        if row[1] == "Pass" or row[1] == "Fail" or row[1] == "N/A" or row[1] == "To Test":
            #Mac
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
    return()

def setupLevel2Count():
    count = 0
    levelCSV = open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedFormula - Setup.csv")
    levelFile = list(csv.reader(levelCSV))

    for row in levelFile:
        count = count+1
        if row[1] == "TRUE" or row[1] == "FALSE":
            #Mac
            row[9] = '=AND(INDIRECT("'+"'Level Test'!A{}".format(count-2)+'")=2,ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!G{}".format(count-2)+'"))))'
            #Mac
            row[10] = '=AND(INDIRECT("'+"'Level Test'!A{}".format(count-2)+'")=2,ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!H{}".format(count-2)+'"))))'
            #print('=AND(INDIRECT("'+"'Level Test'!A{}".format(count)+'")=2,ISNUMBER(FIND("Success",INDIRECT("'+"'Level Test'!H{}".format(count)+'"))))'

    with open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\UpdatedSetup2.csv", "w") as output:
        for row in tqdm(levelFile):
                writer = csv.writer(output, lineterminator='\n')
                writer.writerow(row)
    return()

def ogFormula(fileName): #Formula for generating the original style rt tests
    count = 1
    file = open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\Original CSV files\\{}".format(fileName))
    csvFile = list(csv.reader(file))
    file.close()
    for row in tqdm(csvFile):
        if not row[1].find("L") != -1: #Checks to see its only adding the formula to cells which are tests and not titles
            row[2] ='=if(iserror(search("L",INDIRECT("$B{0}"))),if(not(iserror(search("Success",INDIRECT("$H{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$H{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$J{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$J{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$L{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$L{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$N{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$N{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$P{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$P{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$R{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$R{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$T{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$T{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$V{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$V{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$X{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$X{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$Z{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$Z{0}")))),"Win Fail","Win RT")))))))))))))))))))),"")'.format(count)
            row[3] ='=if(iserror(search("L",INDIRECT("$B{0}"))),if(not(iserror(search("Success",INDIRECT("$I{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$I{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$K{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$K{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$M{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$M{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$O{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$O{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$Q{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$Q{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$S{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$S{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$U{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$U{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$W{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$W{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$Y{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$Y{0}")))),"Mac Fail",if(not(iserror(search("Success",INDIRECT("$AA{0}")))),"Mac Pass",if(not(iserror(search("Fail",INDIRECT("$AA{0}")))),"Mac Fail","Mac RT")))))))))))))))))))),"")'.format(count)
        count = count+1
    with open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\Updated CSV files\\Updated {}".format(fileName), "w") as output:
        for row in csvFile:
                writer = csv.writer(output, lineterminator='\n')
                writer.writerow(row)
    return()

def ogFormulaPCOnly(fileName):
    count = 1
    file = open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\Original CSV files\\{}".format(fileName))
    csvFile = list(csv.reader(file))
    file.close()
    for row in tqdm(csvFile):
        if not row[1].find("L") != -1: #Checks to see its only adding the formula to cells which are tests and not titles
            row[2] ='=if(iserror(search("L",INDIRECT("$B{0}"))),if(not(iserror(search("Success",INDIRECT("$G{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$G{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$H{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$H{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$I{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$I{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$J{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$J{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$K{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$K{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$L{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$L{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$M{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$M{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$N{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$N{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$O{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$O{0}")))),"Win Fail",if(not(iserror(search("Success",INDIRECT("$P{0}")))),"Win Pass",if(not(iserror(search("Fail",INDIRECT("$P{0}")))),"Win Fail","Win RT")))))))))))))))))))),"")'.format(count)
        count = count+1
    with open("C:\\Users\\dburgess\\Documents\\GitHub\\Python Playground\\Python Playground\\CSV Editor\\Updated CSV files\\Updated {}".format(fileName), "w") as output:
        for row in csvFile:
                writer = csv.writer(output, lineterminator='\n')
                writer.writerow(row)
    return()

ogFormula("[DLC Connect] Level Testing Document - SC Settings.csv")
ogFormula("[DLC Connect] Level Testing Document - AI CC 2017.csv")
ogFormula("[DLC Connect] Level Testing Document - AI CC 2018.csv")
ogFormula("[DLC Connect] Level Testing Document - AI CC 2019.csv")
ogFormulaPCOnly("[DLC Connect] Level Testing Document - CD 2017.csv")
ogFormulaPCOnly("[DLC Connect] Level Testing Document - CD 2018.csv")
ogFormulaPCOnly("[DLC Connect] Level Testing Document - CD 2019.csv")
