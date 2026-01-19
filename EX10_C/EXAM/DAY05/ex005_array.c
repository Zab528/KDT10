/* *************************************************************
* Filename     : ex05_array.c
* Description  : 입력받은 값으로 배열 초기화
*				 합계, 평균 계산 출력
* Author       : LJG
* History	   : 2026.01.02
* ***************************************************************/
// --------------------------------------------------------------
// Loading Library
// --------------------------------------------------------------
#include <stdio.h>

int main(void)
{
	//  선언 및 초기화
	int		score[5] = { 0 };
	int		sum = 0;
	float	avg = 0;
	const int LEN = sizeof(score) / sizeof(score[0]);

	// 배열 값 입력 받아서 저장
	for (int idx = 0; idx < LEN; idx++)
	{
		printf("%d번 원소 입력:", idx);
		scanf("%d", &score[idx]);
	}

	// 배열 값 확인 => 원소값 출력해주는 함수
	for (int idx = 0; idx < LEN; idx++)
	{
		printf("%d번 원소 확인: %d\n", idx, score[idx]);
	}

	// 합계 => 원소의 
	for (int idx = 0; idx < LEN; idx++)
		sum += score[idx];

	// 평균과 합계 출력
	printf("합계 : %d, 평균 : %f\n", sum, (float)sum / LEN);
	
	return 0;
}