#!/usr/bin/env python3

from cffi import FFI
import itertools

ffi = FFI()

lib = ffi.dlopen('./substrings.so')
print('Loaded lib {0}'.format(lib))

# Describe the data type and function prototype to cffi.
ffi.cdef('''
    uint32_t substr2(char* s1, char* s2);
                ''')


strings = [b'abracadabra',
           b'raccolta',
           b'frazione']

print(max([ lib.substr2(x,y) for (x,y) in itertools.combinations(strings, 2) ]))


