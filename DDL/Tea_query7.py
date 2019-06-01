from DDL.account import *

def getNumOfBed(room,account):
    cur.execute('''
    select room_id,max_capacity-act_capacity
    from room
    where room_id='%s'
     and 
     build_id=(
     select manager.build_id
     from manager
     where account_name='%s')'''%(room,account))
    data=cur.fetchall()
    return data