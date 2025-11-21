-- ===========================================================
-- 1. GROUP BY 문제
-- ===========================================================

use employees;

select * from employees.employees

-- ----------------------------------------------------------
-- G1. 성별별 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select gender, count(*) 'CNT'
from employees
group by gender;




-- ----------------------------------------------------------
-- G2. 부서별 현재 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select title, count(title)
from employees as em
INNER JOIN titles as ti
ON em.emp_no = ti.emp_no
group by title;



-- ----------------------------------------------------------
-- G3.직급별 직원 수 (전체 이력 기준)
-- 테이블: employees.title
-- ----------------------------------------------------------
select dept_no, count(dept_no)
from employees as em
INNER JOIN dept_emp as de
ON em.emp_no = de.emp_no
group by dept_no;


-- ----------------------------------------------------------
-- G4. 직급별 “현재” 직원 수
-- 테이블: employees.title
-- ----------------------------------------------------------
select dept_no, count(dept_no)
from employees as em
INNER JOIN dept_emp as de
ON em.emp_no = de.emp_no
group by dept_no;


-- ----------------------------------------------------------
-- G5.부서별 평균 급여 (현재 기준)
-- 테이블: employees.title
-- ----------------------------------------------------------
select title, salary
from titles as ti
INNER JOIN salaries as sl
ON ti.emp_no = sl.emp_no
group by title, salary;


-- ----------------------------------------------------------
-- G6.입사 연도별 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select year(hire_date), count(*)
from employees
group by year(hire_date);


-- ----------------------------------------------------------
-- G7.부서별 남녀 인원수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select dept_no, gender, count(*)
from employees as em
INNER JOIN dept_emp as de
ON em.emp_no = de.emp_no
group by dept_no, gender;


-- ----------------------------------------------------------
-- G8.부서별 평균 재직 일수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select dept_no, (to_date-from_date)
from employees as em
INNER JOIN dept_emp as de
ON em.emp_no = de.emp_no
group by dept_no, (to_date-from_date);


-- ----------------------------------------------------------
-- G9.직급별 평균 급여 (현재 직급 + 현재 급여)
-- 테이블: employees.employees
-- ----------------------------------------------------------
select title, salary
from titles as tl
INNER JOIN salaries as sl
ON tl.emp_no = sl.emp_no
group by title, salary;



-- ----------------------------------------------------------
-- G10.부서별 직원 수 + 전체 합계 
-- 테이블: employees.employees
-- ----------------------------------------------------------
select dept_no, count(*) "CNT"
from employees as em
INNER JOIN dept_emp as de
ON em.emp_no = de.emp_no
group by dept_no;
