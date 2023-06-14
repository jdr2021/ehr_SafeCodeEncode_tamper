"""
Author: jdr
"""

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    return encode(payload)

def encode(s):
    if s is None:
        return ""
    else:
        s3 = ""
        for i in range(len(s)):
            s2 = ""
            k = 0
            c = s[i]
            if ord(c) > 255:
                s2 = hex(ord(c))[2:].zfill(4)
                s3 += "^" + s2
            elif (str(c) >= '0' and (str(c) <= '/' or str(c) >= 'A') and (str(c) <= 'Z' or str(c) >= 'a') and str(c) <= 'z'):
                s3 += c
            else:
                s2 = hex(ord(c))[2:].zfill(2)
                s3 += "~" + s2

        return s3