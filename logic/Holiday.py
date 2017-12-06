from logic import *
from DBModel import *
import datetime

class Holiday():
    def __init__(self, dbholiday):
        self.Date = dbholiday.Date
        self.Name = dbholiday.Name
        self.Fixed = dbholiday.Fixed

    @staticmethod
    def GetHolidaysByServiceDate(servicedate):
        Holidays = []
        try:
            dbholidays = tHolidays.select().where(tHolidays.Date >= servicedate)
            for dbholiday in dbholidays:
                h = Holiday(dbholiday)
                Holidays.append(h)
        except Exception as err:
            print("Unable to get Holidays:", err)
            
        return Holidays;
