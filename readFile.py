import openpyxl as pyxl

class Container:
    def __init__(self, vesselName, shippingLine, containerID, billOfLanding, size,
                 loadPort, unloadPort, isLocal, inlandPoint, arrivingTerminal,
                 entryMode, exitMode, is_avaliable):
        self.vesselName = vesselName
        self.shippingLine = shippingLine
        self.containerID = containerID
        self.billOfLanding = billOfLanding
        self.size = size
        self.loadPort = loadPort
        self.unloadPort = unloadPort
        self.isLocal = isLocal
        self.arrivingTerminal = arrivingTerminal
        self.inlandPoint = inlandPoint
        self.entryMode = entryMode
        self.existMode = exitMode
        self.avaliable = is_avaliable
        self.location = ""

    def show(self):
        print("Container #{} location: {}".format(self.containerID, self.location))

class Warehouse:
    # only for trucks
    def __init__(self, name):
        self.name = name
        self.size = 100
        self.containers = []

    def upload(self, container):
        self.containers.append(container)
        container.location = "house"

    def unload(self, container):
        self.containers.remove(container)
        container.location = "truck"

    def show(self):
        print("Warehouse #{} avaliability: {}/{}".format(self.name, len(self.containers), self.size))

class Vessel:
    def __init__(self, vessel_name, outbound,  
               is_local, voyage_num,
               estimated_arrival, cutoff, estimated_departure):
        self.name = vessel_name
        self.outbound = outbound
        if outbound:
            self.load_port = "Los Angeles"
        else:
            self.unload_port = "Los Angeles"
        self.local = is_local
        self.voyage_num = voyage_num
        self.estimated_arrival = estimated_arrival
        self.cutoff = cutoff
        self.estimated_departure = estimated_departure
        self.size = 0
        self.containers = []

    def upload(self, current_container):
        self.containers.append(current_container)
        current_container.location = "vessel"

    def unload(self, warehouse):
        for container in self.containers:
            warehouse.upload(container)

    def show(self):
        print("Vessel #{} size: {}/{}".format(self.name, len(self.containers), self.size))

class Port:
    def __init__(self, name, vessel, warehouse):
        self.name = "Los Angeles"
        self.vessel = vessel
        self.warehouse = warehouse
        self.car_capacity = 100
        self.current_capacity = 0
        self.estimated_capacity = 0

    def load_operation_time(self):
        self.estimated_depart_time.append()
        self.estimated_arrival_time.append()
        self.estimated_curoff_time.append()

    def unload(self, estimated_depart_time):
        for operation in estimated_depart_time:
            if time == operation:
                # add stuff here
                pass

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

    