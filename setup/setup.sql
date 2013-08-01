-- execute as root on mysql to get schema setup for testing
create database test;
use test;
create table test (id int, value int);
create user 'py'@'localhost' identified by 'py_pass';
grant all privileges on test.* to 'py'@'localhost' with grant option;

insert into test (id, value) values (0, 0);
insert into test (id, value) values (1, 1);
