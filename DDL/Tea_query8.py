from DDL.account import *

def arrangeStuWithoutBed(stuid,room,account):
    cur.execute('''
    select bed_id
    from student
    where stu_id='%s' '''%(stuid))
    data=cur.fetchall()
    if len(data)>0:
        #学生已有床位
        return -1
    else:
        cur.execute('''
        select max_capacity-act_capacity
        from room
        where room_id='%s' '''%(room))
        d=cur.fetchall()
        if d[0][0]==0:
            #宿舍已满
            return -1;
        cur.execute('''
        select act_capacity
        from room
        where room_id='%s' '''%(room))
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


        cur.execute('''
        update student
        set bed_id=(
        select act_capacity+1
        from room
        where room.room_id='%s'),
        room_id ='%s' ,
        room_build_id=(
        select build_id
        from manager
        where manager.account_name='%s')
        where stu_id='%s' '''%(room,room,account,stuid))
        # 宿舍已用床位+1
        cur.execute('''
        update room set
        act_capacity=act_capacity+1
        where room_id='%s' '''%(room))
        db.commit()
        cur.execute('''
        select stu_id, name, gender, dept_name, room_id, bed_id, birthday, own_phone, parent_phone
        from student
        where stu_id='%s' '''%(stuid))
        data=cur.fetchall()
        return data
