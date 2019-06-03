from DDL.account import *

def apply(account,stuid,name,building,room,toRoom):
    cur.callproc("applicate",(stuid,stuid,name,building,room,toRoom))
    db.commit()
    return 0