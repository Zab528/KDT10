#include <stdio.h>
#include <string.h>
#include "headerCafe.h"


//extern int lastOrderedIndex;

int selectMenu(Drink* arr, int Target) {
	int num = 0;

	while (1) {
		printf("\n메뉴를 선택하세요!\n");
		printf("1:%s  2:%s  3:%s : ",
			arr[Target].name,
			arr[Target + 1].name,
			arr[Target + 2].name);

		if (scanf("%d", &num) != 1 || num < 1 || num > 3) {
			printf("잘못 입력하셨습니다. 1, 2, 3 중 다시 입력해주세요.\n");
			while (getchar() != '\n');
			continue;
		}
		break;
	}

	printf("선택하신 메뉴는 : %s", arr[Target + (num - 1)].name);
	return arr[Target + (num - 1)].price;
}

// 음료 내부 옵션 설정 함수
// selectMenu에서 선택한 category를 같이 주는거
int selectDetail(Drink* selected, int category) {
	int choice;
	int total = 0;

	// 1. 온도 선택
	if (category != 3) {
		printf("\n[온도 선택] 1.HOT  2.ICE(+300)원: ");
		scanf("%d", &choice);
		if (choice == 2) {
			total += 300;	// 원본 가격에 300원 추가
		}
	}
	else {
		printf("\n 주스는 ICE 전용 메뉴입니다.");
	}
	// 2. 사이즈 선택
	printf("\n[사이즈 선택] 1.Regular  2.Medium(+500원)  3.Large(+1000원) : ");
	scanf("%d", &choice);
	if (choice == 2) {
		total += 500;	// 원본 가격에 500원 추가
	}
	else if (choice == 3) {
		total += 1000;
	}
	return total;
};

int isManager(void)
{
	char id[20];
	char pw[20];

	printf("ID : ");
	scanf("%19s", id);

	printf("PW : ");
	scanf("%19s", pw);

	if (strcmp(id, "admin") == 0 && strcmp(pw, "1234") == 0) {
		printf("관리자 로그인 성공\n");
		return 1;   // 관리자
	}

	if (strcmp(id, "customer") == 0 && strcmp(pw, "123") == 0) {
		printf("사용자 로그인 성공\n");
		return 2;   // 사용자
	}

	printf("로그인 실패: ID 또는 PW가 올바르지 않습니다.\n");
	return 0;
}


