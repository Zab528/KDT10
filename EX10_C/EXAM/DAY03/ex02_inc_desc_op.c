/* *************************************************************
* Filename     : ex02_inc_desc_op.c
* Description  : 단항 연산자 -> 증감 연산자
*				 ++ 연산자 : 현재 값을 1 증가
*				 -- 연산자 : 현재 값을 1 감소
*				 ★ 변수/피연산자 값을 변경하는 연산자
* History	   : 2025.12.30  BY LJG
* Note
* ***************************************************************/
// 라이브러리 로딩
#include <stdio.h>

// 엔트피포인트 함수
int main(void)
{
	// 지역변수 선언 및 초기화
	int num1 = 5, num2 = 0;
	
	// (1) 선증감 & 후증감 연산 수행 - 단독
	++num1;
	num2 = num1;

	num1++;
	num2 = num1;

	printf("단독 증감연산자 수행 : num1 %d, num2 %d\n", num1, num2);

	// (2) 선증감 & 후증감 연산 수행 - 수식
	num1 = 5, num2 = 0;
	num2 = ++num1;    // ① ++num1; ②num2=num1;
	printf("수식 증감연산자 수행 : num1 %d, num2 %d\n", num1, num2);

	num2 = num1++;    // ① num2=num1; ②num1++;
	printf("수식 증감연산자 수행 : num1 %d, num2 %d\n", num1, num2);

	// (3) 선증감 & 후증감 연산 수행 - 함수 인자
	num1 = 5, num2 = 0;
	printf("함수 인자 증감연산자 수행 : ++num1 %d, num2++ %d\n", ++num1, num2++);
	printf("함수 인자 증감연산자 수행 : num1 %d, num2 %d\n", num1, num2);

	return 0;
}