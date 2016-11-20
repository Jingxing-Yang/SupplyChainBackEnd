from datetime import datetime, timedelta
from Vessel import Vessel
from Container import Container

class Port:
    def __init__(self, truckNum, maxtruckNum, vessels):
        self.truckNum = truckNum
        self.maxtruckNum = maxtruckNum
        self.vessels = vessels
        self.capacity_size = 450000
        # truck size = 80
        # unload time for one: 0,5 hour
    def getstatus(self, datetime):
        if self.truckNum>self.maxtruckNum:
            self.status = "full"
        elif self.truckNum>0.6*self.maxtruckNum:
            self.status = "busy"
        else:
            self.status = "usual"
        return self.status
        
    def unload(self, vessel_name):
        for vessel in self.vessels:
            if vessel.name == vessel_name:
                vessel.unload()

class Truck:
    def __init__(self, receivenum, location):
        self.receivenum = receivenum
        self.location = location
        if self.location == "port":
            self.time = datetime.now()
        else:
            self.time = datetime.now()+timedelta(minutes=20)