/* *************************************************************
* Filename     : ex03_pointer.c
* Description  : 포인터 변수의 연산
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
	char* p = &value;		// 데이터 주소 저장 변수 선언

	// 증감연산자 & 포인터 : 주소 증감
	printf("p    : 0x%p, %llu\n", p, (unsigned long long)p);
	p++;
	printf("p    : 0x%p, %llu\n", p, (unsigned long long)p);
	++p;
	printf("p    : 0x%p, %llu\n\n", p, (unsigned long long)p);
	
	p--;
	printf("p    : 0x%p, %llu\n", p, (unsigned long long)p);
	--p;
	printf("p    : 0x%p, %llu\n", p, (unsigned long long)p);

	return 0;
}