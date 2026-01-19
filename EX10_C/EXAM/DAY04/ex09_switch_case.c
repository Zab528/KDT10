/* *************************************************************
* Filename     : ex08_switch_case.c
* Description : switch ~ case 다중조건 처리문
*               if ~ else if ~ else 동일 가능
*               제약조건 => 정수, 상수만 가능함!
* Author       : LJG
* History	   : 2025.12.31
* ***************************************************************/
// --------------------------------------------------------------
// 라이브러리 로딩
// --------------------------------------------------------------
#include <stdio.h>

// --------------------------------------------------------------
// 엔트피포인트 함수
// [실습] 학점 출력 => 점수 입력 받으면 학점 출력하기
//		 A, B, C, D, F
// --------------------------------------------------------------
int main(void)
{
	// 지역변수 선언 및 초기화
	int		score = 0;
	char	grade = 0;		// 1byte 정수 저장

	// 점수 입력 받기
	printf("점수 입력:");
	if (scanf("%d", &score) != 1)
	{
		printf("입력이 올바르지 않습니다.");
		return 0;					// 종료
	}

	// 점수에 따른 학점 출력
	if (score >= 90)
		grade = 'A';
	else if (score >= 80)
		grade = 'B';
	else if (score >= 70)
		grade = 'C';
	else if (score >= 60)
		grade = 'D';
	else
		grade = 'F';

	printf("당신의 학점은 %c입니다.", grade);

	// 점수에 따른 학점 출력 : switch_case
	switch (score/10)
	{
	case 10:
	case 9:	grade = 'A';	break;

	case 8:	grade = 'B';	break;

	case 7:	grade = 'C';	break;

	case 6:	grade = 'D';	break;

	default:
		grade = 'F';
	}


	// 출력
	printf("당신의 학점은 %c입니다.", grade);

	return 0;
}