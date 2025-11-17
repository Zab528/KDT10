-- Active: 1763095341790@@127.0.0.1@3306@sakila
-- =========================================================
-- JOIN : 테이블 조합으로 원하는 데이터 추출/선택
--        종류 : 내부(INNER) / 외부(OUTER)
-- =========================================================
-- DB 선택 및 TB 생성
-- =========================================================
-- DB 선택
use sakila;

-- =========================================================
-- 데이터 조회
-- =========================================================

-- [내부조인] / 교집합과 동일
-- [내부 조인]  / Equi Join : 두개 TB에 기준 컬럼의 값이 동일한 것만 선택
--               customer TB, address TB
--              고객정보의 상세 주소 정보 출력
SELECT customer.first_name, customer.last_name, address.address
FROM customer INNER JOIN address
ON customer.customer_id = address.address_id;


-- [내부 조인]  / Equi Join : 두개 TB에 기준 컬럼의 값이 동일한 것만 선택
--               customer TB => cu, address TB => ad, city TB => ci
--              고객정보의 도시명, 상세 주소 정보 선택
SELECT cu.first_name, cu.last_name, ci.city, ad.address, ad.address2
from customer as cu 
    INNER JOIN address as ad ON cu.address_id = ad.address_id
    INNER JOIN city as ci ON ci.city_id = ad.city_id;