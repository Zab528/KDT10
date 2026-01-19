/* *************************************************************
* Filename     : ex06_func_pointer.c
* Description  : 함수 포인터
*				 함수 주소를 저장하는 포인터
*				 형식 :  반환자료형  (*포인터이름)(매개변수자료형, ...);
* Author       : LJG
* History	   : 2026-01-08
* ***************************************************************/

// --------------------------------------------------------------
// Library			
// --------------------------------------------------------------
#include <stdio.h>

// --------------------------------------------------------------
// Entry Point Function
// --------------------------------------------------------------
int add(int x, int y)
{
	return x + y;
}

int pow(int x, int y)
{
	return x * y;
}

int sub(int x, int y)
{
	return x - y;
}

void msg()
{
	printf("Good Luck!");
}

float div(int x, int y)
{
	return (float)x / y;
}

// --------------------------------------------------------------
// Entry Point Function
// --------------------------------------------------------------
int main(void)
{
	// 함수 포인터 변수 선언 및 초기화
	int (*pAdd)(int, int) = add;
	float (*pDiv)(int, int) = div;
	void (*pMsg)() = msg;
	int (*pFunc[3])(int, int) = { add, pow, sub };



	// 함수이름과 포인터 저장값 확인
	printf("add Func : %p,  pAdd : %p\n", add, pAdd);

	// 함수 실행
	printf(" pAdd(10,20) : %d\n", pAdd(10, 20));
	printf(" pDiv(10, 3) : %f\n", pDiv(10, 3));
	printf(" pFunc[0]    : %d\n", pFunc[0](10, 20));
	pMsg();

	return 0;
}