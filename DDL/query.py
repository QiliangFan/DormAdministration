from DDL.account import *
import pymysql


def selectAllByAccount(account):
    cur.execute("select * from account where account_name='%s'"%(account,))
    data=cur.fetchall()
    return data

def selectTypeByAccount(account):
    cur.execute("select type from account where account_name='%s'"%(account,))
    data=cur.fetchall()
    return data[0][0]

def selectPwdByAccount(account):
    cur.execute("select password from account where account_name='%s'"%(account,))
    data=cur.fetchall()
    return data[0][0]

def selectNumByType(type):
    cur.execute("select count(*) from account where type='%s'"%(type,))
    data=cur.fetchall()
    return data[0][0]

def selectRoomBuildingByAccount(account):
    cur.execute("select room_build_id from student where student.account_id in (select account.account_id from account where account_name='%s')"%(account,))
    data=cur.fetchall()
    return data

def selectRoomByAccount(account):
    cur.execute("select room_id from student where student.account_id in (select account.account_id from account where account_name='%s')"%(account,))
    data=cur.fetchall()
    return data

def selectStudentNumberHasInByAccount(account):
    cur.execute("select count(*) from student")
    data=cur.fetchall()
    return data[0][0]