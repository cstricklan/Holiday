from DBModel import *
from BaseModel import BaseModel
from peewee import *
import uuid

class tHolidays(BaseModel):
    ID = UUIDField(default=uuid.uuid4, index=True, primary_key=True)
    Name = CharField(max_length=45)
    Date = DateTimeField()
    Fixed = BooleanField()
