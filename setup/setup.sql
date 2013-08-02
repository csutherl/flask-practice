-- create and use database
create database if not exists testing;
use testing;

-- create table
create table if not exists proc_status (name varchar(64), status varchar(12), start_date datetime, end_date datetime, duration long);

-- create and setup user account
drop procedure if exists createUser;
create procedure createUser(username varchar(50), pw varchar(50), db varchar(50))
begin
  if (select exists(select 1 from mysql.user where user = username)) = 0 then
      begin
        -- creat user
        set @sql = concat('create user ', username, '@\'localhost\' identified by \'', pw, '\'');
        prepare stmt from @sql;
        execute stmt;
        deallocate prepare stmt;
      end;

      begin
        -- set privileges
        set @sql = concat('grant all privileges on ', db, '.* to ', username, '@localhost', ' with grant option');
        prepare stmt from @sql;
        execute stmt;
        deallocate prepare stmt;
      end;
  end if;
end;

-- call createUser SP
call createUser('py', 'py_pass', 'testing');

-- truncate table (so I dont get dupes) and insert some test data
truncate table proc_status;
insert into proc_status (name, status, start_date, end_date, duration)
  values ('test 00', 'done', sysdate(), sysdate(), end_date - start_date);
insert into proc_status (name, status, start_date, end_date, duration)
  values ('test 01', 'started', sysdate(), sysdate() + 10, end_date - start_date);
insert into proc_status (name, status, start_date, end_date, duration)
  values ('test 02', 'failed', sysdate(), sysdate() + 20, end_date - start_date);
