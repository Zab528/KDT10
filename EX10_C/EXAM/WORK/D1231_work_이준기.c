/* *************************************************************
* Filename     : D1231_work_이준기
* Description  : p188 ~ p232
* Author       : LJG
* History	   : 2026.01.02
* ***************************************************************/
// --------------------------------------------------------------
// 라이브러리 로딩
// --------------------------------------------------------------
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

// --------------------------------------------------------------
// 엔트피포인트 함수
// --------------------------------------------------------------
int main(void)
{
	
	// 예제 4-3
	/*int x = 0;

	printf("x=%d 일때, 참인 것은\n", x);

	if (x == 0) printf("x==0\n");
	if (x != 0) printf("x!=0\n");
	if (x)		printf("x\n");
	if (!x)	    printf("!x\n");

	x = 1;
	printf("\nx=%d 일때, 참인 것은\n", x);

	if (x == 0) printf("x==0\n");
	if (x != 0) printf("x!=0\n");
	if (x)		printf("x\n");
	if (!x)	    printf("!x\n");*/


	// Quiz 4-1
	/*int num = 0;
	printf("숫자를 입력하세요 : ");
	scanf("%d", &num);

	if (num % 2 == 0) printf("%d은(는) 짝수입니다.", num);
	else printf("%d은(는) 홀수입니다.", num);*/


	// 예제 4-4
	/*int  score;
	char grade = ' ';

	printf("점수를 입력하세요.>");
	scanf("%d", &score);

	if (score >= 90) {
		grade = 'A';
	}
	else if (score >= 80) {
		grade = 'B';
	}
	else if (score >= 70) {
		grade = 'C';
	}
	else {
		grade = 'D';
	}

	printf("당신의 학점은 %c입니다.\n", grade);*/


	// Quiz 4-2
	/*char word = 0;

	printf("하나의 문자를 입력하세요. >");
	scanf("%c", &word);

	if (word >= 'A' && word <= 'Z')
	{
		printf("대문자입니다.");
	}
	else if (word >= 'a' && word <= 'z')
	{
		printf("소문자입니다.");
	}
	else if (word >= '1' && word <= '9')
	{
		printf("숫자입니다.");
	}
	else
	{
		printf("숫자나 영문자가 아닙니다.");
	}*/


	// 예제 4-5
	/*int score;
	char grade;
	char opt = '0';

	printf("점수를 입력해주세요.>");
	scanf("%d", &score);
	printf("당신의 점수는 %d입니다.\n", score);

	if (score >= 90) {
		grade = 'A';
		if (score >= 98) {
			opt = '+';
		}
		else if (score < 94) {
			opt = '-';
		}
	}
	else if (score >= 80) {
		grade = 'B';
		if (score >= 88) {
			opt = '+';
		}
		else if (score < 84) {
			opt = '-';
		}
	}
	else {
		grade = 'C';
	}

	printf("당신의 학점은 %c%c입니다\n", grade, opt);*/

	
	// Quiz 4-3
	/*int score;
	char grade = 'C';
	char opt = '0';

	printf("점수를 입력해주세요.>");
	scanf("%d", &score);
	printf("당신의 점수는 %d입니다.\n", score);

	if (score >= 90) {
		grade = 'A';
		if (score >= 98) {
			opt = '+';
		}
		else if (score < 94) {
			opt = '-';
		}
	}
	else if (score >= 80) {
		grade = 'B';
		if (score >= 88) {
			opt = '+';
		}
		else if (score < 84) {
			opt = '-';
		}
	}

	printf("당신의 학점은 %c%c입니다\n", grade, opt);*/
	

	// 예제 4-6
	//int month;

	//printf("현재 월을 입력하세요.>");
	//scanf("%d", &month);

	//switch (month) {
	//	case 3:
	//	case 4:
	//	case 5:
	//		printf("현재의 계절은 봄입니다.\n");
	//		break;
	//	case 6: case 7: case 8:
	//		printf("현재의 계절은 여름입니다.\n");
	//		break;
	//	case 9: case 10: case 11:
	//		printf("현재의 계절은 가을입니다.\n");
	//		break;
	//	default:
	////	case 12:	case1: case2:
	//		printf("현재의 계절은 겨울입니다.\n");
	//}

	// 예제 4-7
	/*int user, com;
	
	printf("가위(1), 바위(2), 보(3) 중 하나를 입력하세요.>");
	scanf("%d", &user);

	srand((unsigned)time(NULL));
	com = rand() % 3 + 1;

	printf("당신은 %d입니다.\n", user);
	printf("컴은   %d입니다.\n", com);

	switch (user - com) {
		case 2: case -1:
			printf("당신이 졌습니다.\n");
			break;
		case 1: case -2:
			printf("당신이 이겼습니다.\n");
			break;
		case 0:
			printf("비겼습니다.\n");
			break;
	}*/
	

	// Quiz 4-4
	/*int user, com;
	
	printf("가위(1), 바위(2), 보(3) 중 하나를 입력하세요.>");
	scanf("%d", &user);

	srand((unsigned)time(NULL));
	com = rand() % 3 + 1;

	if (user == 1) printf("당신은 가위입니다.\n");
	else if (user == 2) printf("당신은 바위입니다.\n");
	else printf("당신은 보입니다.\n");


	if (com == 1) printf("컴은   가위입니다.\n");
	else if (com == 2) printf("컴은   바위입니다.\n");
	else printf("컴은   보입니다.\n");

	switch (user - com) {
		case 2: case -1:
			printf("당신이 졌습니다.\n");
			break;
		case 1: case -2:
			printf("당신이 이겼습니다.\n");
			break;
		case 0:
			printf("비겼습니다.\n");
			break;
	}*/
	

	// 예제 4-8
	/*char gender;
	char regNo[15];

	printf("당신의 주민번호를 입력하세요. (011231-1111222)>");
	scanf("%s", regNo);

	gender = regNo[7];

	switch (gender) {
		case '1':
		case '3':
			printf("당신은 남자입니다.\n");
			break;
		case '2':
		case '4':
			printf("당신은 여자입니다.\n");
			break;
		default:
			printf("유효하지 않은 주민등록번호입니다.\n");
	}*/

	
	// Quiz 4-5
	/*char gender;
	char regNo[15];

	printf("당신의 주민번호를 입력하세요. (011231-1111222)>");
	scanf("%s", regNo);

	gender = regNo[7];

	if (gender == '1' || gender == '3')
	{
		printf("당신은 남자입니다.\n");
	}
	else if (gender == '2' || gender == '4')
	{
		printf("당신은 여자입니다.\n");
	}
	else
	{
		printf("유효하지 않은 주민등록번호입니다.\n");
	}*/

	
	// 예제 4-10
	/*int score;
	char grade = ' ';

	printf("당신의 점수를 입력하세요.(1~100)>");
	scanf("%d", &score);

	switch (score / 10) {
		case 10:
		case 9:
			grade = 'A';
			break;
		case 8:
			grade = 'B';
			break;
		case 7:
			grade = 'C';
			break;
		case 6:
			grade = 'D';
			break;
		default :
			grade = 'F';
	}

	printf("당신의 학점은 %c입니다.\n", grade);*/

	
	// Quiz 4-6
	/*int score;
	char grade = ' ';

	printf("당신의 점수를 입력하세요.(1~100)>");
	scanf("%d", &score);

	switch (score / 5) {
		case 20: case 19: case 18:
			grade = 'A';
			break;
		case 17: case 16:
			grade = 'B';
			break;
		case 15: case 14:
			grade = 'C';
			break;
		case 13: case 12:
			grade = 'D';
			break;
		default :
			grade = 'F';
	}

	printf("당신의 학점은 %c입니다.\n", grade);*/


	// 예제 4-13
	/*int i;

	for (i = 1; i <= 5; i++) {
		printf("%d\n", i);
	}

	for (i = 1; i <= 5; i++) {
		printf("%d", i);
	}
	printf("\n");*/


	// Quiz 4-7
	/*int i;
	int count = 1;

	for (i = 1; i < 10; i++) {
		if (count % 3 == 0)
		{
			printf("%d\n", i);
		}
		else
		{
			printf("%d", i);
		}
		count++;
	}*/


	// 예제 4-14
	/*int sum = 0;
	int i;

	for (i = 1; i <= 10; i++) {
		sum += i;
		printf("1부터 %2d 까지의 합: %2d\n", i, sum);
	}*/


	// Quiz 4-8
	/*int mul = 1;

	for (int i = 1; i <= 10; i++) {
		mul *= i;
		printf("1부터 %2d 까지의 곱: %d\n", i, mul);
	}*/

	
	// Quiz 4-9
	/*int i;

	for (i = 1; i <= 9; i++)
	{
		printf("%d \t %d\n", ((i - 1) % 3) + 1, ((i - 1) / 3) + 1);
	}*/


	// 예제 4-18
	/*int num;
	int i, j;

	printf("*을 출력할 라인의 수를 입력하세요.>");
	scanf("%d", &num);

	for (i = 0; i < num; i++) {
		for (j = 0; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}*/


	// Quiz 4-10
	// (1)
	/*int i, j;
	
	for (i = 1; i <= 5; i++)
	{
		for (j = 0; j < i; j++)
		{
			printf("%d", i);
		}
		printf("\n");
	}*/


	// (2)
	/*int i, j;
	
	for (i = 1; i <= 5; i++)
	{
		for (j = 1; j <= i; j++)
		{
			printf("%d", j);
		}
		printf("\n");
	}*/
	

	// 예제 4-19
	/*int i, j;

	for (i = 2; i <= 9; i++) {
		for (j = 1; j <= 9; j++) {
			printf("%d x %d = %d\n", i, j, i * j);
		}
	}*/


	// Quiz 4-11
	/*int i, j;
	
	for (i = 1; i <= 9; i++)
	{
		for (j = 2; j <= 5; j++)
		{
			printf("%d x %d = %2d\t", j, i, j * i);
		}
		printf("\n");
	}*/


	// 예제 4-22
	/*int i, j;

	for (i = 1; i <= 5; i++) {
		for (j = 1; j <= 5; j++) {
			if (i == j)
				printf("[%d, %d]", i, j);
			else
				printf("%5c", ' ');
		}
		printf("\n");
	}*/


	// Quiz 4-12
	// (b)
	/*int i, j;

	for (i = 1; i <= 5; i++)
	{
		for (j = 1; j <= 5; j++)
		{
			if (j <= i)
				printf("[%d, %d] ", i, j);
		}
		printf("\n");
	}*/


	// (a)
	/*int i, j;

	for (i = 1; i <= 5; i++)
	{
		for (j = 1; j <= 5; j++)
		{
			if (i + j == 6) printf("[%d, %d] ", i, j);
			else printf("%6c", ' ');
		}
		printf("\n");
	}*/

	return 0;
}