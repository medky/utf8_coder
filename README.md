utf8 与 unicode编码映射关系如下:

#ref: http://www.ietf.org/rfc/rfc3629.txt

Char. number range  |        UTF-8 octet sequence
   (hexadecimal)    |              (binary)
   
--------------------+--------------------------------

0000 0000-0000 007F | 0xxxxxxx

0000 0080-0000 07FF | 110xxxxx 10xxxxxx

0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx

0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx


utf8_coder.py 主要就是实现编码解码
