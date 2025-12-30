#include <stdio.h>

#define MIN 60
#define HOUR MIN*60

int main(void)
{
	// 예제 3-6
	/*int a = 10;
	int b = 4;

	printf("%d + %d = %d\n", a, b, a + b);
	printf("%d - %d = %d\n", a, b, a - b);
	printf("%d * %d = %d\n", a, b, a * b);
	printf("%d / %d = %d\n", a, b, a / b);

	printf("%d / %f = %f\n", a, (float)b, a / (float)b);*/


	// 예제 3-7
	/*int a = 1000000;
	int b = 2000000;

	long long c = a * b;

	printf("c=%d\n", c);*/


	// 예제 3-8
	/*long long a = 1000000 * 1000000;
	long long b = 1000000 * 1000000LL;

	printf("a=%lld\n", a);
	printf("b=%lld\n", b);*/

	
	// 예제 3-9
	/*int a = 1000000;

	int result1 = a * a / a;
	int result2 = a / a * a;

	printf("%d * %d / %d = %d\n", a, a, a, result1);
	printf("%d / %d * %d = %d\n", a, a, a, result2);*/


	// 예제 3-10
	/*char a = 'a';
	char d = 'd';

	char zero = '0';
	char two = '2';

	printf("'%c' - '%c' = %d\n", d, a, d - a);
	printf("'%c' - '%c' = %d\n", two, zero, two - zero);
	printf("'%c'=%d\n", a, a);
	printf("'%c'=%d\n", d, d);
	printf("'%c'=%d\n", zero, zero);
	printf("'%c'=%d\n", two,  two);*/


	// 예제 3-11
	/*int dayInSec = 24 * HOUR;
	int numOfDay = 10;
	int result = dayInSec * numOfDay;

	printf("%d day = %d sec\n", numOfDay, result);*/


	// 예제 3-12
	/*double pi = 3.141592;
	double shortPi = (int)(pi * 1000) / 1000.0;
	printf("%lf\n", shortPi);
	printf("%5.3lf\n", shortPi);*/


	// 예제 3-13
	/*double pi = 3.141592;
	double shortPi = (int)(pi * 1000 + 0.5) / 1000.0;

	printf("%lf\n", shortPi);*/


	// 예제 3-14
	/*double pi = 3.141592;
	double shortPi = (int)(pi * 100 + 0.9) / 100.0;

	printf("%lf\n", shortPi);*/


	// 예제 3-15
	/*int x = 10, y = 8;

	printf("%d을 %d로 나누면, \n", x, y);
	printf("몫은 %d이고, 나머지는 %d입니다.\n", x / y, x % y);*/


	// 예제 3-16
	/*int x = 10;
	int y = 8;

	printf("%3d %% %2d = %2d\n", x, y, x % y);
	printf("%3d %% %2d = %2d\n", x, -y, x % -y);
	printf("%3d %% %2d = %2d\n", -x, y, -x % y);
	printf("%3d %% %2d = %2d\n", -x, -y, -x % -y);*/

	return 0;
}