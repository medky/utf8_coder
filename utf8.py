# "二"
# unicode:  0x4E8C
# utf8:     b'\xe4\xba\x8c'

#ref: http://www.ietf.org/rfc/rfc3629.txt
#   Char. number range  |        UTF-8 octet sequence
#      (hexadecimal)    |              (binary)
#   --------------------+---------------------------------------------
#   0000 0000-0000 007F | 0xxxxxxx
#   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

def chr_encode(code):
    if code < 0x80:
        return [code]
    if code < 0x800:
        return [0xc0 + ((code>>6)&0x1f),
                      0x80 + (code&0x3f)]
    if code < 0x10000:
        return [0xe0 + ((code>>12)&0xf),
                      0x80 + ((code>>6)&0x3f),
                      0x80 + (code&0x3f)]
    if code < 0x200000:
        return [0xf0 + ((code>>18)&0x7),
                      0x80 + ((code>>12)&0x3f),
                      0x80 + ((code>>6)&0x3f),
                      0x80 + (code&0x3f)]

def utf8_encode(unicode_array):
    ret = []
    for i in unicode_array:
        ret += chr_encode(i)
    return ret

# 通过code计算需要的长度
def utf8_need_len(code):
    if code < 0x80:
        return 1
    if code < 0xdf:  #5,6
        return 2
    if code < 0xef:  #4,6,6
        return 3
    if code < 0xf7:  #3,6,6,6
        return 4

def chr_decode(array, index=0):
    code = array[index]
    if code < 0x80:  #7
        return code
    if code < 0xdf:  #5,6
        return ((array[index]&0x1f)<<6) + (array[index+1]&0x3f)
    if code < 0xef:  #4,6,6
        return ((array[index]&0xf)<<12) + ((array[index+1]&0x3f)<<6) \
               + (array[index+2]&0x3f)
    if code < 0xf7:  #3,6,6,6
        return ((array[index]&0x7)<<18) + ((array[index+1]&0x3f)<<12) \
                + ((array[index+2]&0x3f)<<6) + (array[index+3]&0x3f)

def utf8_decode(utf8_array):
    ret = []
    index = 0
    total = len(utf8_array)
    while True:
        if index >= total:
            break
        need = utf8_need_len(utf8_array[index])
        if index+need > total:
            break
        ret.append(chr_decode(utf8_array, index))
        index += need
    return ret

def test_utf8():
    s = ["你是谁", "1234434", "QQQasasd", "遗传很长的字符串啊实打实放到地方地方地方"]
    for i in s:
        text = [ord(j) for j in i]
        assert(bytes(utf8_encode(text)) == i.encode())
    for i in s:
        utf8_bytes = i.encode()
        myres = utf8_decode(utf8_bytes)
        myres = ''.join([chr(j) for j in myres])
        assert(myres == i)

test_utf8()
