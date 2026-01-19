#pragma once
#include <stdio.h>

#define MIN_COFFEE 20
#define MIN_MILK 20
#define MIN_TEABAG_HEB 20
#define MIN_TEABAG_EAR 20
#define MIN_TEABAG_HIB 20
#define MIN_APPLE 20
#define MIN_BANANA 20
#define MIN_SHINE 20



typedef struct drink { char* name; int price; }Drink;

//enum 
typedef enum { DRINK_HOT = 0, DRINK_ICE }DrinkTemp;

typedef enum { SIZE_REGULAR = 0, SIZE_MEDIUM, SIZE_LARGE }DrinkSize;

typedef struct mem {
	char* ID[20];
	char* PW[20];
}memeber;

//함수 이름 적기
void MenuBoard(void);
int ChoiceMenu(Drink* arr);
int selectMenu(Drink* arr, int Target);
int selectDetail(Drink* selected, int category);
void checkIngre(void);
void orderIngre(int* p, int* pn);
void printTotalFee(void);
int ChoiceMenuManager(Drink* items);
int choiceCate(Drink* arr, int tot, int tag, int sub, int num);

void saveToFile(int category, int price);