#include <stdio.h>
#include <stdlib.h>

char *byteArrayToIPStr(unsigned char *byteArray) {
    // converts 0xFFFFFFFF -> "255.255.255.255"
    // printf("byteArrayToIPStr - %02x %02x %02x %02x\n", byteArray[0], byteArray[1], byteArray[2], byteArray[3]);
    char *str = calloc(15, sizeof(char));  // 15 is max string length
    sprintf(str, "%d.%d.%d.%d", byteArray[0], byteArray[1], byteArray[2], byteArray[3]);
    return str;
}
