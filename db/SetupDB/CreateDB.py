from DBModel import  *
import datetime

class CreateDB():
    def __init__(self):
        db.connect()
        
    def CreateTables(self):
        db.create_tables([tEmployee,  tHolidays,  tEmployeeHoliday])

    def filldata_Holidays(self):
        tHolidays.create(Name = 'New Years',  Date=datetime.date(2017, 01, 01), Fixed=True)
        tHolidays.create(Name = 'MLK',  Date=datetime.date(2017, 1, 16), Fixed=False)
        tHolidays.create(Name= 'Washington', Date=datetime.date(2017, 2, 20), Fixed=False)
        tHolidays.create(Name='Memorial',Date=datetime.date(2017, 05, 29), Fixed=True)
        tHolidays.create(Name='Independence', Date=datetime.date(2017, 7, 4), Fixed=True)
        tHolidays.create(Name='Labor Day',  Date=datetime.date(2017, 9, 4), Fixed=True)
        tHolidays.create(Name='Columbus',  Date=datetime.date(2017, 10, 9), Fixed=False)
        tHolidays.create(Name='Veterans', Date=datetime.date(2017, 11, 10), Fixed=False)
        tHolidays.create(Name='Thanksgiving', Date=datetime.date(2017, 11, 23), Fixed=True)
        tHolidays.create(Name='Christmas', Date=datetime.date(2017, 12, 25), Fixed=True)
        
    def filldata(self):
        self.filldata_Holidays()
        
    def Close(self):
        db.close();
