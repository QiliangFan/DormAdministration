from DDL.account import *

def arrangeStuWithoutBed(stuid,room,account):
    cur.execute('''
    select bed_id
    from student
    where stu_id='%s' '''%(stuid))
    data=cur.fetchall()
    print(data)
    if len(data)>0 and len(data[0])>1:
        #学生已有床位
        print("已有床位")
        return -1
    else:
        cur.execute('''
        select max_capacity-act_capacity
        from room
        where room_id='%s' 
        and
        build_id=(
            select manager.build_id
            from manager
            where account_name='%s') '''%(room,account))
        d=cur.fetchall()
        if d[0][0]==0:
            #宿舍已满
            return -1
        cur.execute('''
        select act_capacity
        from room
        where room_id='%s' 
        and
        build_id=(
            select manager.build_id
            from manager
            where account_name='%s' )'''%(room,account))
        d=cur.fetchall()
        if d[0][0]==0:
            #已用宿舍+1
            cur.execute('''
            update building set
            act_roomnum=act_roomnum+1
            where build_id=(
            select manager.build_id
            from manager
            where account_name='%s')'''%(account))


        cur.execute("select count(*) from student where stu_id='%s' "%(stuid))
        data=cur.fetchall()
        print(data)
        if data[0][0]==0:
            cur.execute('''
        insert into student(stu_id,account_name)
        values
        ('%s','%s')
        '''%(stuid,stuid))
            db.commit()

        cur.execute('''
        update student
        set bed_id=(
        select act_capacity+1
        from room
        where room.room_id='%s'
        and build_id=(
            select manager.build_id
            from manager
            where account_name='%s'
        )),
        room_id ='%s' ,
        room_build_id=(
        select build_id
        from manager
        where manager.account_name='%s')
        where stu_id='%s' '''%(room,account,room,account,stuid))
        db.commit()
        # 宿舍已用床位+1
        cur.execute('''
        update room set
        act_capacity=act_capacity+1
        where room_id='%s' 
        and 
        build_id=(
        select build_id
        from manager
        where manager.account_name='%s')
            '''%(room,account))
        db.commit()
        cur.execute('''
        select stu_id, name, gender, dept_name, room_id, bed_id, birthday, own_phone, parent_phone
        from student
        where stu_id='%s' '''%(stuid))
        data=cur.fetchall()
        return data
