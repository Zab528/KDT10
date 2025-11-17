## ============================================================
## 조회 개수 제한 / 중복 제거 / 정렬
## ============================================================
## DB 선택
use sakila;

## ============================================================
## 조회 결과 개수 제한 : limit 숫자 => 0부터~ 숫자 개수
##                     limit 첫번째부터 몇개 건너뛸 개수, 조회 개수
## ============================================================

## 5개 데이터만 조회
select * from customer;
select * from customer limit 5;

-- 5개 건너뛰고 3개
select * from customer limit 5, 3;
-- 5개 건너뛰고 3개 : limit 추출개수 Offset 건너뛸 개수
select * from customer limit 3 OFFSET 5;


-- ============================================================
-- 중복 제거 : distinct
-- ============================================================

select store_id from customer;

select DISTINCT store_id from customer;

-- count() : 개수 반환  ----------------------------------------
select count( store_id ) from customer;

select count( DISTINCT store_id ) from customer;


-- ============================================================
-- 정렬 : order by 정렬기준 컬럼명 ASC[기]/DESC limit 숫자
--       limit 숫자
-- ============================================================

-- TOP-N개 : limit와 함께 조회 / 정렬 조건에 따라 상위/하위 
select first_name from customer
where customer_id >=100
order by first_name ASC
limit 5;


select customer_id, first_name, last_name from customer
order by customer_id desc limit 3;

