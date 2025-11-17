## D1117_work_이준기 과제 : 4장 되새김 문제, 5-1장 정리 (177page ~ 199page)


## 4장 되새김 문제
use world;

# Q1 : world 데이터베이스의 country 테이블에서 Code가 KOR인 데이터를 조회하는 쿼리를 작성하세요.
select *
from country
where Code = 'KOR'

# Q2 : world 데이터베이스의 country 테이블에서 Region 열에 Asia라는 글자를 포함하는 데이터를 조회하는 쿼리를 작성하세요.
select *
from country
where Region LIKE '%Asia%'

# Q3 : world 데이터베이스의 country 테이블에서 Name 열의 데이터가 5글자인 데이터를 조회하는 쿼리를 작성하세요.
select *
from country
where length(Name)=5

# Q4 : world 데이터베이스의 country 테이블에서 Population열을 숫자가 높은 순으로 정렬하여 조회하는 쿼리를 작성하세요.
select *
from country
order by Population DESC

# Q5 : world 데이터베이스의 country 테이블에서 LifeExpectancy 열의 데이터가 60 이상 70 이하인 데이터를 조회하는 쿼리를 작성하세요.
select *
from country
where `LifeExpectancy` >= 60 and `LifeExpectancy` <= 70

# Q6 : world 데이터베이스의 country 테이블에서 Region 열의 데이터가 Asia를 포함하지 않으면서 name 열에서 g 또는 u 글자를 포함하는 데이터를
#      Population 열의 내림차순으로 조회하는 쿼리를 작성하세요
select *
from country
WHERE (Region not Like '%Asia%') and (name like '%g%' or '%u%')
order by Population desc

# Q7 : world 데이터베이스에서 country 테이블에서 Region 그룹별로 개수를 구하고, 개수가 높은 순서대로 조회하는 쿼리를 작성하세요.
select count(*) 'CNT'
from country
group by Region
order by count(Region) DESC

## 5장 조인으로 두 테이블 묶기
use sakila;

# 내부 조인한 테이블에서 조건에 맞는 데이터 조회
SELECT
	a.customer_id, a.store_id, a.first_name, a.last_name, a.email, a.address_id AS a_address_id,
	b.address_id AS b_address_id, b.address, b.district, b.city_id, b.postal_code, b.phone, b.location
FROM customer AS a
	INNER JOIN address AS b ON a.address_id = b.address_id
WHERE a.first_name = 'ROSA';

# 열 이름이 유일하지 않은 경우
SELECT
	address_id
FROM customer AS a
	INNER JOIN address AS b ON a.address_id = b.address_id
WHERE a.first_name = 'ROSA';

# 2개의 조인 조건으로 조인한 테이블에서 조건에 맞는 데이터 조회
SELECT
	a.customer_id, a.first_name, a.last_name,
	b.address_id, b.address, b.district, b.postal_code
FROM customer AS a
	INNER join address AS b ON a.address_id = b.address_id AND a.create_date = b.last_update
WHERE a.first_name = 'ROSA';

# 3개의 테이블을 조인한 테이블에서 조건에 맞는 데이터 조회
SELECT
	a.customer_id, a.first_name, a.last_name,
	b.address_id, b.address, b.district, b.postal_code,
	c.city_id, c.city
FROM customer AS a
	INNER JOIN address AS b ON a.address_id = b.address_id
	INNER JOIN city AS c ON b.city_id = c.city_id
WHERE a.first_name = 'ROSA';

# LEFT OUTER JOIN한 결과 조회
SELECT
	a.address, a.address_id AS a_address_id,
	b.address_id AS b_address_id, b.store_id
FROM address AS a
	LEFT OUTER JOIN store AS b ON a.address_id = b.address_id;

# LEFT OUTER JOIN으로 조회한 결과에서 NULL만 조회
SELECT
	a.address, a.address_id AS a_address_id,
	b.address_id AS b_address_id, b.store_id
FROM address AS a
	LEFT OUTER JOIN store AS b ON a.address_id = b.address_id
WHERE b.address_id IS NULL

# RIGHT OUTER JOIN한 결과 조회
SELECT
	a.address, a.address_id AS a_address_id,
	b.address_id AS b_address_id, b.store_id
FROM address AS a
	RIGHT OUTER JOIN store AS b ON a.address_id = b.address_id;

# RIGHT OUTER JOIN으로 조회한 결과에서 NULL만 조회
SELECT
	a.address_id AS a_address_id, a.store_id,
	b.address, b.address_id AS b_address_id
FROM store AS a
	RIGHT OUTER JOIN address AS b ON a.address_id = b.address_id
WHERE a.address_id IS NULL;

# FULL OUTER JOIN한 결과 조회
SELECT
	a.address_id AS a_address_id, a.store_id,
	b.address, b.address_id AS b_address_id
FROM store AS a
	LEFT OUTER JOIN address AS b ON a.address_id = b.address_id

UNION

SELECT
	a.address_id AS a_address_id, a.store_id,
	b.address, b.address_id AS b_address_id
FROM store AS a	
	RIGHT OUTER JOIN address AS b ON a.address_id = b.address_id;

# FULL OUTER JOIN으로 조회한 결과에서 NULL만 조회
SELECT
	a.address_id AS a_address_id, a.store_id,
	b.address, b.address_id AS b_address_id
FROM store AS a
	LEFT OUTER JOIN address AS b ON a.address_id = b.address_id
WHERE b.address_id IS NULL

UNION

SELECT
	a.address_id AS a_address_id, a.store_id,
	b.address, b.address_id AS b_address_id
FROM store AS a
	RIGHT OUTER JOIN address AS b ON a.address_id = b.address_id
WHERE a.address_id IS NULL;

# 샘플 데이터 생성
CREATE TABLE doit_cross1(num INT);
CREATE TABLE doit_cross2(name VARCHAR(10));

INSERT INTO doit_cross1 VALUES (1), (2), (3);
INSERT INTO doit_cross2 VALUES ('Do'), ('It'), ('SQL');

# CROSS JOIN 문을 적용한 쿼리
SELECT
	a.num, b.name
FROM doit_cross1 AS a
	CROSS JOIN doit_cross2 AS b
ORDER BY a.num;

# WHERE 문을 사용한 CROSS JOIN
SELECT
	a.num, b.name
FROM doit_cross1 AS a
	CROSS JOIN doit_cross2 AS b
WHERE a.num = 1;

# SELF JOIN 문을 적용한 쿼리 1
SELECT 
	a.customer_id AS a_customer_id, b.customer_id AS b_customer_id
FROM customer AS a
	INNER JOIN customer AS b ON a.customer_id = b.customer_id

# SELF JOIN 문을 적용한 쿼리 2
SELECT
	a.payment_id, a.amount, b.payment_id, b.amount, b.amount - a.amount AS profit_amount
FROM payment AS a
	LEFT OUTER JOIN payment AS b ON a.payment_id = b.payment_id -1;