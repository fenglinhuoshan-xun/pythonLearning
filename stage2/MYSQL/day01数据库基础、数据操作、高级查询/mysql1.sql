-- 创建表 class_1
create table `class_1` (
id int primary key auto_increment,
name varchar(20) not null,
age tinyint unsigned not null,
sex enum('m','w','o'),
score float default 0
);

-- 创建表 interest
create table `interest` (
id int primary key auto_increment,
name varchar(20) not null,
hobby set('sing','dance','draw'),
level char,
price decimal(7,2),
remark text
);
--
-- 练习1：
-- *  创建数据库 books
-- *  在该数据库下创建数据表 book
--    字段如下：
--    id  书名  作者  出版社  价格  备注
--    数据类型和约束条件自己拟定
create database `books` charset=utf8;

create table book (
id int primary key auto_increment,
title varchar(30) not null,
author varchar(30) default '佚名',
publication varchar(50) not null,
price decimal(6,2),
comment text
);

-- 插入操作

insert into class_1
(name,age,sex,score)
values
('Lucy',17,'w',81);

insert into interest
values
(1,'Joy','sing','B',12800.00,"天籁之声");


-- 练习2
-- *  在数据表book中插入几条数据（>4）
--    作者： 老舍   鲁迅   钱钟书  沈从文  冰心
--          韩寒   郭敬明
--
--    价格： 30 --- 120
--
--    出版社 ：  中国文学   中国教育   机械工业

insert into book (title,author,publication,price,comment) values ('边城','沈从文','机械工业出版社',36,'小城故事多'),('骆驼祥子','老舍','机械工业出版社',87,'你是祥子么'),('林家铺子','茅盾','中国文学出版社',42,'铺子'),('茶馆','老舍','中国教育出版社',70,'茶馆故事');


-- 查找
 select * from class_1 where score not  between 70 and 80;

select * from class_1 where age not in (17,18);

select * from class_1 where sex='w' xor score > 85;


-- 基于book表：
-- 查找价格30多的图书
select *
from book
where price >= 30
  and price < 40;
-- 查找出版社为中国教育出版社的
select *
from book
where publication = '中国教育出版社';
-- 查找老舍写的，中国文学出版社的
select *
from book
where author = '老舍'
  and publication = '中国文学出版社';
-- 查找备注不为空的
select *
from book
where comment is not null;
-- 查找价格超过60的，只看书名和价格
select title, price
from book
where price > 60;
-- 查找价格超过100的或者鲁迅写的
select *
from book
where price > 100
   or author = '鲁迅';

-- alter 操作
alter table interest
    add tel char(16) not null after price;
alter table interest
    drop level;
alter table interest
    modify tel char(16) default '999';
alter table interest
    change tel phone char(16) default '999';
alter table class_1 rename cls;

-- 马拉松
create table marathon
(
    id                 int primary key auto_increment,
    athlete            varchar(30) not null,
    birthday           date,
    registeration_time datetime,
    performance        time
);

insert into marathon
values (1, '曹操', '1990-1-31', "2019/12/28 18:33:25", "2:14:55"),
       (2, '朱仝', '1996-12-5', "2020-1-1 10:10:11", '2:36:5');

# 练习3 使用book表
# 1. 将呐喊的价格改为 45元
update book
set price=45
where title = '呐喊';
# 2. 增加一个字段，出版日期，类型为date，放在价格后面
alter table book
    add publication_time date after price;
# 3. 修改所有老舍的图书的出版日期为2012-5-4
update book
set publication_time='2012-5-4'
where author = '老舍';
# 4. 修改中国教育出版社的图书出版日期为2016-10-1，
#  但是老舍的不修改
update book
set publication_time='2016-10-1'
where publication = '中国教育出版社'
  and author != '老舍';
# 5. 删除所有价格在80元以上的图书
delete
from book
where price > 80;
# 6. 修改价格的字段类型 decimal(5,2)
alter table book
    modify price decimal(5, 2);

# 高级查询
# 多个字段复合排序
select *
from cls
order by age, score desc;

# 查询第一名的男生
select *
from cls
where sex = 'm'
order by score desc
limit 1;

update cls
set score = 80
where sex = 'm'
limit 1;

# 创建sanguo表
create table sanguo
(
    id      int primary key auto_increment,
    name    varchar(30),
    gender  enum ('男','女'),
    country enum ('吴','蜀','魏'),
    attack  smallint,
    defense tinyint
);

insert into sanguo
values (1, '曹操', '男', '魏', 256, 63),
       (2, '张辽', '男', '魏', 328, 69),
       (3, '甄姬', '女', '魏', 168, 34),
       (4, '夏侯渊', '男', '魏', 366, 83),
       (5, '刘备', '男', '蜀', 220, 59),
       (6, '诸葛亮', '男', '蜀', 170, 54),
       (7, '赵云', '男', '蜀', 377, 66),
       (8, '张飞', '男', '蜀', 370, 80),
       (9, '孙尚香', '女', '蜀', 249, 62),
       (10, '大乔', '女', '吴', 190, 44),
       (11, '小乔', '女', '吴', 188, 39),
       (12, '周瑜', '男', '吴', 303, 60),
       (13, '吕蒙', '男', '吴', 330, 71);

# 练习4 ： 综合训练
#
# 查找所有蜀国人信息，按照攻击力排名
select *
from sanguo
where country = '蜀'
order by attack desc;

# 将赵云的攻击力设为360 防御力设置为70
update sanguo
set attack=360,
    defense=70
where name = '赵云';

# 吴国英雄攻击力超过300的改为300（最多改2个）
update sanguo
set attack=300
where country = '吴'
  and attack > 300
limit 2;

# 查找攻击力高于250 的魏国英雄的名字和攻击力
select name, attack
from sanguo
where attack > 250
  and country = '魏';

# 将所有英雄攻击力按照降序排序，如果攻击力相同则按照防御力降序排序
select *
from sanguo
order by attack desc, defense desc;

# 查找所有名字为3个字的英雄
select *
from sanguo
where name like "___";

# 找到魏国防御力前2名的英雄
select *
from sanguo
where country = '魏'
order by defense desc
limit 2;
# 找到攻击力比魏国最高攻击力者还要高的蜀国英雄
select *
from sanguo
where country = '蜀'
  and attack >
      (select attack
       from sanguo
       where country = '魏'
       order by attack desc
       limit 1);

# 找过所有女性角色中攻击力比诸葛亮还要高的英雄
select *
from sanguo
where gender = '女'
  and attack >
      (select attack
       from sanguo
       where name = '诸葛亮');
