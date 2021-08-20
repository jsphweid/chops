#include "util/ip_string.h"

#include <string.h>

#include "util/test_utils.h"

static void TestByteArrayToIPStrWorksSimple() {
    unsigned char myArr[] = {0xff, 0xff, 0xff, 0xff};
    char* result = byteArrayToIPStr(myArr);
    char* expected = "255.255.255.255";
    int len = strlen(expected);
    int i = 0;
    for (i = 0; i < len; i++) {
        CHECK(expected[i] == result[i])
    }
    CHECK(result[len] == '\0');
}

static void TestByteArrayToIPStrWorksWithAnother() {
    unsigned char myArr[] = {0x01, 0x18, 0xc8, 0x4e};
    char* result = byteArrayToIPStr(myArr);
    char* expected = "1.24.200.78";
    int len = strlen(expected);
    int i = 0;
    for (i = 0; i < len; i++) {
        CHECK(expected[i] == result[i])
    }
    CHECK(result[len] == '\0');
}

int main(int argc, char** argv) {
    TestByteArrayToIPStrWorksSimple();
    TestByteArrayToIPStrWorksWithAnother();

    puts("PASS");
    return EXIT_SUCCESS;
}