'''
Author: jdr
Date: 2023.6.14
'''
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

def decode(s):
    if s is None:
        return ""
    else:
        s3 = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c == '^':
                s2 = s[i + 1:i + 5]
                s3 = s3 + chr(int(s2, 16))
                i += 4
            elif c == '~':
                s1 = s[i + 1:i + 3]
                s3 = s3 + chr(int(s1, 16))
                i += 2
            else:
                s3 = s3 + c
            i += 1
        return s3



