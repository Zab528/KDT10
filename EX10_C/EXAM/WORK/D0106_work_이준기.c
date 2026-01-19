/* *************************************************************
* Filename     : D0106_work_이준기
* Description  : 6장 함수
*				 p348 ~ p424
* Author       : LJG
* History	   : 2026.01.06
* ***************************************************************/
// --------------------------------------------------------------
// 라이브러리 로딩
// --------------------------------------------------------------
#include <stdio.h>


// --------------------------------------------------------------
// [실습]
// --------------------------------------------------------------
// 예제 6-1
//int multiply(int x, int y) {
//	int result = x * y;
//
//	return result;
//}
//
//int getUserInput(void) {
//	int num;
//
//	printf("input a number(2~9) :");
//	scanf("%d", &num);
//
//	return num;
//}
//
//void printGugudan(int dan) {
//	int i;
//	for (i = 1; i <= 9; i++) {
//		int result = multiply(dan, i);
//		printf("%d*%d=%2d\n", dan, i, result);
//	}
//}
//
//void printGugudanAll(void) {
//	int i, j;
//	for (i = 1; i <= 9; i++) {
//		for (j = 2; j <= 9; j++)
//			printf("%d*%d=%2d ", j, i, multiply(j, i));
//		printf("\n");
//	}
//}
//
//int main(void) {
//	int dan = getUserInput();
//
//	if (2 <= dan && dan <= 9)
//		printGugudan(dan);
//	else
//		printGugudanAll();
//
//	return 0;
//}


// 예제 6-2
//int add(int x, int y) {
//	int result = x + y;
//	printf("add(%d, %d)이 호출되었습니다.\n", x, y);
//	return result;
//}
//int mul(int x, int y) {
//	int result = x * y;
//	printf("mul(%d, %d)이 호출되었습니다.\n", x, y);
//	return result;
//}
//
//int main(void) {
//	printf("main() - add(3,5)=%d, mul(3,5)=%d\n", add(3, 5), mul(3, 5));
//
//	return 0;
//}


// Quiz 6-1
// -> add(2,3)이 실행되어 5가 return되고, add(1,5)가 실행되어 6이 return되어 6이 출력으로 나온다.


// 예제 6-4
/*int multiply(int x, int y)  { return x * y;          }             
int abs(int x)             	{ return x > 0 ? x : -x; }             
int diff(int x, int y)     	{ return abs(x - y);     }             
int max(int x, int y)       { return x > y ? x : y;  }             
int min(int x, int y)      	{ return x < y ? x : y;  }             
                                                                       
int main(void) {                                                       
	int x = 3;                                                     
	int y = 5;                                                     
                                                                       
	printf("multiply(%d, %d)=%d\n", x, y, multiply(x, y));         
	printf("abs(%d)=%d\n", -y, abs(-y));                           
	printf("diff(%d, %d)=%d\n", x, y, diff(x, y));                 
	printf("max(%d, %d)=%d\n", x, y, max(x, y));                   
	printf("min(%d, %d)=%d\n", x, y, min(x, y));                   
                                                                       
	return 0;                                                      
}   */     


//Quiz 6-2
//int max3(int x, int y, int z) {
//	return max(x, (max(y, z)));
//}


// Quiz 6-3
//int multiply(int x, int y) {
//	int result = x * y;
//	return result;
//}
//-> 두 매개변수의 타입이 int라서 범위를 벗어날 수 있다.


// 예제 6-5
//int divide(int x, int y) {                                            
//	if (y == 0) return 0;         
//                                                                      
//	return x / y;                                                 
//}                                                                     
//                                                                      
//int main(void) {                                                      
//	int x = 4, y = 2;                                             
//                                                                      
//	printf("%d/%d=%d\n", x, y, divide(x, y));                     
//                                                                      
//	y = 0;                                                        
//	printf("%d/%d=%d\n", x, y, divide(x, y));                     
//	return 0;                                                     
//}


// Quiz 6-4
//void printGugudan(int dan) {
//	int i;
//	if (dan >= 2 && dan <= 9) return 0;
//
//	for (i = 1; i <= 9; i++)
//		printf("%d*%d=%2d\n", dan, i, dan * i);
//}


// 예제 6-6
//int  multiply(int x, int y);                         
//int  getUserInput(void);                         
//void printGugudan(int dan);                           
//void printGugudanAll(void);                                 
//
//int main(void) {
//	int dan = getUserInput();           
//
//	if (2 <= dan && dan <= 9)
//		printGugudan(dan);    
//	else
//		printGugudanAll();        
//
//	return 0;
//}
//
//int multiply(int x, int y) { return x * y; }
//int getUserInput(void) {
//	int num;
//	printf("input a number(2~9) :");
//	scanf("%d", &num);
//	return num;
//}
//
//void printGugudan(int dan) {
//	int i;
//	for (i = 1; i <= 9; i++)
//		printf("%d*%d=%2d\n", dan, i, multiply(dan, i));
//}
//
//void printGugudanAll(void) {
//	int i, j;
//	for (i = 1; i <= 9; i++) {
//		for (j = 2; j <= 9; j++)
//			printf("%d*%d=%2d ", j, i, multiply(j, i));
//		printf("\n");
//	}
//}


// 예제 6-7
//// main.c 부분
//int  multiply(int x, int y);
//int  getUserInput(void);
//void printGugudan(int dan);
//void printGugudanAll(void);
//
//int main(void) {
//	int dan = getUserInput();               
//
//	if (2 <= dan && dan <= 9) {
//		printGugudan(dan);        
//	}
//	else {
//		printGugudanAll();         
//	}
//
//	return 0;
//}
//
//// 여기서부터 원래 따로 선언이지만 과제 제출을 위해 같이 만듦. sub.c
//int multiply(int x, int y) {
//	int result = x * y;
//
//	return result;
//}
//
//int getUserInput(void) {
//	int num;
//
//	printf("input a number(2~9) :");
//	scanf("%d", &num);
//
//	return num;
//}
//
//void printGugudan(int dan) {
//	int i;
//
//	for (i = 1; i <= 9; i++) {
//		int result = multiply(dan, i);       
//		printf("%d*%d=%2d\n", dan, i, result);
//	}
//}
//
//void printGugudanAll(void) {
//	int i, j;
//
//	for (i = 1; i <= 9; i++) {
//		for (j = 2; j <= 9; j++) {
//			printf("%d*%d=%2d ", j, i, multiply(j, i));
//		}
//		printf("\n");
//	}
//}


// 예제 6-8 (header.h 따로 선언)
//// main2.c
//#include "header.h"                                                                                
//
//int main(void) {
//	int dan = getUserInput();                                
//
//	if (2 <= dan && dan <= 9) {
//		printGugudan(dan);                        
//	}
//	else {
//		printGugudanAll();  	                         
//	}
//
//	return 0;
//}
//
//// sub2.c
//#include "header.h" 
//int multiply(int x, int y) {
//	int result = x * y;
//
//	return result;
//}
//
//int getUserInput(void) {
//	int num;
//
//	printf("input a number(2~9) :");
//	scanf("%d", &num);
//
//	return num;
//}
//
//void printGugudan(int dan) {
//	int i;
//
//	for (i = 1; i <= 9; i++) {
//		int result = multiply(dan, i);        
//		printf("%d*%d=%2d\n", dan, i, result);
//	}
//}
//
//void printGugudanAll(void) {
//	int i, j;
//
//	for (i = 1; i <= 9; i++) {
//		for (j = 2; j <= 9; j++) {
//			printf("%d*%d=%2d ", j, i, multiply(j, i));
//		}
//		printf("\n");
//	}
//}


// Quiz 6-5
// -> 포함되는 소스파일은 전부 다시 컴파일하여야 한다.


// 예제 6-9
//void second(void) {
//	printf("second()\n");
//}
//
//void first(void) {
//	second();
//}
//
//int main(void) {
//	first();
//	return 0;
//}


// 예제 6-10
//void second(void) {
//	printf("\t\tsecond() - start\n");
//	printf("\t\t\tprintf(\"second()\")\n");
//	printf("\t\tsecond() - end\n");
//}
//
//void first(void) {
//	printf("\tfirst() - start\n");
//	second();
//	printf("\tfirst() - end\n");
//}
//
//int main(void) {
//	printf("main() - start\n");
//	first();
//	printf("main() - end\n");
//
//	return 0;
//}


// 예제 6-11
//int factorial(int n) {
//	if (n == 1) return 1;            
//
//	return n * factorial(n - 1);                   
//}
//
//int main(void) {
//	int result = factorial(5);
//
//	printf("%d!=%d\n", 5, result);
//
//	return 0;
//}


// 예제 6-12
//long long factorial(int n) {
//	if (n <= 0 || n > 20) return -1;                             
//	if (n <= 1)
//		return 1;
//
//	return n * factorial(n - 1);
//}
//
//int main(void) {
//	int i = 0;
//	int n = 21;
//	long long result = 0;
//
//	for (i = 1; i <= n; i++) {
//		result = factorial(i);
//
//		if (result == -1) {
//			printf("유효하지 않은 값입니다.(0<n<=20):%d\n", n);
//			break;
//		}
//		printf("%2d!=%20lld\n", i, result);
//	}
//
//	return 0;
//}


// 예제 6-13
//long long power(int x, int n) {
//	if (n == 1)
//		return x;
//	return x * power(x, n - 1);
//}
//
//int main(void) {
//
//	int i, x = 2, n = 5;
//	long long result = 0;
//
//	for (i = 1; i <= n; i++)
//		result += power(x, i);
//
//	printf("result=%d\n", result);
//	return 0;
//}


// Quiz 6-6
// 재귀 호출
//long long power(int x, int n) {
//	if (n == 1)
//		return x;
//	return x * power(x, n - 1);
//}
// 반복문
//long long power(int x, int n) {
//	int result = x;
//	for (int i = 0; i < n; i++)
//		result *= x;
//	return result;
//}


// 예제 6-14
//void func1() {
//	int tmp = 100;
//	int i;
//
//	for (i = 0; i < 1; i++) {
//		printf("[1]tmp=%d\n", tmp);    
//
//		int tmp = 200;               
//		printf("[2]tmp=%d\n", tmp); 	            
//	}
//	printf("[3]tmp=%d\n", tmp);    	                     
//}
//
//int main(void) {
//	func1();
//	return 0;
//}


// 예제 6-15
//int x;                                                       
//
//void func1(void) {
//	int y;                                                    
//	x = 1;                                                                     
//	y = 2;                                                                    
//	//z = 3;                                                                   
//	//x2 = 4;                                 
//
//	printf("func1() x=%d\n", x);
//	printf("func1() y=%d\n", y);
//	//printf("func1() z=%d\n", z);                                          
//}
//
//int x2;                                                       
//
//void func2(void) {
//	int z;                                                  
//	x = 10;                                                                 
//	//y  = 20;                                                 
//	z = 30;                                                             
//	x2 = 40;                                         
//
//	printf("func2() x=%d\n", x);
//	//printf("func2() y=%d\n", y);                           
//	printf("func2() z=%d\n", z);
//	printf("func2() x2=%d\n", x2);
//}
//
//int main(void) {
//	func1();
//	func2();
//	return 0;
//}


// 예제 6-16
//int x = 100;                     
//
//int main(void) {
//    printf("x=%d\n", x);                     
//
//    int x = 200;                  
//
//    printf("x=%d\n", x);          
//
//    return 0;
//}


// 예제 6-17
//// main3.c
//int gv = 100; 
//
//void printGv(void);
//
//int main(void) {
//	printf("main() - gv=%d\n", gv);
//	printGv();
//
//	return 0;
//}
//
//// sub3.c
//extern int gv;                        
//
//void printGv(void) {
//	printf("printGv() - gv=%d\n", gv);        
//}


// 예제 6-18
//#define STU 4                                                          
//#define SUB 3                                                           
//                                                       
//int score[STU + 1][SUB + 1] = {
//	{ 100, 100, 100 },
//	{ 25,  20,  20  },
//	{ 35,  30,  30  },
//	{ 45,  40,  40  }
//};
//
//void sumScore(void);                                           
//void printScore(void);                                         
//
//int main(void) {
//	sumScore();
//	printScore();
//	return 0;
//}
//
//void sumScore(void) {
//	int i, j;
//	for (i = 0; i < STU; i++)
//		for (j = 0; j < SUB; j++) {
//			score[i][SUB] += score[i][j];
//			score[STU][j] += score[i][j];
//		}
//}
//
//void printScore(void) {
//	int i, j;
//	printf("번호 국어 영어 수학 총점  평균\n");
//	printf("===============================\n");
//
//	for (i = 0; i < STU; i++) {
//		printf(" %d   ", i + 1);
//
//		for (j = 0; j < SUB; j++)
//			printf("%3d  ", score[i][j]);
//
//		printf(" %3d  %5.1f\n", score[i][SUB], score[i][SUB] / (float)SUB);
//	}
//	printf("===============================\n총점 ");
//
//	for (j = 0; j < SUB; j++)
//		printf("%3d  ", score[STU][j]);
//
//	puts("");
//}


// 예제 6-19
//static int sv;            
//
//void func1() {
//	static 	int sv2 = 1;                    
//	int lv = 1;	                                       
//
//	printf("func1() - sv2=%d, lv=%d\n", sv2++, lv++);
//}
//
//void func2() {
//	sv = 100;
//	printf("func2() - sv =%d\n", sv);
//	//printf("func2() - sv2=%d\n", sv2);          
//}
//
//int main(void) {
//	func1();
//	func1();
//	func1();
//	func2();
//
//	return 0;
//}


// 예제 6-20
//// main4.c
//int gv = 100;     
//
//void   gfunc(void);     
//static void sfunc(void);           
//
//extern int main(void) {
//	gfunc();                                 
//	sfunc();                               
//	return 0;
//}
//
//static void sfunc(void) {          
//	printf("sfunc() - main4.c\n");
//}
//
//// sub4.c
//extern int gv;          
//
//void   gfunc(void);      
//static void sfunc(void); 
//
//static void sfunc(void) { 
//	printf("sfunc() - sub4.c\n");
//	gv = 200;
//}
//
//void gfunc(void) {       
//	sfunc();
//	printf("gfunc(%d)\n", gv);
//}