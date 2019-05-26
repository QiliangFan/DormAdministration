import DDL.account

mydb=DDL.account.db
mycur=DDL.account.cursor

def selectAllByAccount(account):
    mycur.execute("select * from account where account_name='%s'"%(account,))
    return mycur.fetchall()