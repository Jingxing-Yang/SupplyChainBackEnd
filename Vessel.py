from Container import *

"""
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
"""

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
        
    def unload(self, warehouseid):
        for container in self.containers:
            container.location = ("warehouse%i" %warehouseid)
            container.inform()
        self.containers = []

    def show(self):
        print("Vessel #{} size: {}/{}".format(self.name, len(self.containers), self.size))
