#include <stdio.h>

int main(void)
{
	int i = 0;
	int j = 0;

	printf("¼ýÀÚ 2°³ ÀÔ·Â : ");
	scanf_s("%d %d", &i, &j);

	printf("µ¡¼À   : %d + %d = %d\n", i, j, i + j);
	printf("»¬¼À   : %d - %d = %d\n", i, j, i - j);
	printf("°ö¼À   : %d * %d = %d\n", i, j, i * j);
	printf("³ª´°¼À : %d / %d = %f\n", i, j, (double)i / j);

	return 0;
}