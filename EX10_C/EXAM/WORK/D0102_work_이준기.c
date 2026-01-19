/* *************************************************************
* Filename     : D1231_work_이준기
* Description  : p270 ~ p282
* Author       : LJG
* History	   : 2026.01.02
* ***************************************************************/
// --------------------------------------------------------------
// 라이브러리 로딩
// --------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#define LEN 10


// --------------------------------------------------------------
// 엔트피포인트 함수
// --------------------------------------------------------------
int main(void)
{
	// 예제 5-6
	/*int score[] = { 100, 88, 100, 100, 90 };
	const int LEN = sizeof(score) / sizeof(score[0]);

	int	   i, sum = 0;
	float average = 0.0f;

	for (i = 0; i < LEN; i++)
	{
		sum += score[i];
		printf("score[%d]=%d\tsum%d\n", i, score[i], sum);
	}

	average = sum / (float)LEN;

	printf("총점 : %d\n",    sum);
	printf("평균 : %4.1f\n", average);*/


	// Quiz 5-3
	/*int arr[] = { 10, 20, 30, 40, 50, 60, 70 };
	const int LEN = sizeof(arr) / sizeof(arr[0]);
	
	int sum1 = 0;
	int sum2 = 0;

	for (int i = 0; i < LEN; i++)
	{
		if (i % 2 == 1) sum1 += arr[i];
		else sum2 += arr[i];
	}

	printf("짝수 합 : %d\n", sum1);
	printf("홀수 합 : %d", sum2);*/


	// 예제 5-7
	/*int score[] = { 79,88,91,33,100,55,95 };

	int max = score[0];
	int min = score[0];

	const int LEN = sizeof(score) / sizeof(score[0]);
	int i;

	for (i = 1; i < LEN; i++) {
		if (score[i] > max)
			max = score[i];
		else if (score[i] < min)
			min = score[i];
	}

	printf("최대값 : %d\n", max);
	printf("최소값 : %d\n", min);*/


	// 예제 5-8
	/*int numArr[10];
	const int LEN = sizeof(numArr) / sizeof(numArr[0]);
	int i, n, tmp;

	srand((unsigned)time(NULL));

	for (i = 0; i < LEN; i++) {
		numArr[i] = i;
		printf("%d", numArr[i]);
	}
	printf("\n");

	for (i = 0; i < LEN; i++) {
		n = rand() % 10;

		tmp = numArr[0];
		numArr[0] = numArr[n];
		numArr[n] = tmp;
	}

	for (i = 0; i < LEN; i++) {
		printf("%d", numArr[i]);
	}
	printf("\n");*/


	// 예제 5-9
	/*int ball[45];
	const int LEN = sizeof(ball) / sizeof(ball[0]);
	int i, n, tmp;

	srand((unsigned)time(NULL));

	for (i = 0; i < LEN; i++)
		ball[i] = i + 1;

	for (i = 0; i < LEN; i++) {
		n = rand() % LEN;

		tmp = ball[i];
		ball[i] = ball[n];
		ball[n] = tmp;
	}

	for (i = 0; i < 6; i++)
		printf("ball[%d]=%d\n", i, ball[i]);*/


	// Quiz 5-4
	/*int num[9];
	const int LEN = sizeof(num) / sizeof(num[0]);
	int i, n, tmp;

	srand((unsigned)time(NULL));

	for (i = 0; i < LEN; i++)
		num[i] = i + 1;

	for (i = 0; i < LEN; i++) {
		n = rand() % LEN;

		tmp = num[i];
		num[i] = num[n];
		num[n] = tmp;
	}

	for (i = 0; i < 3; i++)
		printf("num[%d]=%d\n", i, num[i]);*/


	// 예제 5-10
	/*int code[] = { -4, -1, 3, 6, 11 };
	int arr[LEN], i, tmp;
	const int CODE_LEN = sizeof(code) / sizeof(code[0]);

	srand((unsigned)time(NULL));

	for (i = 0; i < LEN; i++) {
		tmp = rand() % CODE_LEN;
		arr[i] = code[tmp];
	}

	for (i = 0; i < LEN; i++)
		printf("arr[%d]=%d\n", i, arr[i]);*/


	// 예제 5-11
	/*int numArr[10];
	const int LEN = sizeof(numArr) / sizeof(numArr[0]);
	int i, j, k, tmp;

	int chk;

	srand((unsigned)time(NULL));

	for (i = 0; i < LEN; i++) {
		numArr[i] = rand() % 10;
		printf("%d", numArr[i]);
	}
	printf("\n");

	for (i = 0; i < LEN; i++) {
		chk = 0;
		for (j = 0; j < LEN - 1 - i; j++) {
			if (numArr[j] > numArr[j + 1]) {
				tmp = numArr[j];
				numArr[j] = numArr[j + 1];
				numArr[j + 1] = tmp;

				chk = 1;
			}
		}
		if (chk == 0) break;

		for (k = 0; k < LEN; k++)
			printf("%d", numArr[k]);
		printf("\n");
	}*/


	// Quiz 5-5
	/*int iArr[] = { 3,7,2,4,1,5,6 };
	const int LEN = sizeof(iArr) / sizeof(iArr[0]);
	int i, j, chk, tmp;

	for (i = 0; i < LEN; i++) {
		chk = 0;
		for (j = 0; j < LEN - 1 - i; j++) {
			if (iArr[j] < iArr[j + 1]) {
				tmp = iArr[j];
				iArr[j] = iArr[j + 1];
				iArr[j + 1] = tmp;

				chk = 1;
			}
		}
		if (chk == 0) break;
	}
	for (i = 0; i < LEN; i++) {
		printf("%d", iArr[i]);
	}*/


	// 예제 5-12
	/*int number[10];
	int counter[10] = { 0 };
	const int LEN = sizeof(number) / sizeof(number[0]);
	int i;

	srand((unsigned)time(NULL));

	for (i = 0; i < LEN; i++) {
		number[i] = rand() % 10;
		printf("%d", number[i]);
	}
	printf("\n");

	for (i = 0; i < LEN; i++) {
		counter[number[i]]++;
	}

	for (i = 0; i < LEN; i++) {
		printf("%d의 개수 : %d\n", i, counter[i]);
	}*/

	return 0;
}