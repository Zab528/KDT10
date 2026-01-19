/* *************************************************************
* Filename     : ex05_static.c
* Description  : 정적 변수 static variable
*				 static 전역변수 : 다른 파일에서 extern 즉, 참고 불가!
*				 static 지역변수 : 함수 종료 후에도 유지.
* Author       : LJG
* History	   : 2026-01-06
* ***************************************************************/
// --------------------------------------------------------------
// Library			<- preprocessor
// --------------------------------------------------------------
#include <stdio.h>

static int sv;

// --------------------------------------------------------------
// User Define Function
// --------------------------------------------------------------
void func1(void)
{
	static int sv2 = 1;
	int		   lv = 1;

	printf("[func1] sv2 = %d, lv = %d\n", sv2++, lv++);
}

void func1(void)
{
	static int sv2 = 1;		// 생성된 후 1회 초기화, 메모리 유지, 해당 함수에서만 사용가능
	int		   lv  = 1;

	printf("[func1] sv2= %d, lv = %d\n", sv2++, lv++);
}

void func2(void)
{
	sv = 100;		// 전역변수 사용
	printf("[func2] sv = %d\n", sv);
	//printf("[func2] static 지역변수 sv2 = %d\n", sv2);
}

// --------------------------------------------------------------
// Entry Point Function
// --------------------------------------------------------------
int main(void)
{
	func1();
	func1();
	func1();
	func2();

	return 0;
}