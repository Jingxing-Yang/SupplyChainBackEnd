from datetime import datetime, timedelta
from Container import *
from Vessel import *

class Port:
    def __init__(self, truckNum, maxtruckNum, vessels)
        self.truckNum = truckNum
        self.maxtruckNum = maxtruckNum
        self.vessels[] = vessels
        
    def getstatus(self, datetime):
        if self.truckNum>self.maxtruckNum:
            self.status = "full"
        elif self.truckNum>0.6*self.maxtruckNum:
            self.status = "busy"
        else:
            self.status = "vacant"
        return self.status
        
    def work(self, )
        for vessel in self.vessels:
            vessel.unload()
            
        
class Truck:
    def __init__(self, receivenum, location)
        self.receivenum = receivenum
        self.location = location
        if self.location == "port":
            self.time = datetime.now()
        else:
            self.time = datetime.now()+timedelta(minutes=20)