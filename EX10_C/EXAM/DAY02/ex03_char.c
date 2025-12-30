/* *************************************************************
* Filename     : ex03_char.c
* Description  : 문자형 타입
*				 1바이트 정수 저장
*				 '문자1개' 입력 시 해당 코드값이 저장
*				 limits.h에서 문자형 타입의 최소/최대값 선언
*				 ASCII 코드표 기반 변환 진행
* History	   : 2025.12.29  BY LJG
* Note
* ***************************************************************/
// 라이브러리 로딩
#include <stdio.h>				// 입출력 함수들
#include <limits.h>				// 자료형의 최소/최대값

// 엔트리 포인트 함수 : OS에서 실행 시 호출하는 함수
int main(void)
{
	// 지역변수 선언 + 초기화
	unsigned char  code = ' ';   // 문자형 초기화 시에 ''만 지정 X
	unsigned char code2 = 0;    // 문자형 초기화 시에 숫자 지정 가능

	printf("code 값 : %c, %d, %x\n", code, code, code);

	code = 97;
	printf("code 값 : %c, %d, %x\n", code, code, code);

	code = -1;
	printf("code 값 : %c, %d, %x\n", code, code, code);

	return 0;
}