#include "util/str.h"

#include <stdio.h>

#include "util/test_utils.h"

static void TestGetStrLength() {
    CHECK(getStringLength("a") == 1);
    CHECK(getStringLength("ab") == 2);
    CHECK(getStringLength("abc") == 3);
}

int main(int argc, char **argv) {
    TestGetStrLength();

    puts("PASS");
    return EXIT_SUCCESS;
}
