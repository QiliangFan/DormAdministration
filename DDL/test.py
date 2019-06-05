from DDL.account import *


cur.execute("update  room set act_capacity=0")
db.commit()