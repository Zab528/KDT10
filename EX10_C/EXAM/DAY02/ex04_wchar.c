/* *************************************************************
* Filename     : ex04_wchar.c
* Description  : 확장문자형 타입
*				 ASCII 코드 제외한 기업/국가에서 추가한 문자 저장 타입
*				 Windows는 2바이트에 저장 / Linux는 4바이트에 저장
* History	   : 2025.12.29  BY LJG
* Note
* ***************************************************************/
// 라이브러리 로딩
#include <stdio.h>				// 입출력 함수들
#include <wchar.h>
#include <locale.h>

// 엔트리 포인트 함수 : OS에서 실행 시 호출하는 함수
int main(void)
{
	wchar_t wch = L'가';							// 확장문자형 변수 선언

	setlocale(LC_ALL, "Korean");					// 지역설정 - 시스템 설정
	const char* loc = setlocale(LC_ALL, "");		// 시스템 기본 로케일
	printf("setlocale = %s\n", loc ? loc : "(null");

	//printf("wchar => %lc\n", wch);				// 확장 문자형 출력 X
	wprintf(L"wchar => %lc\n", wch);

	return 0;
}