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