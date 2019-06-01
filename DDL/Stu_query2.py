from DDL.account import *

def getStuInfro(dorm,room):
    cur.execute('''
    select stu_id,name,dept_name,grade,birthday,own_phone,parent_phone,bed_id
    from student
    where room_id='%s' and room_build_id='%s' '''%(room,dorm))
    data=cur.fetchall()
    return data