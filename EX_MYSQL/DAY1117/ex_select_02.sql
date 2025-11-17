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
select DISTINCT special_features from film;

-- special features 기준으로 그룹화
select special_features
from film
group by special_features;



select special_features, count(special_features)
from film
group by special_features;


-- GROUP BY 컬럼명1 , 컬럼명2, .. : 여러 개 컬럼으로 그룹화
-- ========================================================================
-- special features, rating
select DISTINCT rating
from film;

-- special features, rating 그룹화
select special_features, rating
from film
group by special_features, rating;

-- special features, rating 그룹별 소속된 행수
select special_features, rating, count(rating)
from film
group by special_features, rating;

-- rating, special features 그룹화
select special_features, rating, count(rating)
from film
group by rating, special_features;


-- ========================================================================
-- count() 집계함수와 정렬 order by
-- ========================================================================
-- special features 그룹별 소속된 행 개수 파악 개수 파악
select special_features, count(special_features) "CNT"
from film
group by special_features;


-- special features 그룹별 소속된 행 개수 파악 개수 파악
select special_features, count(special_features) "CNT"
from film
group by special_features
order by cnt desc, special_features desc 
limit 5;