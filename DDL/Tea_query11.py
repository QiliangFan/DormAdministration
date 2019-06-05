from DDL.account import *

def Teamodify(account,t_id,name,gender,b_id,phone,birthday):
    cur.execute("select count(*) from building where build_id='%s'"%(b_id))
    data=cur.fetchall()
    if data[0][0]==0:
        return -1
    cur.callproc("change_TeaInformation",(account,t_id,name,gender,b_id,phone,birthday))
    db.commit()
    return 0

def getTeaInfo(account):
    cur.execute('''
    select m_id,name,gender,build_id,own_phone,birthday
    from manager
    where account_name='%s' '''%(account))


    data=cur.fetchall()
    return data