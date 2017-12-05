import __builtin__
import sys, os

sys.path.append(os.path.abspath("../db"))


__builtin__.DBType = "sqlite"
__builtin__.SQLLightDB = "/tmp/holidays.db"

#__builtin__.DBType = "sqlitetmp"


from DBModel import *
from SetupDB import CreateDB

c = CreateDB.CreateDB()
c.CreateTables()
c.filldata()
c.Close()
