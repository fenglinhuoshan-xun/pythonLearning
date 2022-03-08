-- 函数
delimiter $$
create function st1()
returns float
begin
update cls set sex='m' where name='Jack';
delete from cls where name='Levi';
set @s=(select score from cls where name='Jack');
return @s;
end$$
delimiter ;

-- 函数中不要出现查询多个值的语句
delimiter $$
create function st2() returns float
begin
select * from cls;
set @s=(select score from cls where name='Jack');
return @s;
end$$
delimiter ;

-- 存储过程局部变量
delimiter $$
create procedure p_test()
begin
declare num int;
set num=10;
select num;
end $$
delimiter ;

delimiter $$
create procedure p_test1()
begin
declare num int;
select score from cls where id=1 into num;
select num;
end $$
delimiter ;

-- 使用cls表完成
-- * 编写一个函数,传入两个参数,分别是两个记录id
-- 返回这两个人的分数之差
create function st3(uid1 int,uid2 int)
returns float
begin
set @val1=(select score from cls where id=uid1);
set @val2=(select score from cls where id=uid2);
set @r=@val1-@val2;
return @r;
end $$

--
-- * 编写一个存储过程, 传入学生id,通过out类型的参数
-- 获取到这个学生的年龄
create procedure get_age(in uid int,out num int)
begin
declare val int;
select age from cls where id=uid into val;
set num=val;
end $$

-- 事务隔离级别
set session transaction isolation level read committed