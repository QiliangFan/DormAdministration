from DDL.account import *
import pymysql



def insertNewStu(account,pwd):
    cur.execute("insert into account(account_name,password,type) values ('%s','%s','student')"%(account,pwd))
    db.commit()


def insertNewTea(account,pwd):
    cur.execute("insert into account(account_name,password,type) values ('%s','%s','manager')"%(account,pwd))
    db.commit()

