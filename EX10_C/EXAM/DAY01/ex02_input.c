/* **********************************************
* Filename	   : ex02_input.c
* Description  : 표준 입력 함수 중 대표 함수 실습 - scanf()
* DATE		   : 2025-12-16
* Note		   : 
* - 실습용
************************************************/
// 라이브러리 로딩
//#pragma warning(disable: 4996)
#include <stdio.h>

// 전역변수

// 사용자 정의 함수

// 엔트리포인트 함수
int main(void) {

	// 프롬프트 출력
	printf("나이 입력 받기 : ");

	// 입력받기
	int  age = 0;
	scanf("%d", &age);

	// 입력 확인
	printf("당신의 나이는 %d이군요.", age);

	
	// 정상 종료 의미 0 반환 => 운영체제에게 반환
	return 0;
}
