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

class Warehouse:
    def __init__(self, name):
        self.name = name
        self.capacity = 100
        self.containers = []

    def upload(self, container):
        self.containers.append(container)

    def unload(self, container):
        self.containers.remove(container)

    def show(self):
        print("Warehouse #{} avaliability: {}/{}".format(self.name, len(self.containers), self.capacity))

class Vessel:
    def __init__(self, vessel_name, outbound, capacity, 
               is_local, voyage_num,
               estimated_arrival, cutoff, estimated_departure):
        self.name = vessel_name
        self.outbound = outbound
        if (outbound):
            self.load_port = "Los Angeles"
        else:
            self.unload_port = "Los Angeles"
        self.local = is_local
        self.voyage_num = voyage_num
        self.estimated_arrival = estimated_arrival
        self.cutoff = cutoff
        self.estimated_departure = estimated_departure
        self.capacity = capacity
        self.containers = []

    def upload(self, current_container):
        self.containers.append(current_container)
        return len(current_container)

    def unload(self, warehouse):
        for container in self.containers:
            warehouse.upload(container)

    def show(self):
        print("Vessel #{} capacity: {}/{}".format(self.name, len(self.containers), self.capacity))

class Port:
    def __init__(self, name, vessel, company):
        self.name = "Los Angeles"
        self.vessel = vessel
        self.company = company
