-- ========================================================================
-- Subquery : 쿼리 결과값을 활용한 쿼리문
-- ========================================================================
-- ------------------------------------------------------------------------
-- DB 선택
-- ------------------------------------------------------------------------
use sakila

-- ------------------------------------------------------------------------
-- [1] WHERE절 Subquery -> 중첩 서브쿼리. 대부분의 서브쿼리 해당
-- ------------------------------------------------------------------------
-- [단일행 결과] ROSA와 동일한 customer_id의 고객정보 추출
select * from customer
where customer_id = (
    select customer_id from customer
where first_name = 'ROSA'
);

set @u_id := ( select customer_id from customer
               where first_name = 'ROSA');

select * from customer
where customer_id = @u_id;

-- [다중행 결과] ANA, ROSA와 동일한 customer_id의 고객정보 추출
select customer_id from customer
    where first_name in ('ROSA', 'ANA');

select * from customer
where customer_id in (
    select customer_id from customer
    where first_name in ('ROSA', 'ANA')
);

-- [다중행 결과] ANA, ROSA의 지불내역 정보 추출
select * from payment
where customer_id in (
    select customer_id from customer
    where first_name in ('ROSA', 'ANA')
);


-- [다중행 결과] action 장르 영화 리스트 추출 --------------------------------
-- 1. action 장르의 id 찾기 => category TB
-- 2. action 장르에 해당하는 영화 id => film_category TB
-- 3. action 장르에 해당하는 영화 정보 리스트 추출

select category_id, name
from category
where name='action';            -- action 장르 id => 1

select * from film_category     -- id 1에 해당하는 영화 id
where category_id = 1;

select * from film_category     -- action 장르에 해당하는 영화 id
where category_id = (
    select category_id
    from category
    where name = 'action'
);

select * from film
where film_Id in (
    select film_id from film_category   -- action 장르에 해당하는 영화 id
    where category_id = (
        select category_id
        from category
        where name='action'
    )
);