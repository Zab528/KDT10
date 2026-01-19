/* *************************************************************
* Filename     : ex03_array.c
* Description  : 배열의 요소 개수
* Author       : LJG
* History	   : 2026.01.02
* ***************************************************************/
// --------------------------------------------------------------
// Loading Library
// --------------------------------------------------------------
#include <stdio.h>


// --------------------------------------------------------------
// 배열 요소개수 계산
// --------------------------------------------------------------
int main(void)
{
	// 선언 및 초기화
	int	   score[5] = { 90, 80, 50, 80,100 };
	short  nums[] = { 11,22,33,44,55,66,77,88,99,0,9,8,7,6,5,4,3,2,1 };

	// 배열의 요소 개수 및 배열 전체 사용 메모리 크기 출력
	int cnt = 0, totalBytes = 0;

	cnt = sizeof(score) / sizeof(score[0]);
	totalBytes = cnt * sizeof(score[0]);

	printf("score 배열 요소 : %d개, 총 사용 메모리 : %dbytes, %llubytes", 
			cnt, totalBytes, sizeof(score));

	cnt = sizeof(nums) / sizeof(nums[0]);
	totalBytes = cnt * sizeof(nums[0]);

	printf("nums 배열 요소 : %d개, 총 사용 메모리 : %dbytes, %llubytes",
		cnt, totalBytes, sizeof(nums));

	return 0;
}