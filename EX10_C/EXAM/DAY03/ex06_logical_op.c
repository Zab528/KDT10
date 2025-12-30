/* *************************************************************
* Filename     : ex06_logical_op.c
* Description  : 논리연산자
*				 && : AND 연산자 - 모든 조건이 True인 경우만 True
*				 || : OR  연산자 - 1개 이상 True면 True
*								   모든 조건이 False인 경우만 False
*				 동작방식
*				 첫번째 조건만 검사 후 빠르게 처리 가능함
*				 - && : 첫번째 조건이 False면 바로 False로 결론
*				 - || : 첫번째 조건이 True면 바로 True로 결론
* History	   : 2025.12.30  BY LJG
* Note
* ***************************************************************/
// 라이브러리 로딩
#include <stdio.h>

// 엔트피포인트 함수
int main(void)
{
	// 지역변수 선언 및 초기화
	int a = 5, b = 0;

	// && 연산 처리 결과
	printf("a=%d, b=%d\n", a, b);
	printf("a==0 && ++b 결과 : %d\n", a == 0 && ++b);

	// || 연산 처리 결과
	printf("\na=%d, b=%d\n", a, b);
	printf("a>0 || ++b 결과 : %d\n", a > 0 || ++b);

	printf("\na=%d, b=%d\n", a, b);
	printf("a==0 || ++b 결과 : %d\n", a == 0 || ++b);

	return 0;
}