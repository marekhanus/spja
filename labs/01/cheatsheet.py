# Useful functions, numbers, strings

a = 'hey'
type(a)     # str
id(a)       # address of `a` object
dir(a)  # attributes and methods of `a`
help(a) # documentation of `a`


# Numbers
a = 5
b = 5
5 == 5      # True, same value
-5 is -5    # True, same address (same object)
-6 is -6    # False, different object (only integers [-5, 256] are interned/cached in CPython)
a = 555555555555555555555555555555555555 # arbitrarily large ints
2 / 4       # 0.5, float division by default
2 // 4      # 0, integer division

type(5)     # int
type(5.0)   # float


# Strings
a = 'hello'
a[0] = 'a'      # error, strings are immutable
len(a)          # 5
'h' in a        # True
a + ' world'    # 'hello world'
emoji = '👍'     # Unicode by default
'  data \n'.strip() # 'data' (strips whitespace)
'hey how are you'.split(' ') # ['hey', 'how', 'are', 'you'] (splits string by spaces)


# Formatting
"{}: {}".format('a', 'b')   # 'a: b'
"{1}: {0}".format('a', 'b') # 'b: a' 
"{a}: {b}".format(a=1, b=2) # '1: 2'
"{:.2f}".format(2.33333)    # 2.33

# Multi-line strings
"""
This string spans multiple lines and keeps whitespace
    space before this are kept
"""


# Data types are checked
'1' + 2         # error
int('1') + 2    # 3
'1' + str(2)    # '12'
