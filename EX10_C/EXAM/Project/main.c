/* *************************************************************
* Filename     : main.c
* Description  : 카페 키오스트 Project
* Author       : LJG
* History	   : 2026-01-13
* ***************************************************************/

// --------------------------------------------------------------
// Library			
// --------------------------------------------------------------
#include <stdio.h>
#include "headerCafe.h"

// --------------------------------------------------------------
// User Define Type
// --------------------------------------------------------------
int COFFEEBEANS_COUNT = 19;
int MILK_COUNT = 100;
int HERB_COUNT = 100;
int EARL_COUNT = 100;
int HIBI_COUNT = 100;
int APPLE_COUNT = 100;
int BANANA_COUNT = 100;
int SHINE_COUNT = 100;
int totalFee=0;



// --------------------------------------------------------------
// Entry Point Function
// --------------------------------------------------------------
int main(void)
{
	int flag = 0;
	char c;
	Drink items[9] = {
		{"AMERICANO",2000},
		{"LATTE",2000},
		{"ESPRESSO",2000},
		{"HERB_TEA",2100},
		{"EARL_GREY",2100},
		{"HIBISCUS",2100},
		{"APPLE",2200},
		{"BANANA",2200},
		{"SHINE",2200},
	};


	while (1) {
		printf("로그인하시겠습니까? (O, X) 중 하나를 입력하세요: ");
		scanf(" %c", &c);

		if (c == 'X' || c == 'x') {
			printf("프로그램을 종료합니다.\n");
			break;
		}
		flag = isManager();
		if (flag == 2) {
			while (1)
			{
				int result = ChoiceMenu(items);

				if (result == 0)   // 종료
					break;
				// result == 1 이면 자동으로 다시 처음
			}
			continue;
		}
		else if (flag == 1){
			while (1) {
				printf("\n관리자 모드를 시작합니다.\n");
				int result = ChoiceMenuManager(items);
				if (result == 0)   // 종료
					break;
			}
			continue;
		}


	}
	

	return 0;
}