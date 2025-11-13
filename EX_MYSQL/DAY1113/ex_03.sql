## ================================================
## 내장 데이터베이스 활용 - 데이터 조회
## ================================================
## DB 선택 : use 데이터베이스이름;
use sakila;

## Table 구조 : desc/describe 테이블이름;
desc customer;

## [1] 간단한 데이터 조회 ==============================
-- 고객의 first_name만 조회
select first_name from customer;

-- 고객의 first_name, last_name 조회
select first_name, last_name from customer;


## [2] 조건 만족하는 데이터 조회 ========================
##	   where 조건 ;
##	   조건 :  컬럼명 연산자 조건
## ================================================
-- first name 'MARIA'인 고객 정보 출력
select first_name, customer_id, active, create_date
from customer
where first_name = 'MARIA';

-- customer_id가  9인 고객 정보 4개 출력
select customer_id, first_name, last_name, address_id
from customer
where customer_id =9;


-- [실1] 현재 활동중인 고객 정보만 추출
select customer_id, first_name, active
from customer
where active != 1;

-- [실2] 이메일이 없는 고객 정보만 추출
select customer_id, first_name, email
from customer
where email is null;


--  [실3] 고객ID가 짝수인 고객 정보만 추출
select customer_id, first_name, email
from customer
where customer_id % 2 = 0;