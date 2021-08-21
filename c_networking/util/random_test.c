#include "util/random.h"

#include <stdio.h>

#include "util/test_utils.h"

static void TestRandomChar() {
    // not really a test because there are no assertions but
    // is still useful if you want to test it out by running this
    // file and checking output
    printf("%x\n", getRandomTwoByteId());
}

int main() {
    TestRandomChar();

    return EXIT_SUCCESS;
}