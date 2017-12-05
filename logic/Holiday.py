from logic import *
from DBModel import *
import datetime

class Holiday():
    def __init(self, dbholiday):
        self.Date = dbholiday.Date
        self.Name = dbholiday.Name
        self.Fixed = dbholiday.Fixed

    @staticmethod
    def GetHolidaysByServiceDate(servicedate):
        Holidays = []
        try:
            dbholidays = tHoliday.select().where(Date >= datetime.date(2017, servicedate.month, 1))
            for dbholiday in dbholidays:
                Holidays.append(Holiday(dbholiday))
        except Exception as err:
            print("Unable to get Holidays:", err)
            
        return Holidays;
