/* *************************************************************
* Filename     : D0107_work_이준기
* Description  : 7장 포인터
*				 p428 ~ p480 (더블포인터 제외)
* Author       : LJG
* History	   : 2026.01.07
* ***************************************************************/
// --------------------------------------------------------------
// 라이브러리 로딩
// --------------------------------------------------------------
#include <stdio.h>


// --------------------------------------------------------------
// [실습]
// --------------------------------------------------------------
// Quiz 7-1
// -> 64비트 OS는 주소 표현에 8비트를 사용하기 때문에 2^64 -1 만큼의 메모리 다룰 수 있다.


// 예제 7-1
//int main(void) {
//	int  i = 5;
//	int* p = &i;
//
//	printf("i =%d\n", i);                   
//	printf("&i=%p\n", &i);                 
//	printf("p =%p\n", p);         
//	printf("&p=%p\n", &p);                  
//
//	return 0;
//}


// 예제 7-2
//int main(void) {
//	int  i = 200;
//	int* ptr = &i;
//
//	*ptr = *ptr + 1;
//
//	printf("i    =%d\n", i);
//	printf("*ptr =%d\n", *ptr);
//	printf("&i   =%p\n", &i);
//	printf("ptr  =%p\n", ptr);
//
//	return 0;
//}


// Quiz 7-2
//200
//100
//200
//i의 주소
//i의 주소


// 예제 7-3
//int main(void) {
//	int  i = 200;
//	int* ptr = &i;
//
//	printf("  i   =%d\n", i);
//	printf(" &i   =%p\n", &i);
//	printf("*&i   =%d\n", *&i);
//	puts("");
//	printf("  ptr =%p\n", ptr);
//	printf(" *ptr =%d\n", *ptr);
//	printf("&*ptr =%p\n", &*ptr);
//
//	return 0;
//}


// 예제 7-4
//int main(void) {
//    char   ch;
//    int    i;
//    float  f;
//    double d;
//
//    char* pch = &ch;
//    int* pi = &i;
//    float* pf = &f;
//    double* pd = &d;
//
//    printf("sizeof(pch) =%d\n", sizeof(pch));
//    printf("sizeof(pi)  =%d\n", sizeof(pi));
//    printf("sizeof(pf)  =%d\n", sizeof(pf));
//    printf("sizeof(pd)  =%d\n", sizeof(pd));
//    puts("");
//    printf("sizeof(*pch)=%d\n", sizeof(*pch));
//    printf("sizeof(*pi) =%d\n", sizeof(*pi));
//    printf("sizeof(*pf) =%d\n", sizeof(*pf));
//    printf("sizeof(*pd) =%d\n", sizeof(*pd));
//
//    return 0;
//}


// 예제 7-5
//int main(void) {
//    int    i = 0x1B2B3B4B;
//    int* pi = &i;
//    char* pc = (char*)pi;    
//    short* ps = (short*)pi;
//
//    printf("&i=%p\n", &i);
//    printf("pi=%p\n", pi);
//    printf("pc=%p\n", pc);
//    printf("ps=%p\n", ps);
//
//    printf("*pi=%X\n", *pi);     
//    printf("*pc=%X\n", *pc);
//    printf("*ps=%X\n", *ps);
//    printf("*(int*)pc=%X\n", *(int*)pc);
//    return 0;
//}


// 예제 7-6
//int main(void) {
//    float f = 12.625f;
//    float* pf = &f;
//    unsigned* pu = (unsigned*)pf;
//
//    printf("f=%f\n", f);
//    printf("pf=%p\n", pf);
//    printf("pu=%p\n", pu);
//    printf("*pf=%f\n", *pf);
//    printf("*pu=%X\n", *pu);
//
//    return 0;
//}


// 예제 7-7
//int main(void) {
//	int   i = 0x1B2B3B4B;
//	int* pi = &i;
//	unsigned addr = (unsigned)pi;
//
//	printf("i        =%X\n", i);
//
//	printf("&i       =%p\n", &i);
//	printf("pi       =%p\n", pi);
//	printf("*pi      =%X\n", *pi);
//
//	printf("addr  =%08X, *(char*)addr    =%X\n", addr, *(char*)addr);
//	printf("addr+1=%08X, *(char*)(addr+1)=%X\n", addr + 1, *(char*)(addr + 1));
//	printf("addr+2=%08X, *(char*)(addr+2)=%X\n", addr + 2, *(char*)(addr + 2));
//	printf("addr+3=%08X, *(char*)(addr+3)=%X\n", addr + 3, *(char*)(addr + 3));
//
//	return 0;
//}