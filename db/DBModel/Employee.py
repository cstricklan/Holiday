from DBModel import *
from BaseModel import BaseModel
from peewee import *
import datetime

class tEmployee(BaseModel):
    EmpID = CharField(unique=True, max_length=50, primary_key=True)
    Name = CharField(max_length=45)
    ServiceDate = DateTimeField()
    #Created = DateTimeField(default=datetime.datetime.now)
    LastViewed = DateTimeField(null=True)
