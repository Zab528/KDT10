## 04-3 ORDER BY 절로 데이터 정렬하기
use sakila

# first_name 열을 기준으로 정렬
select * from customer order by first_name;

# last_name 열을 기준으로 정렬
select * from customer order by last_name;

# store_id, first_name 순으로 데이터 정렬
select * from customer order by store_id, first_name

# first_name, store_id 순으로 데이터 정렬
select * from customer order by first_name, store_id;

# 오름차순 또는 내림차순으로 정렬하기
# first_name 열을 오름차순으로 정렬
select * from customer order by first_name ASC;

# first_name 열을 내림차순으로 정렬
select * from customer order by first_name desc;

# ASC와 DESC를 조합하여 데이터 정렬
select * from customer order by store_id desc, first_name asc;

# LIMIT으로 상위 10개의 데이터 조회
select * from customer order by store_id desc, first_name asc limit 10;

# LIMIT으로 101번째부터 10개의 데이터 조회
select * from customer order by customer_id asc limit 100, 10;

# 데이터 100개 건너뛰고 101번째부터 데이터 10개 조회
select * from customer order by customer_id asc limit 10 offset 100;




## 04-4 와일드카드로 문자열 조회하기
# LIKE와 %로 특정 문자열을 포함하는 데이터 조회하기

# 첫 번째 글자가 A로 시작하는 데이터 조회
select * from customer where first_name LIKE 'A%';

# 첫 번째 글자가 AA로 시작하는 데이터 조회
select * from customer where first_name like 'AA%'

# A로 끝나는 모든 데이터 조회
select * from customer where first_name like '%A';

# RA로 끝나는 모든 데이터 조회
select * from customer where first_name like '%RA';

# A를 포함한 모든 데이터 조회
select * from customer where first_name like '%A%';

# 첫 번째 글자가 A로 시작하지 않는 데이터만 조회
select * from customer where first_name not like 'A%';

# ESCAPE로 특수 문자를 포함한 데이터 조회하기
# 특수 문자를 포함한 임의의 테이블 생성
with CTE (col_1) as (
    select 'A%BC' union ALL
    select 'A_BC' union ALL
    select 'ABC'
)

select * from CTE;

# 특수 문자 %를 포함한 데이터 조회
with CTE (col_1) as (
    select 'A%BC' union ALL
    select 'A_BC' union ALL
    select 'ABC'
)

SELECT * from CTE where col_1 like '%';

# ESCAPE로 특수 문자 %를 포함한 데이터 조회
with CTE (col_1) as (
    select 'A%BC' union ALL
    select 'A_BC' union ALL
    select 'ABC'
)

select * from CTE where col_1 like '%#%%' escape '#';