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
#define MAX_RESPONSE_BYTES 128

void printAnswers(unsigned char *responseBuffer, int numAnswers, uint8_t encodedUrlLength) {
    int i;
    int offset = 0;
    uint8_t isARecord, isCName;

    int offsetToAnswers = 8 + 4 + encodedUrlLength + 5;
    unsigned char *answersSection = responseBuffer + offsetToAnswers;

    for (i = 0; i < numAnswers; i++) {
        isARecord = answersSection[3 + offset] == 0x01;
        isCName = answersSection[3 + offset] == 0x05;

        if (answersSection[2 + offset] != 0x00 ||
            (!isARecord && !isCName)) {
            puts("Skipping answer because it contains something other than a CNAME or IP");
            continue;
        }

        uint8_t contentSize;
        contentSize = (answersSection[10 + offset] << 8) | answersSection[11 + offset];
        if (isARecord) {
            printf("Found A Record -> %s\n", byteArrayToIPStr(&answersSection[12 + offset]));
        } else {
            printf("Found CNAME -> %s\n", &answersSection[12 + offset]);
        }
        offset += 12 + contentSize;
    }
}

void buildBuffer(char *buffer, unsigned short transactionId, char *url, int urlLength) {
    uint8_t encodedUrlLength = urlLength + 1;

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

unsigned short getNumAnswers(int size, unsigned short transactionId, unsigned char *responseBuffer) {
    if (size < 20) {
        // 20 is arbitrary, not sure this is worth
        puts("Response wasn't long enough to be meaningful... something is definitely wrong");
        return -1;
    }

    // check to make sure the transactionId is correct
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

    // assert answers >= 1
    return (responseBuffer[6] << 8) | responseBuffer[7];
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Requires one arg, like `laughtears.com`");
        exit(1);
    }

    // open socket
    int sockfd;
    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    // make request to dns server
    unsigned short transactionId = getRandomTwoByteId();
    char *url = argv[1];
    uint8_t urlLength = getStringLength(url);
    uint8_t encodedUrlLength = urlLength + 1;
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
    char *tempBuffer = malloc(MAX_RESPONSE_BYTES);
    int size = recv(sockfd, tempBuffer, MAX_RESPONSE_BYTES, 0);
    if (size == MAX_RESPONSE_BYTES) {
        // TODO: how can we avoid using MAX_RESPONSE_BYTES?
        puts("Haven't handled the case where we read in the MAX_RESPONSE_BYTES...");
        return -1;
    }
    unsigned char *responseBuffer = malloc(size);
    memcpy(responseBuffer, tempBuffer, size);
    free(tempBuffer);

    unsigned short numAnswers = getNumAnswers(size, transactionId, responseBuffer);
    if (numAnswers < 0) {
        return -1;
    } else if (numAnswers == 0) {
        puts("Response had no answers...");
    }

    printAnswers(responseBuffer, numAnswers, encodedUrlLength);
    free(responseBuffer);
    printf("Exiting...");

    return 1;
}