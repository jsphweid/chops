#include "util/encode_url.h"

#include <string.h>

#include "util/test_utils.h"

static void TestEncodeUrlWorks() {
    char* url = "thing.test.com";
    int len = strlen(url);
    char* result = encodeUrl(url, len);
    CHECK(result[0] == 5);
    CHECK(result[1] == 't');
    CHECK(result[2] == 'h');
    CHECK(result[3] == 'i');
    CHECK(result[4] == 'n');
    CHECK(result[5] == 'g');
    CHECK(result[6] == 4);
    CHECK(result[7] == 't');
    CHECK(result[8] == 'e');
    CHECK(result[9] == 's');
    CHECK(result[10] == 't');
    CHECK(result[11] == 3);
    CHECK(result[12] == 'c');
    CHECK(result[13] == 'o');
    CHECK(result[14] == 'm');
}

int main() {
    TestEncodeUrlWorks();

    puts("PASS");
    return EXIT_SUCCESS;
}
