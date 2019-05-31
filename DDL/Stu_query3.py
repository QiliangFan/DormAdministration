from DDL.account import *

def getStuByBuildAndName(build,name):
    cur.execute('''
    select stu_id,name,dept_name,grade,room_id
    from student,information
    where student.information_id=information.information_id 
    and room_build_id='%s'
     and name='%s' '''%(build,name))
    data=cur.fetchall()
    return data