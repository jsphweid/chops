#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>

#define UDP_PORT 53
#define MAX_RESPONSE_BYTES 1024

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

char *byteArrayToIPStr(unsigned char *byteArray) {
    // converts 0xFFFFFFFF -> "255.255.255.255"
    printf("byteArrayToIPStr - %02x %02x %02x %02x\n", byteArray[0], byteArray[1], byteArray[2], byteArray[3]);
    char *str = calloc(15, sizeof(char)); // 15 is max string length
    sprintf(str, "%d.%d.%d.%d", byteArray[0], byteArray[1], byteArray[2], byteArray[3]);
    return str;
}

char *convertUrl(char *url, int urlLength) {
    // Example:
    // thing.test.com
    // t h i n g . t e s t . c o m   - input
    // 5 t h i n g 4 t e s t 3 c o m - ret
    // 0 1 2 3 4 5 6 7 8 9 a b c d e - hex
    uint8_t i, offset, len;
    char *ret;

    offset = 1;
    len = 0;

    ret = malloc(urlLength + 1);
    for (i = 0; i < urlLength; i++) {
        if (url[i] == '.') {
            ret[offset - 1] = len;
            memcpy(ret + offset, &url[offset - 1], len);
            offset += len + 1; // length of word + room for the count
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

typedef struct Answer {
    char *type;
    char *content;
} Answer;

void printBlob(unsigned char *blob, int len) {
    int i = -1;
    printf("blob (len = %d) -> ", len);
    while (i++ < len) {
        printf("%02x ", blob[i]);
    }
    printf("\n");
}

void handleAnswers(Answer *out, unsigned char *blob, int blobLen, int numAnswers) {
    int i;
    int offset = 0;
    uint8_t isARecord, isCName;

    printBlob(blob, blobLen);
    for (i = 0; i < numAnswers; i++) {
        isARecord = blob[3 + offset] == 0x01;
        isCName = blob[3 + offset] == 0x05;

        if (blob[2 + offset] != 0x00 ||
            (!isARecord && !isCName)) {
            puts("Skipping answer because it contains something other than a CNAME or IP");
            continue;
        }

        Answer *answer;
        answer = malloc(sizeof(struct Answer));

        if (isARecord) {
            answer->type = "A RECORD";
        } else {
            answer->type = "CNAME";
        }

        uint8_t contentSize;
        contentSize = (blob[10 + offset] << 8) | blob[11 + offset];
        if (isARecord) {
            char *ipStr = byteArrayToIPStr(&blob[12 + offset]);
            puts(ipStr);
            answer->content = ipStr;
        } else {
            char *ptr = malloc(contentSize + 1);
            memcpy(ptr, &blob[12 + offset], contentSize);
            answer->content = ptr;
        }
        out[i] = *answer;
        offset += 12 + contentSize;
    }
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Requires one arg, like `laughtears.com`");
        exit(1);
    }

    int sockfd;
    uint addrlen;
    char *url = argv[1];
    char *convertedUrl;
    int urlLength = getStringLength(url);
    int convertedUrlLength = urlLength + 1;
    int dataLength = 17 + convertedUrlLength;
    struct sockaddr_in addr;
    struct sockaddr *converted_addr;
    struct in_addr ap;

    unsigned char *buffer = malloc(dataLength);

    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    inet_aton("8.8.8.8", &ap);
    addr.sin_family = AF_INET;
    addr.sin_port = htons(UDP_PORT);
    addr.sin_addr = ap;

    converted_addr = (struct sockaddr *) &addr;

    addrlen = sizeof(addr);

    // 2 byte random transaction id (can just use af 70 hex) TODO: actually make random
    buffer[0] = 0xaf;
    buffer[1] = 0x70;
    // 2 byte flag, use 01 00
    buffer[2] = 0x01;
    buffer[3] = 0x00;
    // 2 byte questions, use 00 01 (1 question)
    buffer[4] = 0x00;
    buffer[5] = 0x01;
    // 2 byte answer rr, use 00 00
    buffer[6] = 0x00;
    buffer[7] = 0x00;
    // 2 byte authority rr, use 00 00
    buffer[8] = 0x00;
    buffer[9] = 0x00;
    // 2 byte additional rr, use 00 00
    buffer[10] = 0x00;
    buffer[11] = 0x00;
    // query with length, but padded 1 byte on each side (0a to start, 00 to end)
    convertedUrl = convertUrl(url, urlLength);
    memcpy(&buffer[12], convertedUrl, convertedUrlLength); // (void *dst, const void *src, size_t n)
    free(convertedUrl);
    buffer[12 + convertedUrlLength] = 0x00;
    // 2 byte type, use 00 01
    buffer[13 + convertedUrlLength] = 0x00;
    buffer[14 + convertedUrlLength] = 0x01;
    // 2 byte class, use 00 01
    buffer[15 + convertedUrlLength] = 0x00;
    buffer[16 + convertedUrlLength] = 0x01;


    if (sendto(sockfd, buffer, dataLength, 0, converted_addr, addrlen) == -1) {
        puts("sendto failed somehow...");
        return -1;
    }

    // get response from socket
    int size;
    unsigned char *response_buffer;
    unsigned char temp_buffer[MAX_RESPONSE_BYTES] = {0};
    size = recv(sockfd, temp_buffer, 100, 0);
    response_buffer = malloc(size);
    memcpy(response_buffer, temp_buffer, size);

    // 2 bytes like before
    if (buffer[0] != response_buffer[0] || buffer[1] != response_buffer[1]) {
        puts("Transactions IDs didn't match...");
        return -1;
    }

    // should be done with this by this point
    free(buffer);

    // next 2 bytes are flags
    // There's probably lots of stuff we could/should do here, but minimum is make sure no errors...
    if (response_buffer[3] & 0x0F) { // i.e. mask last 4 bits of these 2 bytes
        // if not 0000...
        puts("There was some error...");
        return -1;
    }

    // skip questions (response_buffer[4-5])

    // assert answers >= 1
    uint16_t numAnswers = (response_buffer[6] << 8) | response_buffer[7];
    if (numAnswers == 0) {
        puts("There were no answers...");
        return -1;
    }

    // skip next 2+2 bytes because I don't care
    // skip next `convertedUrlLength` IDs matching should be good enough
    // skip the 4 bits after

    struct Answer *parsedAnswers = malloc(sizeof(Answer));
    int offsetToAnswers = 8 + 4 + convertedUrlLength + 5;
    handleAnswers(parsedAnswers, offsetToAnswers + response_buffer, size - offsetToAnswers, numAnswers);
    int j;
    for (j = 0; j < numAnswers; j++) {
        printf("Answer #%d \n", j + 1);
        puts(parsedAnswers[j].type);
        puts(parsedAnswers[j].content);
    }
    printf("Exiting...");

    // is this even necessary
    free(parsedAnswers);
    free(response_buffer);

    return 1;
}