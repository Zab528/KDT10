/* *************************************************************
* Filename     : subJun.c
* Description  : 함수 구현
* Author       : LJG
* History	   : 2026-01-13
* ***************************************************************/

// --------------------------------------------------------------
// Library			
// --------------------------------------------------------------
#include <stdio.h>
#include "headerCafe.h"
extern totalFee;

extern int COFFEEBEANS_COUNT;
extern int MILK_COUNT;
extern int HERB_COUNT;
extern int EARL_COUNT;
extern int HIBI_COUNT;
extern int APPLE_COUNT;
extern int BANANA_COUNT;
extern int SHINE_COUNT;

int lastCategory = 0;
// --------------------------------------------------------------
// User Define Type
// --------------------------------------------------------------
void decreaseIngre(int category)
{
	switch (category)
	{
	case 1: // 커피
		COFFEEBEANS_COUNT--;
		MILK_COUNT--;
		break;

	case 2: // 차
		HERB_COUNT--;
		break;

	case 3: // 주스
		APPLE_COUNT--;
		break;
	}
}


void MenuBoard(void) {
	printf(" ---------------------------------------------------------------------------\n");
	printf("|                      SL 사내 카페에 오신 것을 환영합니다                  |\n");
	printf("|                       원하는 항목을 숫자로 입력해주세요!                  |\n");
	printf(" ---------------------------------------------------------------------------\n");
	printf(" ---------------------------------------------------------------------------\n");
	printf("| 1. 커피                                                                   |\n");
	printf("| 2. 차                                                                     |\n");
	printf("| 3. 주스                                                                   |\n");
	printf("| 4. 초기화                                                                 |\n");
	printf("| 5. 결제                                                                   |\n");
	printf("| 6. 종료                                                                   |\n");
	printf(" ---------------------------------------------------------------------------\n");
}

// 카테고리 선택 함수
int choiceCate(Drink* arr, int tot,int tag, int sub, int num) {
	for (int i = tag; i < tag+3; i++)
	{
		printf("%-10s  %5d원\n", arr[i].name, arr[i].price);

	}
	tot = selectMenu(arr, tag);
	sub = selectDetail(arr, num);
	printf("결제 가격은 %d원 입니다.\n", tot + sub);
	return totalFee += tot + sub;
}


// 메뉴 선택 함수
int ChoiceMenu(Drink* arr) {
	MenuBoard();
	int num, total=0, sub= 0;
	// Tag 설정으로 케이스별 메뉴선택을 통해 구조체 배열의 인덱스를 설정하기 위한 변수
	int Tag;
	printf("입력 : ");
	scanf("%d", &num);
	printf("\n");

	switch (num)
	{
	case 1:
		Tag = 0;
		lastCategory = 1;
		choiceCate(arr, total, Tag, sub, num);

		break;
	case 2:
		Tag = 3;
		lastCategory = 2;
		choiceCate(arr, total, Tag, sub, num);
		break;
	case 3:

		Tag = 6;
		lastCategory = 3;
		choiceCate(arr, total, Tag, sub, num);
		break;
	case 4:
		totalFee = 0;
		printf("초기 화면으로 돌아갑니다.\n\n");
		//구현해야함
		return 1;
		//break;
		
	case 5:
		printf("총 결제 가격은 %d입니다.\n", totalFee);

		saveToFile(lastCategory, totalFee);

		// 재고 감소
		decreaseIngre(lastCategory);

		totalFee = 0;
		printf("결제가 완료되었습니다.\n\n");
		return 1;
	case 6:
		printf("프로그램을 종료합니다.\n");
		return 0;
	default:
		printf("다시 입력하세요!\n");
	}

}


void saveToFile(int category, int price)
{
	FILE* fp = fopen("sales.txt", "a");   // a = append (이어쓰기)

	if (fp == NULL) {
		printf("파일을 열 수 없습니다.\n");
		return;
	}

	fprintf(fp, "[결제 완료]\n");

	switch (category) {
	case 1: fprintf(fp, "카테고리: 커피\n"); break;
	case 2: fprintf(fp, "카테고리: 차\n"); break;
	case 3: fprintf(fp, "카테고리: 주스\n"); break;
	}

	fprintf(fp, "결제 금액: %d원\n", price);
	fprintf(fp, "누적 매출: %d원\n", totalFee);
	fprintf(fp, "-------------------------\n");

	fclose(fp);
}

