/* *************************************************************
* Filename     : ex01_sizeof.c 
* Description  : C언어에서 자료형별 사용 메모리 크기 확인
* History	   : 2025.12.29  BY LJG 
* Note
* ***************************************************************/
// 라이브러리 로딩
#include <stdio.h>				// 입출력 함수들


// 엔트리 포인트 함수 : OS에서 실행 시 호출하는 함수
int main(void)
{
	int i = 100;

	printf("sizeof i            =%d bytes\n", sizeof i);
	printf("sizeof (char)       =%d bytes\n", sizeof(char));
	printf("sizeof (short)      =%d bytes\n", sizeof(short));
	printf("sizeof (int)        =%d bytes\n", sizeof(int));
	printf("sizeof (long)       =%d bytes\n", sizeof(long));
	printf("sizeof (long long)  =%d bytes\n", sizeof(long long));
	printf("sizeof (float)      =%d bytes\n", sizeof(float));
	printf("sizeof (double)     =%d bytes\n", sizeof(double));
	printf("sizeof (long double)=%d bytes\n", sizeof(long double));

	return 0;
}