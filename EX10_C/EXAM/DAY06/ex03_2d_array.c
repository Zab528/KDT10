/* *************************************************************
* Filename     : ex03_2d_array.c
* Description  : 2차원 배열의 행과 열 개수 계산
* Author       : LJG
* History	   : 2026-01-05
* ***************************************************************/

// --------------------------------------------------------------
// Loading Library : 전처리기에서 처리
// --------------------------------------------------------------
#include <stdio.h>

// --------------------------------------------------------------
// Entry Point [실습] 2차원 배열 선언 및 초기화
//					  행과 열 개수 계산
//					  5명 학생의 3과목 점수 저장
// --------------------------------------------------------------
int main(void) {
    // 변수 선언 + 초기화
    int jumsu[5][3] = { 0 };
    int total = 0;
    float avg = 0;

    const int ROWS = sizeof(jumsu) / sizeof(jumsu[0]);
    const int COLS = sizeof(jumsu[0]) / sizeof(jumsu[0][0]);

    printf(" 전체 배열의 크기: %llu bytes\n", (unsigned long long)sizeof(jumsu));   //sizeof(배열명)
    printf(" 행의 크기: %zu bytes\n", sizeof(jumsu[0]));      //sizeof(배열명[0])
    printf(" 요소의 크기: %zu bytes\n", sizeof(jumsu[0][0]));   //sizeof(배열병[0][0])

    // 점수 입력 받기 => 행 단위 즉, 한번에 3개 과목 점수 입력 받기
    for (int r = 0; r < ROWS; r++) {

        printf("\n %d번 학생의 국, 영, 수 점수 입력 (예: 90 80 50):", r + 1);
        /*for (int c = 0; c < COLS; c++)*/
        {
            int c = 0;
            if (scanf("%d %d %d", &jumsu[r][c], &jumsu[r][c + 1], &jumsu[r][c + 2]) != 3) return 0;
        }
    }
    // 학생 별로 합계, 평균 출력
    for (int r = 0; r < ROWS; r++) {

        for (int c = 0; c < COLS; c++)
            total += jumsu[r][c];

        avg = (float)total / COLS;
        printf("%d번 학생 합계 %d 평균 %f\n", r + 1, total, avg);

    }



    return 0;
}