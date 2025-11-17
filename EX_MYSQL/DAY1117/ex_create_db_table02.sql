-- ======================================================
-- 실습용 DB : MYDB
--       TB : User 
-- ======================================================
-- DB 생성
CREATE DATABASE IF NOT EXISTS doitsql;

-- DB 선택
USE doitsql;

-- TB 생성
CREATE TABLE IF NOT EXISTS doit_tb
(
    col_1 int PRIMARY KEY AUTO_INCREMENT,      
    col_2 VARCHAR(50),
    col_3 int
);

-- TB 확인
SHOW TABLES;

-- TB의 구조 확인
desc doit_tb;

-- 데이터 추가
INSERT INTO doit_tb VALUES
(1, "TEST", 10);

-- AUTO_INCREMENT 자동증가
insert into doit_tb (col_2, col_3)
VALUES ('OK', 100);

insert into doit_tb (col_2, col_3)
VALUES ('OK', 100),
       ('Yes', 90)
       ("Good", 1);

INSERT INTO doit_tb VALUES
(8, "TEST", 10);

-- 전체 데이터 조회
select * from doit_tb;

-- 현재 마지막 AE값 확인
SELECT LAST_INSERT_ID() '마지막 AE 번호';

