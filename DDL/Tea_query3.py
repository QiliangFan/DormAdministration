from DDL.account import *

def getStuInfoSameBuilding(account):
    cur.execute('''
    select stu_id,name,gender, dept_name,room_id,bed_id, birthday, own_phone, parent_phone
    from student
    where room_build_id=(
    select build_id
    from manager
    where manager.account_name='%s')'''%(account,))
    data=cur.fetchall()
    return data