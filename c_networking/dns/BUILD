load("//:defs.bzl", "c_binary")

c_binary(
    name = "dns",
    srcs = ["dns.c"],
    deps = [
        "//util:encode_url",
        "//util:ip_string",
        "//util:random",
        "//util:str",
    ],
)
