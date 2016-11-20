"""THe class for container. It store all the information for a container"""
class Container:
	def _init_(self,vesselName,shippingLine,containerID,billOfLanding,size,
			loadPort,unloadPort,isLocal,inlandPoint,arrivingTerminal,
			arrivalTime,cutOffTime,departTime,availTime,entryMode,existMode):
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
		self.arrivalTime = arrivalTime
		self.cutOffTime = cutOffTime
		self.departTime = departTime
		self.availTime = availTime
		self.entryMode = entryMode
		self.existMode = existMode
        self.avaliable = is_avaliable
        self.location = ""
        
    def show(self):
        print("Container #{} location: {}".format(self.containerID, self.location))
