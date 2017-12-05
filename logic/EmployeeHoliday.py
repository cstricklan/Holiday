from logic import *
from DBModel import *
import datetime

class EmployeeHoliday():
    def __init__(self, dbeh):
        self.ID = dbeh.ID
        self.EmpID = dbeh.Emp.EmpID
        self.Date = dbeh.Date
        self.Hours = dbeh.Hours
        self.Created = dbemployee.Created
        
    @staticmethod
    def get(id):
        eh = None
        try:
            dbeh = tEmployeeHoliday.get(id)
            eh = EmployeeHolidy(dbeh)
        except Exception as err:
            print("Unable to get Employee Holiday {0}: ".format(id), err)
            
        return eh
        
    @staticmethod
    def new(empid,  date, hours):
        eh = None
        try:
            dbeh = tEmployeeHoliday.create(EmpID = tEmployee.get(EmpID=empID),  Date = date,  Hours=hours)
            eh = EmployeeHoliday(dbeh)
        except Exception as err:
            print("Unable to add employee holiday: {0}  ".format(empID), err)
            
        return eh
        
    def getAllbyUser(Employee):
        Holidays = []
        try:
            dbehs = tEmployeeHoliday.select().where(tEmployeeHoliday.Emp == Employee.GetDBObject())
            
            for dbeh in dbehs:
                holiday = EmployeeHoliday(dbeh)
                Holidays.append(holiday)
        except Exception as err:
            print("Unable to get holidays",  err)
        
        return Holidays
        
    
  
