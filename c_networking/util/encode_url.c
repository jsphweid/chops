#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// TODO: my issue with this function is that the caller must know
// that it needs to know the exact size of the buffer to be urlLength + 1
char *encodeUrl(char *ret, char *url, int urlLength) {
    // Example:
    // thing.test.com
    // t h i n g . t e s t . c o m   - input
    // 5 t h i n g 4 t e s t 3 c o m - ret
    // 0 1 2 3 4 5 6 7 8 9 a b c d e - hex
    uint8_t i, offset, len;

    offset = 1;
    len = 0;

    for (i = 0; i < urlLength; i++) {
        if (url[i] == '.') {
            ret[offset - 1] = len;
            memcpy(ret + offset, &url[offset - 1], len);
            offset += len + 1;  // length of word + room for the count
            len = 0;
            continue;
        }
        len++;
    }

    // for now, assume last char is not a `.`
    ret[offset - 1] = len;
    memcpy(ret + offset, &url[offset - 1], len);
    return ret;
}