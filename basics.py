class Container:
    def _init_(self, vesselName, shippingLine, containerID, billOfLanding, size,
               loadPort, unloadPort, isLocal, inlandPoint, arrivingTerminal,
               arrivalTime, cutOffTime, departTime, availTime, entryMode, existMode):
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

class Vessel:
    def _init_(self, vessel_name, outbound, container_quantity, 
               load_port, unload_port, islocal, inland_point, voyage_num, terminal,
               estimated_arrival, cutoff, estimated_departure):
        self.name = vessel_name
        self.outbound = outbound
        self.quantity = container_quantity
        self.load_port = load_port
        self.unload_port = unload_port
        self.local = islocal
        self.inland_point = inland_point
        slef.voyage_num = voyage_num
        self.terminal = terminal
        self.estimated_arrival = estimated_arrival
        self.cutoff = cutoff
        self.estimated_departure = estimated_departure
        self.container = []

        def upload(current_container):
            self.container.append(current_container)

    





