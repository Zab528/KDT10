/* *************************************************************
* Filename     : ex06_struct.c
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
// - 학생 타입
struct student {
	int no;
	int kor, eng, math;
};

// --------------------------------------------------------------
// User Define Function
// --------------------------------------------------------------
// 함수기능 : 구조체 속성/필드 출력 기능
// 함수이름 : printAttr
// 매개변수 : Student std
// 반환결과 : 없음
// --------------------------------------------------------------
void printAttr(Student std)
{
	printf(" %d, %d, %d, %d\n", std.no, std.kor, std.eng, std.math);
}

// --------------------------------------------------------------
// 함수기능 : 구조체 속성/필드 출력 기능
// 함수이름 : printField
// 매개변수 : Student* ptr
// 반환결과 : 없음
// --------------------------------------------------------------
void printField(const Student *const ptr)
{
	printf(" %d, %d, %d, %d\n", ptr->no, ptr->kor, ptr->eng, ptr->math);
	Student ss = { 0 };
	//ptr = &ss;

	//ptr->math = 77;
	//ptr->kor = 92;
}

typedef struct student Student;
// --------------------------------------------------------------
// Entry Point Function
// --------------------------------------------------------------
int main(void)
{
	// 변수 선언 및 초기화
	Student  st1 = { 1, 100, 100, 100 };
	Student* pst = &st1;

	Student  st2 = *pst;	// *&st1;

	// call by Value
	printAttr(st1);
	printf("[st1] %d, %d, %d, %d\n", st1.no, st1.kor, st1.eng, st1.math);

	// call by Reference
	printField(&st1);
	printf("[st1] %d, %d, %d, %d\n", st1.no, st1.kor, st1.eng, st1.math);

	return 0;
}