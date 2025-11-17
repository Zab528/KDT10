-- ========================================================================
use mydb;

-- hometown 값 종류
select DISTINCT hometown from user;

-- hometown 기준으로 그룹화
select hometown, count(hometown)
from user
group by hometown;


-- 그룹별 행 수
select hometown, count(hometown)
from user
group by hometown;

-- ========================================================================
-- GROUP BY 컬럼명1 , 컬럼명2, .. : 여러 개 컬럼으로 그룹화
-- ========================================================================
-- hometown, gender 그룹화
select hometown, gender
from user
group by hometown, gender;


-- 그룹별 행 수, gender 정렬
select hometown, gender, count(gender)
from user
group by hometown, gender
order by gender ASC;