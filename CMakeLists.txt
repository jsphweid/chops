cmake_minimum_required(VERSION 3.20)
project(chops C)

set(CMAKE_C_STANDARD 11)

add_executable(chops
        c_networking/dns.c)
