/* ************************************************************************
 * Filename		: ex08_malloc.c
 * Description  : 동적 할당과 일반 배열 비교
 *                10명으로부터 메일 주소 입력 받아서 저장
 * Author		: SHK
 * History		: 2026-01-08
 * ************************************************************************/
 // ------------------------------------------------------------------------
 // Library
 // ------------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>

#define N_USERS 10
#define MAX_EMAIL 100


// ------------------------------------------------------------------------
// User Define Function 
// ------------------------------------------------------------------------
// -> 문자열 길이 계산
static int my_strlen(const char* s)
{
    int n = 0;
    while (s[n] != '\0') n++;
    return n;
}

// -> 문자열 복사
static void my_strcpy(char* dst, const char* src)
{
    while (*src)
        *dst++ = *src++;
    *dst = '\0';
}



// ------------------------------------------------------------------------
// Entry Point Function 
// ------------------------------------------------------------------------
int main(void)
{
    printf("EXAM 01: 배열 기반 10명에게 메일주소 입력 받고 저장\n");
    {
        // 메일주소 저장 배열 선언 및 초기화
        char emails[N_USERS][MAX_EMAIL + 1] = { 0 };

        // 메일 주소 입력 받기 
        for (int i = 0; i < N_USERS; i++)
        {
            printf("[%d/%d] 이메일 입력: ", i + 1, N_USERS);

            // 공백 없는 문자열 입력 (최대 100글자)
            if (scanf("%100s", emails[i]) != 1)
            {
                printf("입력 오류\n");
                return 1;
            }
        }

        printf("\n=== 저장된 이메일 목록 ===\n");
        for (int i = 0; i < N_USERS; i++)
        {
            printf("%2d: %s\n", i + 1, emails[i]);
        }
        printf("사용메모리 용량  ===>sizeof(emails) : %zubytes\n\n", sizeof(emails));
    }

    printf("EXAM02 : 동적할당 기반 10명에게 메일주소 입력 받고 저장\n");
    {
        char* emails[N_USERS] = { 0 };
        char buf[MAX_EMAIL + 1] = { 0 };

        for (int i = 0; i < N_USERS; i++)
        {
            printf("[%d/%d] 이메일 입력: ", i + 1, N_USERS);

            if (scanf("%100s", buf) != 1)
            {
                printf("입력 오류\n");
                // 이미 할당된 것들 정리
                for (int k = 0; k < i; k++) free(emails[k]);
                return 1;
            }

            int len = my_strlen(buf);
            emails[i] = (char*)malloc((size_t)len + 1);
            if (!emails[i])
            {
                printf("메모리 할당 실패\n");
                for (int k = 0; k < i; k++) free(emails[k]);
                return 1;
            }

            my_strcpy(emails[i], buf);
        }

        printf("\n=== 저장된 이메일 목록 ===\n");
        for (int i = 0; i < N_USERS; i++)
        {
            printf("%2d: %s\n", i + 1, emails[i]);
        }

        printf("사용메모리 용량  ===> sizeof(emails) : %zubytes\n\n", sizeof(emails));

        // 동적 메모리 해제
        for (int i = 0; i < N_USERS; i++)
            free(emails[i]);
    }
    return 0;
}