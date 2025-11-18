-- ========================================================================
-- Subquery : 쿼리 결과값을 활용한 쿼리문
-- ========================================================================
-- ------------------------------------------------------------------------
-- DB 선택
-- ------------------------------------------------------------------------
use sakila

-- ------------------------------------------------------------------------
-- [1] WHERE절 Subquery -> 중첩 서브쿼리. 대부분의 서브쿼리 해당
--     연산자 IN, ANY, ALL, EXISTS 활용
-- ------------------------------------------------------------------------
-- [다중행 결과] ANA, ROSA와 동일한 customer_id의 고객정보 추출
-- 연산자 IN
select customer_id from customer
    where first_name in ('ROSA', 'ANA');

select * from customer
where customer_id in (
    select customer_id from customer
    where first_name in ('ROSA', 'ANA')
);

-- 연산자 ANY : 서브쿼리 결과 다중행 중 한 개라도 True면 True
select * from customer
where customer_id = ANY (
    select customer_id from customer
    where first_name in ('ROSA', 'ANA')
);

select * from customer
where customer_id < ANY (
    select customer_id from customer
    where first_name in ('ROSA', 'ANA')
);

select * from customer
where customer_id > ANY (
    select customer_id from customer
    where first_name in ('ROSA', 'ANA')
);


-- 연산자 EXISTS : 서브쿼리 결과 행이 있으면 True/ 없으면 False
-- 반환되는 행 존재 여부만 관심. 실제 반환되는 데이터 관심 X. 사용 X
-- 서브쿼리의 SELECT * 또는 SELECT 1 형식으로 작성하는 경우 대부분

select * from customer
where EXISTS (
    select customer_id from customer
    where first_name in ('KANG')
);

select 7 from customer
where first_name in ('ROSA', 'ANA')

select 7 from customer
where first_name in ('KANG')