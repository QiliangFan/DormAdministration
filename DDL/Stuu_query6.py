from DDL.account import *

def showAllStu(account):
    cur.execute('''
    select * from log
    where b_id=(select room_build_id from student where account_name='%s')'''%(account))
    data=cur.fetchall()
    print(data)
    if len(data)>0:
        return data
    else:
        return ((),)