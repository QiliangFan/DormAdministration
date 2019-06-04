from DDL.account import *

def teaDelete(account):
    cur.execute('''
    delete from log
    where b_id=(
    select build_id
    from manager
    where account_name='%s')'''%(account))
    db.commit()

def teaShowAll(account):
    cur.execute('''
    select * from log
    where b_id=(
    select build_id
    from manager
    where account_name='%s')'''%(account))
    data=cur.fetchall()

    return data