from DDL.account import *

def getStuByBuildAndName(build,name):
    cur.execute('''
    select stu_id,name,dept_name,grade,room_id
    from student
    where room_build_id='%s'
     and name='%s' '''%(build,name))
    data=cur.fetchall()
    print(data)
    return data