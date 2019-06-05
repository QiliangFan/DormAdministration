from DDL.account import *

def modify(account,stu_id,name,dept_name,grade,phone_parent,phone_own,gender,bed_id,admission_date,birth_day):
    cur.callproc("change_information",(account,stu_id,name,dept_name,grade,phone_parent,phone_own,gender,bed_id,admission_date,birth_day))
    db.commit()

def getinfo(account):
    cur.execute('''
    select stu_id, name, dept_name, grade, parent_phone, own_phone, gender, bed_id, admission_date, birthday
    from student
    where account_name='%s' '''%(account))
    data=cur.fetchall()
    return data