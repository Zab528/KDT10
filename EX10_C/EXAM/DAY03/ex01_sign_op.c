/* *************************************************************
* Filename     : ex01_sign_op.c
* Description  : 단항 연산자 -> 부호 연산자
*				 - 부호 연산자 : 현재 부호를 반대로 변환
*				 + 부호 연산자 : 변환 없음
*				 ★ 컴파일러의 자동형변환 적용
*				    타입별 기본타입으로 형변환 진행
* History	   : 2025.12.30  BY LJG
* Note
* ***************************************************************/
// 라이브러리 로딩
#include <stdio.h>

int main(void)
{
	// 지역변수 선언
	int i, j;
	short s;

	// 지역변수 초기화 및 값 확인
	i = -10;
	i = +i;
	printf("i=%d\n", i);

	j = -10;
	j = -j;
	printf("j=%d\n", j);

	s = 10;
	printf("s=%d,  sizeof(s)=%d\n", s, sizeof(s));
	printf("+s=%d, sizeof(+s)=%d\n", +s, sizeof(+s));

	return 0;
}