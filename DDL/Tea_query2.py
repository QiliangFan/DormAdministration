from DDL.account import *


#获取同楼管理员信息
def GetManagerInfoSameBuilding(account):
    cur.execute('''
    select m_id,name,gender,birthday,own_phone
    from manager
    where build_id=(
    select t.build_id
    from manager t
    where t.account_name='%s')
    '''%(account,))
    data=cur.fetchall()
    return data