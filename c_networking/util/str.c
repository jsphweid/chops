#include <stdio.h>

int getStringLength(const char *str) {
    int i = 0;
    while (str[++i] != '\0') {
    }
    return i;
}

void printStr(char *str) {
    int i = 0;
    while (str[++i] != '\0') {
        printf("%c", str[i]);
    }
}

void printBlob(unsigned char *blob, int len) {
    int i = -1;
    printf("blob (len = %d) -> ", len);
    while (i++ < len) {
        printf("%02x ", blob[i]);
    }
    printf("\n");
}