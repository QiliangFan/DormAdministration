from DDL.account import *
import pymysql



def insertNewStu(account,pwd):
    cur.execute("insert into account(account_name,password,type,type_id) values ('%s','%s','student','null')"%(account,pwd))
    db.commit()


def insertNewTea(account,pwd):
    cur.execute("insert into account(account_name,password,type,type_id) values ('%s','%s','manager','null')"%(account,pwd))
    db.commit()

