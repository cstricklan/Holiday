from peewee import *
import __builtin__


db = None

if hasattr(__builtin__,  'DBType'):
    dbtype = __builtin__.DBType
    
    if dbtype  == "sqlite":
        db = SqliteDatabase(__builtin__.SQLLightDB)
    if dbtype == "sqlitetmp":
        db = SqliteDatabase(":memory:")
        
        
from Employee import tEmployee
from Holidays import tHolidays
from EmployeeHoliday import tEmployeeHoliday

__all__ = ['db','tEmployee', 'tHolidays', 'tEmployeeHoliday']
