/* *************************************************************
* Filename     : ex03_inc_desc_op.c
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
	int a = 5;
	int b = 3;
	int result;

	result = a * b + (++a);
	printf("결과 = %d\n", result);

	int c = 6;
	int d = 4;

	result = c * d + (c--);
	printf("결과 = %d\n", result);

	return 0;
}