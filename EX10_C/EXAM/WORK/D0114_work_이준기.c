/* **********************************************
* Filename	   : ex03_input.c
* Description  : 표준 입력 함수 중 대표 함수 실습 - scanf()
* DATE		   : 2025-12-16
* Note		   :
* - 변수 주소 확인 연산자 &
* - 다양한 타입별 입력 받고 저장하기
* - 입력 결과 파일 저장
************************************************/

// 라이브러리 로딩
#include <stdio.h>

// 엔트리포인트 함수
int main(void) {

	// 입력 데이터 저장용 변수 : 지역변수
	int   age = 0;
	int   score = 0;
	float height = 0;

	FILE* fp = NULL;   // 파일 포인터

	// 변수 주소 출력
	printf("age변수 주소 : %p\n", &age);

	// 키보드로 입력 받은 데이터 저장
	printf("나이: ");
	if (scanf("%d", &age) != 1)
		return 0;

	printf("당신의 나이는 %d세이군요!\n", age);

	// 여러 개 입력
	printf("나이, 점수, 키 : ");
	if (scanf("%d %d %f", &age, &score, &height) != 3)
		return 0;

	printf("당신의 나이는 %d세. 점수는 %d점. 키는 %.1fcm이군요!\n",
		age, score, height);

	// ===============================
	// 파일 저장
	// ===============================
	fp = fopen("input_result.txt", "w");  // w : 새로 쓰기

	if (fp == NULL) {
		printf("파일 열기 실패\n");
		return 0;
	}

	fprintf(fp, "입력 결과\n");
	fprintf(fp, "나이   : %d세\n", age);
	fprintf(fp, "점수   : %d점\n", score);
	fprintf(fp, "키     : %.1fcm\n", height);

	fclose(fp);

	printf("입력 결과가 파일에 저장되었습니다.\n");

	return 0;
}
