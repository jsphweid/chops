#include <arpa/inet.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>

#include "util/encode_url.h"
#include "util/ip_string.h"
#include "util/random.h"
#include "util/str.h"

#define UDP_PORT 53
#define MAX_RESPONSE_BYTES 1024

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

void printAnswers(Answer *out, unsigned char *blob, int blobLen, int numAnswers) {
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

void buildBuffer(char *buffer, unsigned short transactionId, char *url, int urlLength) {
    int encodedUrlLength = urlLength + 1;

    buffer[0] = transactionId >> 8;
    buffer[1] = transactionId;
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
    // dynamic sized query
    char *encodedUrl = malloc(urlLength + 1);
    encodeUrl(encodedUrl, url, urlLength);
    memcpy(&buffer[12], encodedUrl, encodedUrlLength);  // (void *dst, const void *src, size_t n)
    free(encodedUrl);
    buffer[12 + encodedUrlLength] = 0x00;
    // 2 byte type, use 00 01
    buffer[13 + encodedUrlLength] = 0x00;
    buffer[14 + encodedUrlLength] = 0x01;
    // 2 byte class, use 00 01
    buffer[15 + encodedUrlLength] = 0x00;
    buffer[16 + encodedUrlLength] = 0x01;
}

struct sockaddr_in buildDnsDestAddr() {
    // TODO: how do we not return a whole struct? Is this bad?
    // You can't return a point that gets created in the fn obviously. You could malloc a single byte? idk
    struct sockaddr_in addr;
    struct in_addr ap;
    inet_aton("8.8.8.8", &ap);
    addr.sin_family = AF_INET;
    addr.sin_port = htons(UDP_PORT);
    addr.sin_addr = ap;
    return addr;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Requires one arg, like `laughtears.com`");
        exit(1);
    }

    int sockfd;
    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    unsigned short transactionId = getRandomTwoByteId();
    char *url = argv[1];
    int urlLength = getStringLength(url);
    int encodedUrlLength = urlLength + 1;
    int dataLength = 17 + encodedUrlLength;
    char *buffer = malloc(dataLength);
    buildBuffer(buffer, transactionId, url, urlLength);
    struct sockaddr_in addr = buildDnsDestAddr();
    struct sockaddr *destAddr = (struct sockaddr *)&addr;
    uint addrlen = sizeof(struct sockaddr_in);

    if (sendto(sockfd, buffer, dataLength, 0, destAddr, addrlen) == -1) {
        puts("sendto failed somehow...");
        return -1;
    }
    free(buffer);

    // get response from socket
    int size;
    unsigned char *responseBuffer;
    unsigned char tempBuffer[MAX_RESPONSE_BYTES] = {0};
    size = recv(sockfd, tempBuffer, 100, 0);
    responseBuffer = malloc(size);
    memcpy(responseBuffer, tempBuffer, size);

    // 2 bytes like before
    if (transactionId != (responseBuffer[0] << 8 | responseBuffer[1])) {
        puts("Transactions IDs didn't match...");
        return -1;
    }

    // next 2 bytes are flags
    // There's probably lots of stuff we could/should do here, but minimum is make sure no errors...
    if (responseBuffer[3] & 0x0F) {  // i.e. mask last 4 bits of these 2 bytes
        // if not 0000...
        puts("There was some error...");
        return -1;
    }

    // skip questions (responseBuffer[4-5])

    // assert answers >= 1
    uint16_t numAnswers = (responseBuffer[6] << 8) | responseBuffer[7];
    if (numAnswers == 0) {
        puts("There were no answers...");
        return -1;
    }

    // skip next 2+2 bytes because I don't care
    // skip next `encodedUrlLength` IDs matching should be good enough
    // skip the 4 bits after

    struct Answer *parsedAnswers = malloc(sizeof(Answer));
    int offsetToAnswers = 8 + 4 + encodedUrlLength + 5;
    printAnswers(parsedAnswers, offsetToAnswers + responseBuffer, size - offsetToAnswers, numAnswers);
    int j;
    for (j = 0; j < numAnswers; j++) {
        printf("Answer #%d \n", j + 1);
        puts(parsedAnswers[j].type);
        puts(parsedAnswers[j].content);
    }
    printf("Exiting...");

    // is this even necessary
    free(parsedAnswers);
    free(responseBuffer);

    return 1;
}