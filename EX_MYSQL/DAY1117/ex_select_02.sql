-- ========================================================================
-- 그룹화 : Group by 그룹화_기준_컬럼명
--         select 절에 집계함수 사용 : max()/min()/sum()/mean()..
-- ========================================================================
-- DB 선택
use sakila;

-- TB 선택 & 상세 설명 : desc/describe  TB_NAME
desc film;


-- ========================================================================
-- GROUP BY 컬럼명1 , 컬럼명2
-- ========================================================================
-- speical features 값 종류
select DISTINCT speical_features  from film;

-- special features 기준으로 그룹화
select special_features from film
from film
group by special_features;