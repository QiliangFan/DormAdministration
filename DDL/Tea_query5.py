from DDL.account import *

#获取同楼某学生（stu_id）的信息
def getStuInfoById(stuid,account):
    cur.execute('''
    select stu_id,name,gender,dept_name,room_id,bed_id,birthday,own_phone,parent_phone
    from student
    where stu_id='%s'
     and 
     room_build_id=(
     select build_id
     from manager
     where manager.account_name='%s')'''%(stuid,account))
    data=cur.fetchall()
    return data