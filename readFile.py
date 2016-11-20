import openpyxl as pyxl
from Port import Port
from Vessel import Vessel
from Container import Container

from twilio.rest import TwilioRestClient

ACCOUNT_SID = "AC289f7d8e9decded34363ffa03b469cb8" 
AUTH_TOKEN = "74083a3f504a0e4f2d912be47445228e" 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def notify(text):
    client.messages.create(   
        body=text,  # Message body, if any
        to="+12132040803",
        from_="+14159694232",)

def readFile(fileName):
    wb = pyxl.load_workbook(fileName)
    sheet = wb["cargo data"]
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

            newContainer = Container(name, shipppingLine, containerID, billOfLanding, containerSize,
                                     loadPort, unloadPort, isLocal, inlandPoint, arrivingTerminal,
                                     availTime, entryMode, exitMode)
            """ when list is empty, simply push a new vessel"""
            if len(vesselList) == 0:
                newVessel = Vessel(name, outBound, isLocal, voyageNum,
                                   ariivingTime, cutOffTime, departTime)
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
                    newVessel = Vessel(name, outBound, isLocal, voyageNum,
                                       ariivingTime, cutOffTime, departTime)
                    newVessel.upload(newContainer)
                    vesselList.append(newVessel)
    return vesselList

def get_container(landing_num, myList):
    info = []
    for myVessel in myList:
        for myContainer in myVessel.containers:
            if myContainer.billOfLanding == landing_num:
                info.append(myVessel)
                info.append(myContainer)
                return info
# load data
fileName = "resources/HackathonDatapostarrival.xlsx"
print("Loading data...")

myList = readFile(fileName)
for myVessel in myList:
    count = 0
    for myContainer in myVessel.containers:
        temp = int(myContainer.size)
        count += temp
    myContainer.size = count

LA = Port(0, 5625, myList)
LA.unload("Sorcerer's Stone")
# interact with user
correct = 1
while (correct):
    user_type = raw_input("Please enter your user type (Company/Port/Truck): ") 
    if (user_type == "Company" or user_type == "Port" or user_type == "Truck"):
        correct = 0
    else:
        notify("wrong: please enter again ")
        correct = 1

# notify("Hello dear #{} user: what would you like to do? ".format(user_type))
action = raw_input("Hello dear #{} user: what would you like to do? ".format(user_type))
if (action == "track"):
    # notify("Please give me the Bill of Lading")
    billOfLanding = raw_input("Please give me the Bill of Lading: ")
    print("Fetching...")
    myContainer = get_container(billOfLanding, myList)
    print("Your cargo is in container #{} is now on {}".format(myContainer[1].containerID, myContainer[1].location))
    if (myContainer[1].location == "vessel"):
        print("status: {}".format(myContainer[0].estimated_arrival))
    # notify("Your cargo is in container #{} is now on {}".format(myContainer.containerID, myContainer.location))
    elif(myContainer[1].location == "port"):
        # need to show time
        plan1 = "6 hours later"
        plan2 = "12 hours later"
        plan3 = "24 hours later"
        choice = raw_input("Please pick a time from the following to pick up your cargo: \n{}\n{}\n{} \
                              (please use 1, 2, or 3 to indicate option)".format(plan1, plan2, plan3))
        
