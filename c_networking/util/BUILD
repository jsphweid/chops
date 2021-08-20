load("//:defs.bzl", "c_library", "c_test")

c_library(
    name = "ip_string",
    srcs = ["ip_string.c"],
    hdrs = ["ip_string.h"],
    visibility = ["//visibility:public"],
)

c_test(
    name = "ip_string_test",
    srcs = ["ip_string_test.c"],
    deps = [
        ":ip_string",
        ":test_utils",
    ],
)

c_library(
    name = "encode_url",
    srcs = ["encode_url.c"],
    hdrs = ["encode_url.h"],
    visibility = ["//visibility:public"],
)

c_test(
    name = "encode_url_test",
    srcs = ["encode_url_test.c"],
    deps = [
        ":encode_url",
        ":test_utils",
    ],
)

c_library(
    name = "str",
    srcs = ["str.c"],
    hdrs = ["str.h"],
    visibility = ["//visibility:public"],
)

c_test(
    name = "str_test",
    srcs = ["str_test.c"],
    deps = [
        ":str",
        ":test_utils",
    ],
)

c_library(
    name = "test_utils",
    hdrs = ["test_utils.h"],
    visibility = ["//visibility:public"],
)
