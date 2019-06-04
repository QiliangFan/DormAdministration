from DDL.account import *

def selectAll10(s_id,account):
    cur.execute('''
                       select  stu_id,name,gender,dept_name,room_id,bed_id,birthday,own_phone,parent_phone
                       from student
                       where stu_id='%s'
                        and room_build_id=(
                        select build_id
                        from manager
                        where manager.account_name='%s')''' % (s_id, account))

    data = cur.fetchall()
    return data

def judgeIsFull(room,account):
    cur.execute('''
    select max_capacity-act_capacity
    from room
    where room_id='%s' and 
    build_id=(
    select manager.build_id
    from manager
    where account_name='%s')''' % (room, account))
    data=cur.fetchall()
    return data


def adjust(s_id, room, account):
    cur.execute('''
    select room_id
    from student
    where stu_id='%s'
    '''%(s_id,))
    data=cur.fetchall()
    if len(data)>0 and str(data[0][0])==room:
        data=selectAll10(s_id,account)
        return data
    
    data = judgeIsFull(room,account)
    if len(data)>0 and data[0][0] == 0:
        return -1  # 已经满了

    cur.execute('''
    select count(*)
    from student
    where stu_id='%s'
     and length(room_id)>0 ''' % (s_id,))

    data = cur.fetchall()

    if len(data)>0 and data[0][0] == 0:
        flag = 0  # 开始并没有宿舍
    else:
        flag = 1  # 已经有宿舍了
    print(flag)
    cur.execute('''
    select act_capacity
    from room
    where room_id='%s' 
    and 
    build_id=(
    select manager.build_id
    from manager
    where account_name='%s')''' % (room, account))
    data = cur.fetchall()

    flag_room = -1
    if data[0][0] == 0:
        flag_room = 0  # 安排的房间最开始没人
    if data[0][0] >= 1:
        flag_room = 1  # 安排的房间最开始有人
    print(flag_room)
    if flag_room == 1:
        if flag == 0:
            # 安排到指定宿舍后的操作
            cur.execute('''
            update student set
            room_id='%s',
             room_build_id =(
             select build_id
             from manager
             where manager.account_name='%s'),
             bed_id=(
             select act_capacity+1
             from room
             where room.room_id='%s'
             and build_id=(
             select manager.build_id
             from manager
             where manager.account_name='%s'))
              where stu_id='%s' ''' % (room, account, room,  account,s_id))
            db.commit()

            cur.execute('''
                    update room set act_capacity=act_capacity+1,
                    max_capacity=4
                    where room.build_id=(
                    select manager.build_id
                    from manager
                    where account_name='%s')
                    and room.room_id='%s' ''' % (account, room))
            db.commit()
        # 一开始有宿舍
        else:
            cur.execute('''
            select act_capacity
            from room
            where room_id=(
            select student.room_id
            from student
            where stu_id='%s')
            and build_id=(
            select manager.build_id
            from manager
            where account_name='%s')''' % (s_id, account))
            db.commit()

            data = cur.fetchall()
            if data[0] == 1:
                cur.execute('''
                update room set
                act_capacity=0
                where room_id=(
                select student.room_id
                from student
                where stu_id='%s') and build_id=(
                select manager.build_id
                from manager
                where account_name='%s')''' % (s_id, account))
                db.commit()

                cur.execute('''
                update building set
                act_roomnum=act_roomnum-1
                where build_id=(
                select manager.build_id
                from manager
                where account_name='%s')''' % (account,))
                db.commit()
            else:
                cur.execute('''
                update room set
                act_capacity=act_capacity-1
                where room_id=(
                select student.room_id
                from student
                where stu_id='%s') and build_id=(
                select manager.build_id
                from manager
                where account_name='%s')''' % (s_id, account))
                db.commit()

            # 安排到指定宿舍后的操作
            cur.execute('''
            update student set
            room_id='%s',
             room_build_id =(
             select build_id
             from manager
             where manager.account_name='%s'),
             bed_id=(
             select act_capacity+1
             from room
             where room.room_id='%s' and build_id=(
             select manager.build_id
             from manager
             where manager.account_name='%s'))
              where stu_id='%s' ''' % (room, account, room,account, s_id))
            db.commit()

    # 安排的房间最开始没人
    else:

        # 已用床位加1

        cur.execute('''
        update room set act_capacity=act_capacity+1,
        max_capacity=4
        where room.build_id=(
        select manager.build_id
        from manager
        where account_name='%s')
        and room.room_id='%s' ''' % (account, room))



        db.commit()

        if flag == 1:
            cur.execute('''
            select act_capacity
            from room
            where room_id=(
            select student.room_id
            from student
            where stu_id='%s')
             and 
             build_id=(
             select manager.build_id
             from manager
             where account_name='%s')''' % (s_id, account))
            data = cur.fetchall()
            if data[0][0] == 1:
                cur.execute('''
                update room set
                act_capacity=0
                where room_id=(
                select student.room_id
                from student
                where stu_id='%s') and build_id=(
                select manager.build_id
                from manager
                where account_name='%s')''' % (s_id, account))
                db.commit()
                print("+++++++++++++++++++++++++++++++++++++++++")

                cur.execute('''
                update building set
                act_roomnum=act_roomnum-1
                where build_id=(
                select manager.build_id
                from manager
                where account_name='%s')''' % (account,))
                db.commit()
            else:
                
                cur.execute('''
               update room set
               act_capacity=act_capacity-1
               where room_id=(
               select student.room_id
               from student
               where stu_id='%s') and build_id=(
               select manager.build_id
               from manager
               where account_name='%s')''' % (s_id, account))
                db.commit()
            # 安排到指定宿舍后的操作
            cur.execute('''
                update student set
                room_id='%s',
                 room_build_id =(
                 select build_id
                 from manager
                 where manager.account_name='%s'),
                 bed_id=(
                 select act_capacity
                 from room
                 where room.room_id='%s')
                  where stu_id='%s' ''' % (room, account, room, s_id))
            db.commit()

    cur.execute('''
                select  stu_id,name,gender,dept_name,room_id,bed_id,birthday,own_phone,parent_phone
                from student
                where stu_id='%s'
                 and room_build_id=(
                 select build_id
                 from manager
                 where manager.account_name='%s')''' % (s_id, account))

    data = cur.fetchall()
    db.commit()
    return data
