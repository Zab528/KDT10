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

-- ========================================================================
-- GROUP BY 컬럼명1 , 컬럼명2, .. : 여러 개 컬럼으로 그룹화
-- ========================================================================
-- hometown, gender 그룹화
select hometown, gender, count(*) "인원수"
from user
group by hometown, gender
order by hometown;

-- hometown, gender 그룹화 후 성별이 남자인 그룹 데이터만 선택
select hometown, gender, count(*) "CNT"
from user
group by hometown, gender
having gender='남'