#include <stdio.h>
#include <stdlib.h>

#define LOG_ERROR(...) fprintf(stderr, __VA_ARGS__)

static void _fatal_error(const char* message) {
    LOG_ERROR("%s", message);
    exit(EXIT_FAILURE);
}

#define AS_STRING(x) AS_STRING_INTERNAL(x)
#define AS_STRING_INTERNAL(x) #x

#ifdef CHECK
#error CHECK is already defined.
#endif

#define CHECK(condition)                                                                   \
    if (!(condition)) {                                                                    \
        _fatal_error(__FILE__ ":" AS_STRING(__LINE__) ": Check failed: " #condition "\n"); \
    }