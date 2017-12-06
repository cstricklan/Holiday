import sys, os
import __builtin__

sys.path.append(os.path.abspath("../db"))
sys.path.append(os.path.abspath("../logic"))

WTF_CSRF_ENABLED = True
SECRET_KEY="i-bet-you-cant-guess-it"

__builtin__.DBType="sqlite"
__builtin__.SQLLightDB = "/tmp/holidays.db"
