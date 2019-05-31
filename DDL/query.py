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

#宿舍楼数量
def selectRoomBuilding():
    cur.execute("select count(*) from building;")
    data=cur.fetchall()
    d=data[0][0]
    return str(d)

#宿舍间数
def selectRoom():
    cur.execute("select count(*) from room;")
    data=cur.fetchall()
    return str(data[0][0])

def selectStudentNumberHasIn(account):
    cur.execute("select count(*) from student")
    data=cur.fetchall()
    return data[0][0]

#宿舍楼数量
def countBuildtaccount():
    cur.execute("call countbuildtaccount()")
    data=cur.fetchall()
    return data[0][0]

#已经容纳的学生
def countStudentHasIn():
    cur.execute("select sum(act_capacity) from room;")
    data=cur.fetchall()
    return str(data[0[0]])

def countMaxStudentCanIn():
    cur.execute("select sum(max_capacity) from room;")
    data=cur.fetchall()
    if data[0][0] is None:
        return str(0)
    else:
        return str(data[0][0])