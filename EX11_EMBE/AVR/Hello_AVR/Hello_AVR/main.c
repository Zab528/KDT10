/*
 * Hello_AVR.cpp
 *
 * Created: 2026-01-16 오전 10:04:14
 * Author : KDT
 */ 
#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	
	// PB5 출력 설정
	DDRB |= (1 << DDB5);

	// LED 5번 깜빡이기
	for (int i = 0; i < 5; i++)
	{
		PORTB |= (1 << PORTB5);   // LED ON
		_delay_ms(500);

		PORTB &= ~(1 << PORTB5);  // LED OFF
		_delay_ms(500);
	}

	// 이후 LED 계속 ON
	PORTB |= (1 << PORTB5);

	// 무한 루프 (상태 유지)
	while (1)
	{
		// 아무 것도 안 함
	}
}

