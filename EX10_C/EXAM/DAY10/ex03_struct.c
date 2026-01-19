/* *************************************************************
* Filename     : ex03_struct.c
* Description  : 회원정보 저장 및 확인
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
// - 회원 타입 구조체
//	 * 아이디
//	 * 비번
//	 * 이름
//	 * 나이
// - 날짜 타입 구조체
//	 * 년
//	 * 월
//	 * 일
// --------------------------------------------------------------
//- 날짜 타입
struct date {
	int  year;
	int month;
	int   day;
};

//- 사용자점수 타입
struct user {
	char userId[10];
	char userPW[10];
	char name[10];
	int age;
	struct date inputDate;
	struct date DueDate;
};

// - 타입 재정의
typedef struct user User;

// --------------------------------------------------------------
// Entry Point Function
//  - 회원은 2명
//	  * 1번째 회원은 생성과 동시에 초기화
//	  * 2번째 회원은 입력 받은 정보로 저장
// --------------------------------------------------------------
int main(void)
{
	// 변수 선언 및 초기화
	User s1 = { "ljg", "6414", "Lee", 26, {2026, 1, 1}, {2026, 2, 8} };

	// 사용자 정보 확인 출력
	printf("[s1] id:%s, pw:%s, name:%s, age:%d, in : %d-%d-%d, out : %d-%d-%d\n",
		s1.userId, s1.userPW, s1.name, s1.age,
		s1.inputDate.year, s1.inputDate.month, s1.inputDate.day,
		s1.DueDate.year, s1.DueDate.month, s1.DueDate.day);

	



	return 0;
}