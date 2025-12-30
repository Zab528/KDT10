/* **********************************************
* Filename	   : ex03_input.c
* Description  : 표준 입력 함수 중 대표 함수 실습 - scanf()
* DATE		   : 2025-12-16
* Note		   :
* - 변수 주소 확인 연산자 &
* - 다양한 타입별 입력 받고 저장하기
************************************************/
// 라이브러리 로딩
#include <stdio.h>

// 전역변수

// 사용자 정의 함수

// 엔트리포인트 함수
int main(void) {

	// 입력 데이터 저장용 변수 : 지역변수
	int   age    = 0;
	int   score  = 0;
	float height = 0;

	// 변수 주소 출력 : &변수명
	// 주소 저장 타입 point => %p 
	printf("age변수 주소 : %d, %p\n", &age, &age);

	// 키보드로 입력 받은 데이터 저장 및 확인 => 1개 입력 저장
	printf("나이:");							//- 입력 요청 프롬프르
	if (scanf("%d", &age) != 1)					//- 입력&저장 체크
		return 0;

	printf("당신의 나이는 %d세이군요!\n", age);	//- 입력 확인

	// 키보드로 입력 받은 데이터 저장 및 확인 => 3개 입력 저장
	printf("나이, 점수, 키 : ");					
	if (scanf("%d %d %f", &age, &score, &height) != 3)				
		return 0;

	printf("당신의 나이는 %d세. 점수는 %d점. 키는 %.1fcm이군요!", age, score, height);

	return 0;
}
