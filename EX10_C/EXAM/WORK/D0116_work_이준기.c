/* *************************************************************
* Filename     : D0116_work_이준기.c
* Description  : 링크드 리스트
*				 더블 링크드 리스트
*				 환형 링크드 리스트
* Author       : LJG
* History	   : 2026-01-18
* ***************************************************************/

// --------------------------------------------------------------
// Library			
// --------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>

// --------------------------------------------------------------
// 실습
// --------------------------------------------------------------
// 예제 9-6 (648page)
//struct person {
//	char phoneNo[14];
//	char name[10];
//	struct person* next;
//};
//
//int main(void)
//{
//	struct person p1 = { "010-1111-2222","이몽룡" };
//	struct person p2 = { "010-2222-3434","성춘향" };
//	struct person p3 = { "010-3333-1212","홍길동" };
//
//	p1.next = &p2;
//	p2.next = &p3;
//
//	printf("name=%s(%s)\n", p1.name, p1.phoneNo);
//	printf("next person's name=%s(%s)\n", p1.next->name, p1.next->phoneNo);
//	printf("second next person's name=%s(%s)\n", p1.next->next->name, p1.next->next->phoneNo);
//
//	return 0;
//}


// 단일 링크드 리스트 -> 회원관리 프로그램 구현해보기
//struct member {
//	char name[10];
//	char phoneNo[15];
//	char gender;
//	struct member* next;
//};
//
//int main(void)
//{
//	struct member* m1 = NULL;
//	struct member* m2 = NULL;
//
//	m1 = (struct member*)malloc(sizeof(struct member));
//	strcpy(m1->name, "이몽룡");
//	strcpy(m1->phoneNo, "010-1111-2222");
//	m1->gender = 'M';
//	m1->next = NULL;
//
//	m2 = (struct member*)malloc(sizeof(struct member));
//	strcpy(m2->name, "성춘향");
//	strcpy(m2->phoneNo, "010-3333-4444");
//	m2->gender = 'F';
//	m2->next = NULL;
//	m1->next = m2;
//
//	m2->next = (struct member*)malloc(sizeof(struct member));
//	m2 = m2->next;
//	strcpy(m2->name, "홍길동");
//	strcpy(m2->phoneNo, "010-5555-6666");
//	m2->gender = 'M';
//	m2->next = NULL;
//
//	m2 = m1;
//	while (m2 != NULL) {
//		printf("%s (%s)(%c)\n", m2->name, m2->phoneNo, m2->gender);
//		m2 = m2->next;
//	}
//
//	return 0;
//}


// 더블 링크드 리스트
//struct member {
//	char name[10];
//	char phoneNo[15];
//	char gender;
//	struct member* prev;	// 이전 노드의 주소를 저장하는 포인터 생성
//	struct member* next;
//};
//
//int main(void)
//{
//	struct member* m1 = NULL;
//	struct member* m2 = NULL;
//	struct member* m3 = NULL;
//
//	m1 = (struct member*)malloc(sizeof(struct member));
//	strcpy(m1->name, "이몽룡");
//	strcpy(m1->phoneNo, "010-1111-2222");
//	m1->gender = 'M';
//	m1->prev = NULL;
//	m1->next = NULL;
//
//	m2 = (struct member*)malloc(sizeof(struct member));
//	strcpy(m2->name, "성춘향");
//	strcpy(m2->phoneNo, "010-3333-4444");
//	m2->gender = 'F';
//	m2->next = NULL;
//	m2->prev = m1;
//	m1->next = m2;
//
//	m3 = (struct member*)malloc(sizeof(struct member));
//	strcpy(m3->name, "홍길동");
//	strcpy(m3->phoneNo, "010-5555-6666");
//	m3->gender = 'M';
//	m3->next = NULL;
//	m3->prev = m2;
//	m2->next = m3;
//
//
//	printf("1. 정방향 출력\n");
//	struct member* cur = m1;
//	while (cur != NULL) {
//		printf("%s (%s)(%c)\n", cur->name, cur->phoneNo, cur->gender);
//		cur = cur->next;
//	}
//
//	printf("\n2. 역방향 출력\n");
//	cur = m3;
//	while (cur != NULL) {
//		printf("%s (%s)(%c)\n", cur->name, cur->phoneNo, cur->gender);
//		cur = cur->prev;
//	}
//
//	return 0;
//}


// 환형 링크드 리스트
//struct member {
//	char name[10];
//	char phoneNo[15];
//	char gender;
//	struct member* prev;	// 이전 노드의 주소를 저장하는 포인터 생성
//	struct member* next;
//};
//
//int main(void)
//{
//	struct member* m1 = NULL;
//	struct member* m2 = NULL;
//	struct member* m3 = NULL;
//
//	m1 = (struct member*)malloc(sizeof(struct member));
//	strcpy(m1->name, "이몽룡");
//	strcpy(m1->phoneNo, "010-1111-2222");
//	m1->gender = 'M';
//	m1->prev = NULL;
//	m1->next = NULL;
//
//	m2 = (struct member*)malloc(sizeof(struct member));
//	strcpy(m2->name, "성춘향");
//	strcpy(m2->phoneNo, "010-3333-4444");
//	m2->gender = 'F';
//	m2->next = NULL;
//	m2->prev = m1;
//	m1->next = m2;
//
//	m3 = (struct member*)malloc(sizeof(struct member));
//	strcpy(m3->name, "홍길동");
//	strcpy(m3->phoneNo, "010-5555-6666");
//	m3->gender = 'M';
//	m3->next = m1;	// 이 부분을 통해서 환형 링크드 리스트 완성
//	m3->prev = m2;
//	m2->next = m3;
//
//
//	printf("환형 링크드 리스트 출력\n");
//	struct member* cur = m1;
//	int count = 0;			// count를 통해서 출력하고 싶은 데이터 개수 조절
//	
//	while (count <= 6) {
//		printf("%s (%s)(%c)\n", cur->name, cur->phoneNo, cur->gender);
//		cur = cur->next;
//		count++;
//	} 
//
//	return 0;
//}