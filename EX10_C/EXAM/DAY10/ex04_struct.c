/* *************************************************************
* Filename     : ex04_struct.c
* Description  : 구조체 포인터
* Author       : LJG
* History	   : 2026-01-12
* ***************************************************************/

// --------------------------------------------------------------
// Library			
// --------------------------------------------------------------
#include <stdio.h>
#include <string.h>

// --------------------------------------------------------------
// User Define Type
// --------------------------------------------------------------
//- 날짜 타입
struct date {
	int  year;
	int month;
	int   day;
};

//- 사용자점수 타입
struct userScore {
	char userId[8];
	struct date inputDate;
	struct date changeDate;
};

// - 타입 재정의
typedef struct userScore UserScore;

// --------------------------------------------------------------
// Entry Point Function
// --------------------------------------------------------------
int main(void)
{
	// 변수 선언 및 초기화
	UserScore  s1 = { "s1", {2026, 1, 1}, {2026, 2, 1} };
	UserScore  s2 = s1;
	UserScore* pS = &s1;

	// 사용자 정보 확인 출력 : 구조체 변수로 직접 접근 -> 점(.)연산자
	printf("[s1] id:%s, in : %d - %d - %d, change : %d - %d - %d\n",
		s1.userId,
		s1.inputDate.year, s1.inputDate.month, s1.inputDate.day,
		s1.changeDate.year, s1.changeDate.month, s1.changeDate.day);

	// 사용자 정보 확인 출력 : 구조체 포인터로 간접 접근 -> 화살표(->)연산자
	printf("[s1] id:%s, in : %d - %d - %d, change : %d - %d - %d\n",
		pS->userId,
		pS->inputDate.year,  pS->inputDate.month,  pS->inputDate.day,
		pS->changeDate.year, pS->changeDate.month, pS->changeDate.day);

	// 사용자 정보 변경
	strcpy(s1.userId, "newID");  //s1.userId = "newID"; <- 배열 선언과 동시에 초기화때만 가능
	s1.inputDate.year = 2025;
	s1.changeDate.year = 2025;
	s1.changeDate.month = 12;


	return 0;
}