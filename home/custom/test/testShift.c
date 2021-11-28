/*
 * sr.c:
 *      Shift register test program
 *
 * Copyright (c) 2012-2013 Gordon Henderson. <projects@drogon.net>
 ***********************************************************************
 */

#include <stdio.h>
#include <wiringPi.h>
#include <sr595.h>

int main (void)
{
  int i, bit ;

  wiringPiSetup () ;

// Pin base 100 for 10 pins.
//    Use wiringPi pins 12, 14 & 10 for data, clock and latch
  sr595Setup (100, 32,12,14,10) ;

  printf ("Raspberry Pi - Shift Register Test\n") ;

  for (;;)
  {
    for (i = 0 ; i < 1024 ; ++i)
    {
      for (bit = 0 ; bit < 10 ; ++bit)
        digitalWrite (100 + bit, i & (1 << bit)) ;
      delay (5) ;
    }
  }
  return 0 ;
}
