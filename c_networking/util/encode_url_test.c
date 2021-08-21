#include "util/encode_url.h"

#include <string.h>

#include "util/test_utils.h"

static void TestEncodeUrlWorks() {
    char* url = "thing.test.com";
    int len = strlen(url);
    char* buffer = malloc(len + 1);
    encodeUrl(buffer, url, len);
    CHECK(buffer[0] == 5);
    CHECK(buffer[1] == 't');
    CHECK(buffer[2] == 'h');
    CHECK(buffer[3] == 'i');
    CHECK(buffer[4] == 'n');
    CHECK(buffer[5] == 'g');
    CHECK(buffer[6] == 4);
    CHECK(buffer[7] == 't');
    CHECK(buffer[8] == 'e');
    CHECK(buffer[9] == 's');
    CHECK(buffer[10] == 't');
    CHECK(buffer[11] == 3);
    CHECK(buffer[12] == 'c');
    CHECK(buffer[13] == 'o');
    CHECK(buffer[14] == 'm');
    free(buffer);
}

int main() {
    TestEncodeUrlWorks();

    puts("PASS");
    return EXIT_SUCCESS;
}
