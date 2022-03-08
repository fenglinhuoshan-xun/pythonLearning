

# 聚合操作

select country, avg(attack), avg(defense)
from sanguo
where gender = '男'
group by country
order by avg(attack);

select country, gender, count(*)
from sanguo
group by country, gender;


# 练习1 使用book表
#
# 1. 统计每位作家写的图书的价格之和
select author, sum(price)
from book
group by author;
# 2. 统计每个出版社出版的图书的平均价格
select publication,avg(price)
from book
group by publication;
# 3. 筛选出每个出版社出版图书有最高价格大于60的是哪个出版社
select publication,max(price)
from book
group by publication
having max(price) > 60;
# 4. 查看总共有多少位作者
select count(distinct author) from book;
# 5. 统计所有有出版时间的图书的平均价格
select avg(price)
from book
where publication_time is not null;


-- 部门--员工表
insert into dept values
(1,'总裁办'),(2,'销售部'),(3,'技术部'),(4,'人事部'),
(5,'行政部'),(6,'财务部'),(7,'市场部');

insert into person values
(1,"Alex",33,'m',28000,'2017-3-8',2),
(2,"Tom",23,'m',8000,'2017-4-8',5),
(3,"Lucy",25,'w',18000,'2018-3-22',1),
(4,"Lily",30,'w',20000,'2019-5-19',4),
(5,"Emma",29,'w',6500,'2016-10-5',5),
(6,"Joy",31,'m',50000,'2019-2-6',6),
(7,"Sunny",26,'m',10000,'2015-1-28',7),
(8,"Jame",30,'m',40000,'2017-7-18',3);

-- 级联动作
 alter table person add
 constraint dept_fk1
 foreign key(dept_id)
 references dept(id)
 on delete cascade on update cascade;

 alter table person add
 constraint dept_fk2
 foreign key(dept_id)
 references dept(id)
 on delete set null on update set null;

-- 根据学生 课程  老师E-R模型建立关系表
create table teacher (
id int primary key auto_increment,
姓名 varchar(30),
职称 varchar(30),
年龄 tinyint
);

create table course (
id int primary key auto_increment,
名称 varchar(30),
学分 float,
t_id int ,
constraint t_fk
foreign key(t_id)
references teacher(id)
);

create table stu (
id int primary key auto_increment,
姓名 varchar(32),
年龄 tinyint,
性别 char,
籍贯 varchar(128)
);

create table course_stu (
cid int,
sid int,
score float,
primary key(cid,sid),
constraint c_fk
foreign key(cid)
references course(id),
constraint s_fk
foreign key(sid)
references stu(id)
);


-- 练习2  完成朋友圈关系表的设计和创建
create table user (
id int primary key,
name varchar(30),
passwd char(127)
);

create table pyq (
id int primary key,
image blob,
content text,
time datetime,
address text
);

create table pyq_user (
id int primary key,
uid int,
pid int,
`like` bit,
comment text,
constraint u_fk
foreign key(uid)
references user(id),
constraint p_fk
foreign key(pid)
references pyq(id)
);

-- 练习3
-- book表拆分
--     书籍表
--     作者表
--     出版社表
--  三个实体
--
--  * 实体的属性自拟
--  * 建立三个实体之间的关系
--  * 画出ER图，建立表结构

-- 出版社
create table `出版社` (
id int primary key auto_increment,
名称 varchar(64),
创刊日期 date,
地址 text,
电话 char(16)
);

create table `作家`(
id int primary key auto_increment,
姓名 varchar(32),
性别 char,
出生日期 date,
住址 text,
风格 text
);

create table `图书`(
id int primary key auto_increment,
书名 varchar(30),
出版日期 date,
定价 decimal(5,2),
a_id int,
p_id int,
constraint a_fk foreign key(a_id) references 作家(id),
constraint p_fk foreign key(p_id) references 出版社(id)
);

-- 出版社--作家关系
create table publication_author(
author_id int not null,
publication_id int not null,
签约时间 datetime default now(),
primary  key(author_id,publication_id),
constraint a_fk2 foreign key(author_id) references 作家(id),
constraint p_fk2 foreign key(publication_id) references 出版社(id)
);






