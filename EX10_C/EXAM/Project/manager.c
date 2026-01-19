/*
* 재고확인 - int checkIngre()
* 발주하기 - int orderIngre() - 발주 후 수량 확인할거면 int사용
* 매출보기 - int checkTotal()
* 가격수정 - int editPrice()
*/

/*
* #define MILK_COUNT 100
#define HERB_COUNT 100
#define EARL_COUNT 100
#define HIBI_COUNT 100
#define APPLE_COUNT 100
#define BANANA_COUNT 100
#define SHINE_COUNT 100

#define MIN_COFFEE 20
#define MIN_MILK 20
#define MIN_TEABAG_HEB 20
#define MIN_TEABAG_EAR 20
#define MIN_TEABAG_HIB 20
#define MIN_APPLE 20
#define MIN_BANANA 20
#define MIN_SHINE 20
*/
#include "headerCafe.h"

extern int COFFEEBEANS_COUNT;
extern int MILK_COUNT;
extern int HERB_COUNT;
extern int EARL_COUNT;
extern int HIBI_COUNT;
extern int APPLE_COUNT;
extern int BANANA_COUNT;
extern int SHINE_COUNT;
extern int totalFee;

void checkIngre(void) {
    printf("------------------------------------------------\n");
    printf("원두           재고: %d\n", COFFEEBEANS_COUNT);
    printf("우유           재고: %d\n", MILK_COUNT);
    printf("허브차 티백     재고: %d\n", HERB_COUNT);
    printf("얼그레이 티백   재고: %d\n", EARL_COUNT);
    printf("히비스커스 티백 재고: %d\n", HIBI_COUNT);
    printf("사과           재고: %d\n", APPLE_COUNT);
    printf("바나나         재고: %d\n", BANANA_COUNT);
    printf("샤인 머스캣    재고: %d\n", SHINE_COUNT);
    printf("------------------------------------------------\n");
    printf("\n");

    if (COFFEEBEANS_COUNT < MIN_COFFEE) printf("원두 재고가 부족합니다!\n");
    if (MILK_COUNT < MIN_MILK) printf("우유 재고가 부족합니다!\n");
    if (HERB_COUNT < MIN_TEABAG_HEB) printf("허브차 티백 재고가 부족합니다!\n");
    if (EARL_COUNT < MIN_TEABAG_EAR) printf("얼그레이 티백 재고가 부족합니다!\n");
    if (HIBI_COUNT < MIN_TEABAG_HIB) printf("히비스커스 티백 재고가 부족합니다!\n");
    if (APPLE_COUNT < MIN_APPLE) printf("사과 재고가 부족합니다!\n");
    if (BANANA_COUNT < MIN_BANANA) printf("바나나 재고가 부족합니다!\n");
    if (SHINE_COUNT < MIN_SHINE) printf("샤인 머스캣 재고가 부족합니다!\n");

    printf("\n");
}

void orderIngre(int* p, int* pn) {
    switch (*p) {
    case 1:
        COFFEEBEANS_COUNT += *pn;
        printf("원두 재고가 %d개로 증가했습니다.\n", COFFEEBEANS_COUNT);
        break;
    case 2:
        MILK_COUNT += *pn;
        printf("우유 재고가 %d개로 증가했습니다.\n", MILK_COUNT);
        break;
    case 3:
        HERB_COUNT += *pn;
        printf("허브차 티백 재고가 %d개로 증가했습니다.\n", HERB_COUNT);
        break;
    case 4:
        EARL_COUNT += *pn;
        printf("얼그레이 티백 재고가 %d개로 증가했습니다.\n", EARL_COUNT);
        break;
    case 5:
        HIBI_COUNT += *pn;
        printf("히비스커스 티백 재고가 %d개로 증가했습니다.\n", HIBI_COUNT);
        break;
    case 6:
        APPLE_COUNT += *pn;
        printf("사과 재고가 %d개로 증가했습니다.\n", APPLE_COUNT);
        break;
    case 7:
        BANANA_COUNT += *pn;
        printf("바나나 재고가 %d개로 증가했습니다.\n", BANANA_COUNT);
        break;
    case 8:
        SHINE_COUNT += *pn;
        printf("샤인 머스캣 재고가 %d개로 증가했습니다.\n", SHINE_COUNT);
        break;
    default:
        printf("잘못된 품목 번호입니다.\n");
    }
}

void printTotalFee(void) {
    printf("현재까지의 매출은 %d원입니다.\n", totalFee);
}

int ChoiceMenuManager(Drink* items) {
    int menu, inven, n, beverage, won;

    printf("================================================\n");
    printf("1. 재고확인\n");
    printf("2. 발주하기\n");
    printf("3. 매출보기\n");
    printf("4. 가격 수정\n");
    printf("5. 프로그램 종료\n");
    printf("================================================\n");
    printf("\n사용하실 기능을 선택하세요> ");

    if (scanf("%d", &menu) != 1) return 0;

    switch (menu) {
    case 1:
        checkIngre();
        break;

    case 2:
        printf("발주하실 품목 번호와 수량을 선택하세요 (예 1 30):\n");
        printf("1. 원두\n2. 우유\n3. 허브차 티백\n4. 얼그레이 티백\n");
        printf("5. 히비스커스 티백\n6. 사과\n7. 바나나\n8. 샤인 머스캣\n");
        printf("선택 > ");

        if (scanf("%d %d", &inven, &n) != 2) return 1;
        orderIngre(&inven, &n);
        break;

    case 3:
        printTotalFee();
        break;

    case 4:
        printf("가격을 변경하실 품목 번호와 수정된 가격을 입력하세요 (예 1 3000):\n");
        for (int i = 0; i < 9; i++)
            printf("%d. %s / 현재 가격: %d\n", i + 1, items[i].name, items[i].price);

        printf("선택 > ");
        if (scanf("%d %d", &beverage, &won) != 2) return 1;

        items[beverage - 1].price = won;
        printf("%s의 변경된 기본 가격은 %d입니다.\n",
            items[beverage - 1].name, items[beverage - 1].price);
        break;

    case 5:
        return 0;   // 종료 신호

    default:
        printf("잘못된 메뉴입니다.\n");
    }

    return 1;   // 계속 실행
}
