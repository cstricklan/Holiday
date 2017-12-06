from logic import *
from DBModel import *
import datetime

class Employee():
    def __init__(self, dbemployee):
        self.EmpID = dbemployee.EmpID
        self.Name = dbemployee.Name
        self.ServiceDate = datetime.datetime.strptime(dbemployee.ServiceDate, "%m/%d/%Y")
        # self.Created = dbemployee.Created
        self.LastViewed = dbemployee.LastViewed
        
    @staticmethod
    def get(id):
        employee = None
        try:
            print("Emp ID: {0}".format(id))
            dbemployee = tEmployee.get(EmpID = id)
            print(dbemployee.ServiceDate)
            employee = Employee(dbemployee)
        except Exception as err:
            print("Unable to get Employee: ", err)
            
        return employee
        
    @staticmethod
    def new(empID,  name,  serviceDate):
        employee = None
        try:
            dbemployee = tEmployee.create(EmpID = empID,  Name=name, ServiceDate = serviceDate)
            employee = Employee(dbemployee)
        except Exception as err:
            print("Unable to add employee: {0}  ".format(empID), err)
            
        return employee
        
    
    def UpdateLastViewed(self):
        try:
            dbemployee = tEmployee.get(EmpID = self.EmpID)
            dbemployee.LastViewed = datetime.datetime.now()
            dbemployee.save()
        except Exception as err:
            print("Unable to Update Employee: ", err)
            
    def GetDBObject(self):
        try:
            dbemployee = tEmployee.get(EmpID = self.EmpID)
            return dbemployee
        except Exception as err:
            print("Error Getting Employee DB object",  err)
            return None
