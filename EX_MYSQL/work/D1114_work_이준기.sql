-- D1114_work_이준기 SQL과제

## DB 선택 : use DB_NAME ;
use sakila;

## Table 정보 확인 : desc/describe Table_Name;
desc customer;

# 1번
select * from customer where first_name='MARIA';

# 2번
select * from customer where address_id = 200;

#3번
select * from customer where address_id < 200;

#4번
select * from customer where first_name='MARIA';

#5번
select * from customer where first_name<'MARIA';

#6번
select * from payment where payment_date = '2005-07-09 13:24:07';

#7번
select * from payment where payment_date < '2005-07-09';

#8번
select * from customer where address_id between 5 and 10;

#9번
select * from payment where payment_date between '2005-06-17' and '2005-07-19';

#10번
select * from payment where payment_date='2005-07-08 07:33:56';

#11번
select * from customer where first_name between 'M' and 'O';

#12번
select * from customer where first_name not between 'M' and 'O';

#13번
select * from city where city='Sunnyvale' and country_id=103;

#14번
select * from payment
where payment_date >= '2005-06-01' and payment_date <= '2005-07-05';

#15번
select * from customer
where first_name = 'MARIA' or first_name = 'LINDA';

#16번
SELECT * FROM CUSTOMER
where first_name='MARIA' or first_name = 'LINDA' or first_name = 'NANCY';

# 17번
SELECT * FROM CUSTOMER
where first_name in ('MARIA','LINDA','NANCY');

#18번
SELECT * FROM city
where country_id = 103 or country_id = 86
	and city in ('Cheju', 'Sunnyvale', 'Dallas');
    
#19번
select * from city where country_id = 103;

#20번
select * from city where country_id=86 and city in ('Cheju', 'Sunnyvale', 'Dallas');

#21번
select * from city where country_id=86 or country_id=103 and city in ('Cheju', 'Sunnyvale', 'Dallas');

#22번
select * from city where (country_id =103 or country_id=86) and city in ('Cheju', 'Sunnyvale', 'Dallas');

#23번
select * from city where country_id in (103, 86) and city in ('Cheju', 'Sunnyvale', 'Dallas');

#24번
Select * from address;

#25번
Select * from address where address2 = NULL;

#26번
Select * from address where address2 is NULL;

#27번
Select * from address where address2 is not NULL;

#28번
Select * from address where address2 = '';