from DBModel import *
from BaseModel import BaseModel
from peewee import *
import datetime
import uuid

class tEmployeeHoliday(BaseModel):
    ID = UUIDField(default=uuid.uuid4, index=True, primary_key=True)
    Emp = ForeignKeyField(tEmployee)
    Date = DateTimeField()
    Hours = IntegerField()
    Created = DateTimeField(default=datetime.datetime.now)
