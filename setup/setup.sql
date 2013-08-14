-- create and use database
create database if not exists testing;
use testing;

-- create table
create table if not exists aw_jobexecution (
  name varchar(64),
  status varchar(12),
  load_date datetime,
  job_end_date datetime,
  job_execution_duration long
);

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
truncate table aw_jobexecution;
insert into aw_jobexecution (name, status, load_date, job_end_date, job_execution_duration)
  values ('test 00', 'done', sysdate(), sysdate(), job_end_date - load_date);
insert into aw_jobexecution (name, status, load_date, job_end_date, job_execution_duration)
  values ('test 01', 'started', sysdate(), date_add(sysdate(), interval 1 day_minute), job_end_date - load_date);
insert into aw_jobexecution (name, status, load_date, job_end_date, job_execution_duration)
  values ('test 02', 'failed', sysdate(), date_add(sysdate(), interval 1 day_hour), job_end_date - load_date);
