from DDL.account import *

def delete(account,stuid):
    cur.execute('''
    select  count(*)
    from student
    where stu_id='%s' '''%(stuid,))
    data=cur.fetchall()
    if data[0][0]==0:
        return -1
    cur.callproc("DeleteStuent",(account,stuid))
    cur.execute('''
                           select  stu_id,name,gender,dept_name,room_id,bed_id,birthday,own_phone,parent_phone
                           from student
                           where stu_id='%s'
                            and 
                            (room_build_id=(
                            select build_id
                            from manager
                            where manager.account_name='%s')
                            or 
                            room_build_id is null
                            )''' % (stuid, account))

    db.commit()
    data = cur.fetchall()
    return data