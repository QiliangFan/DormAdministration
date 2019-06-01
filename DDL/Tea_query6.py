from DDL.account import *

def getRoomAvaliable(account):
    cur.execute('''
    select room_id,max_capacity-act_capacity
    from room
    where act_capacity<max_capacity
    and 
    build_id=(
    select manager.build_id
    from manager
    where account_name='%s')
    '''%(account))
    data=cur.fetchall()
    return data