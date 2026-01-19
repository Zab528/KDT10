/* *************************************************************
* Filename     : ex01_pointer.c
* Description  : 포인터 변수
* Author       : LJG
* History	   : 2026-01-07
* ***************************************************************/

// --------------------------------------------------------------
// Library			
// --------------------------------------------------------------
#include <stdio.h>

// --------------------------------------------------------------
// Entry Point Function
// --------------------------------------------------------------
int main(void)
{
	// 변수 선언 및 초기화
	int  value = 127;		// 데이터 저장 변수 선언 + 초기화
	char    ch = 'A';

	int* p;					// 데이터 주소 저장 변수 선언
	p = &value;				// 데이터 주소 저장 변수 초기화

	int* p2 = &value;		// 데이터 주소 저장 변수 선언 + 초기화
	char* p3 = &ch;

	// 변수 및 값 확인
	printf("변수 읽기 value : %d\n", value);

	printf("변수	 읽기 p : %p\n", p);		// 주소 저장하는 변수로 형식지정자 %p
	printf("변수 주소 읽기  : %p\n", &value);	// 변수 주소 읽어오기
	printf("변수    읽기 p2 : %p\n", p2);
	
	printf("포인터 변수로 데이터 읽기  *p : %d\n", *p);
	printf("포인터 변수로 데이터 읽기 *p2 : %d\n", *p2);

	// 변수들의 데이터 크기 확인 : sizeof()연산자
	printf("변수 value의 크기 : %zu bytes\n", sizeof(value));
	printf("변수    ch의 크기 : %zu bytes\n", sizeof(ch));
	printf("변수     p의 크기 : %zu bytes\n", sizeof(p));
	printf("변수    p2의 크기 : %zu bytes\n", sizeof(p2));
	printf("변수    p3의 크기 : %zu bytes\n", sizeof(p3));

	return 0;
}