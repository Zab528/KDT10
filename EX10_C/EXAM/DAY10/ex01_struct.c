/* *************************************************************
* Filename     : ex01_struct.c
* Description  : 구조체
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
//- 학생 정보 타입
struct student {
	int  no;
	char name[30];
	int  kor, math, eng;
};

// - 사람 타입
struct person {
	char  name[30];
	int   age;
	float height;
	float weight;
	char  blood;
	char  gender;
};
// - 타입 재정의
typedef struct person Person;

// --------------------------------------------------------------
// Entry Point Function
// --------------------------------------------------------------
int main(void)
{
	// 변수 선언 및 초기화
	struct student std1 = { 1, "Hong", 100, 90, 80 };
	struct student std2 = { 2, "Kim", 90, 70, 80 };

	Person kim = { 0 };
	Person park = { "박찬호", 10, 180.4, 76.3, 'A', 'F' };

	// 배열 선언과 동시에 초기화
	char  msg1[10] = "Good";					//-> 컴파일러가 요소 1개 1개 넣어줌
	char  msg2[] = { 'H','E','L','L','O','\0' };
	char  msg3[10];

	// 선언과 동시에 초기화 시만 가능
	//msg3 = "Happy";
	//msg3 = { 'H','E','L','L','O','\0' };
	for (int i = 0; i < 10; i++)
		msg3[0] = 'H';

	// 속성 확인
	printf("학번 : %d, 이름 : %s, 국어 : %d\n", std1.no, std1.name, std1.kor);
	printf("이름 : %s, 나이 : %d, 키 : %.f, 몸무게 : %.f, 혈액형 : %c\n",
		    park.name, park.age, park.height, park.weight, park.blood);

	// 속성 변경 : 구조체 변수명.속성명 = 새로운값;
	park.age   = 11;
	park.blood = 'O';
	//park.name = "박혁거세";
	strcpy(park.name, "박혁거세");

	printf("이름 : %s, 나이 : %d, 키 : %.f, 몸무게 : %.f, 혈액형 : %c\n",
		park.name, park.age, park.height, park.weight, park.blood);

	return 0;
}