/* *************************************************************
* Filename     : ex02_int.c
* Description  : 정수형 타입별 최소/최대값 체크
*				 limits.h
* History	   : 2025.12.29  BY LJG
* Note
* ***************************************************************/
// 라이브러리 로딩
#include <stdio.h>				// 입출력 함수들
#include <limits.h>				// 자료형의 최소/최대값

// 엔트리 포인트 함수 : OS에서 실행 시 호출하는 함수
int main(void)
{
	printf("----------------------------\n");
	printf("[정수형 타입의 값 범위 체크]\n");
	printf("----------------------------\n");

	printf("  short 타입 : %d ~ %d\n", SHRT_MIN, SHRT_MAX);
	printf("u short 타입 :  0 ~ %d, %hu\n\n", USHRT_MAX, USHRT_MAX);

	printf("    int 타입 : %d ~ %d\n", INT_MIN, INT_MAX);
	printf("u   int 타입 :  0 ~ %d, %u\n\n", UINT_MAX, UINT_MAX);

	printf("   long 타입 : %ld ~ %ld\n", LONG_MIN, LONG_MAX);
	printf("u   int 타입 :  0 ~ %lu\n\n", ULONG_MAX);

	printf("    long long 타입 : %lld ~%lld\n", LLONG_MIN, LLONG_MAX);
	printf("u   long long 타입 :   0 ~ %llu\n\n", ULLONG_MAX);

	return 0;
}