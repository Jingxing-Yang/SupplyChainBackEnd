import openpyxl as pyxl
from Container import *
from Vessel import *

"""Pass in the path and file name
Return a list of vessels """
def readFile(fileName):
    wb = pyxl.load_workbook(fileName)
    sheet = wb['Sheet1']
    vesselList = []
    for row in sheet.iter_rows(row_offset=1):
        name = row[1].value
        if name == None:
            break;
        else: 
            outBound = (row[2]=="Outbound")
            cargoType = row[3].value
            shipppingLine = row[5].value
            containerID = row[6].value
            billOfLanding = row[7].value
            containerSize = row[8].value
            loadPort = row[9].value
            unloadPort = row[10].value
            isLocal = (row[11].value=="Local")
            inlandPoint = row[12].value
            voyageNum = row[13].value
            arrivingTerminal = row[14].value
            ariivingTime = row[15].value
            cutOffTime = row[16].value
            departTime = row[17].value
            availTime = row[18].value
            entryMode = row[19].value
            exitMode = row[20].value

            newContainer = Container(name,shipppingLine,containerID,billOfLanding,containerSize,loadPort,unloadPort,isLocal,inlandPoint,arrivingTerminal,availTime,entryMode,exitMode)
            """ when list is empty, simply push a new vessel"""
            if len(vesselList) == 0:
                newVessel = Vessel(name,outBound,isLocal,voyageNum,ariivingTime,cutOffTime,departTime)
                newVessel.upload(newContainer)
                vesselList.append(newVessel)
            else:
                exist = False
                for myVessel in vesselList:
                    if myVessel.name == name:
                        myVessel.upload(newContainer)
                        exist = True
                        break
                if  exist==False:
                    newVessel = Vessel(name,outBound,isLocal,voyageNum,
                    ariivingTime,cutOffTime,departTime)
                    newVessel.upload(newContainer)
                    vesselList.append(newVessel)
    return vesselList


fileName = "resources/test.xlsx"
myList = readFile(fileName)
for myVessel in myList:
    print(myVessel.name)
    for myContainer in myVessel.containers:
        print(myContainer.containerID)

    