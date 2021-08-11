#include <sys/time.h>

unsigned short getRandomTwoByteId() {
    // really really bad random fn

    // gets the last two bytes of clock in nanoseconds for pseduo-random numbers
    // TODO: if I call this in quick succession, it seems to print out the
    // same result for multiple times... how is that?

    // There are a billion nanoseconds in a second
    // That means if it only took 1 instruction to call the fn, a 1 Ghz processor
    // would get a different result every time in theory. It very likely
    // takes more than 1 instruction for each call for nanoseconds and the
    // processor is even more than 1Ghz

    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    return (unsigned short)ts.tv_nsec;
}
