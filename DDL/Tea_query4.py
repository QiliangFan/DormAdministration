from DDL.account import *

#获取同楼某间的学生信息
def getStuInfo(room,account):
    cur.execute('''
    select stu_id,name,gender,dept_name,room_id,bed_id,birthday,own_phone,parent_phone
    from student
    where student.room_id='%s' 
    and 
    room_build_id=(
    select build_id
    from manager
    where manager.account_name='%s')'''%(room,account))
    data=cur.fetchall()
    return data