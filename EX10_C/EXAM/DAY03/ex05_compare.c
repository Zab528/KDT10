/* *************************************************************
* Filename     : ex05_compare.c
* Description  : 비교연산자 - 문자열
*				 string.h => strXXXX( )
* History	   : 2025.12.30  BY LJG
* Note
* ***************************************************************/
// 라이브러리 로딩
#include <stdio.h>
#include <string.h>

// 엔트피포인트 함수
int main(void)
{
	// 지역변수 선언 및 초기화
	char str[] = "abc";

	printf("\"abc\"==\"abc\" ? %d\n",  "abc"=="abc");
	printf("  str==\"abc\" ? %d\n", str == "abc");
	printf("strcmp(str, \"abc\") ? %d\n", strcmp(str, "abc"));
	printf("strcmp(str, \"abb\") ? %d\n", strcmp(str, "abb"));
	printf("strcmp(str, \"abd\") ? %d\n", strcmp(str, "abd"));

	return 0;
}