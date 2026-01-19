/* *************************************************************
* Filename     : ex05_while.c
* Description  : 반복문 - do~while
*				 반복코드 수행 후에 조건 검사 진행
*				 반드시 코드 수행이 1회 진행됨!!!
* Author       : LJG
* History	   : 2026.01.02
* ***************************************************************/

// --------------------------------------------------------------
// Loading Library
// --------------------------------------------------------------
#include <stdio.h>			// C언어 표준입출력 라이브러리
#include <stdlib.h>			// C언어 표준라이브러리		 -> rand(), srand() 
#include <time.h>			// C언어 시간관련 라이브러리 -> time()

// --------------------------------------------------------------
// [실습] Up/Down 게임 만들기
// - 프로그램 지정 숫자 준비
// - 사용자가 입력한 숫자
// - 입력 숫자와 지정 숫자 비교해서 정보 제공 : Up/Down
// - 입력 숫자와 지정 숫자 동일하면 종료
// --------------------------------------------------------------
int main(void)
{
	// 지역변수 선언 및 초기화
	const int TARGET = 63;
	int		  user   = 0;

	// 프로그램 안내 메시지 출력
	printf("Up-Down Game");
	do {
		printf("0~100 범위의 정수 1개 입력:");
		scanf("%d", &user);

		if (user > TARGET)
			printf("Down number!");
		else if (user < TARGET)
			printf("Up number!");
	} while (TARGET != user);

	printf("Bing Go~!!\nGAME END");

	return 0;
}