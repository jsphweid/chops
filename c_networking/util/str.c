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