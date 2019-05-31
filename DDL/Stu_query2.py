from DDL.account import *

def getStuInfro(dorm,room):
    cur.execute('''
    select stu_id,name,dept_name,grade,birthday,own_phone,parent_phone,bed_id
    from student,information
    where room_id='%s' and room_build_id='%s' and student.information_id=information.information_id '''%(room,dorm))
    data=cur.fetchall()
    print(data)
    return data