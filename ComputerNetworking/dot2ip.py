"""
dot2ip: an ip address like xx.xxx.x.x to uint
tips: The uint comes as follows:

1.split .
2.every part will be added
3.32 bits in total,thus the 1st part will multiply 2 ^ 24 (For IPv4:
each 8 bit equal a Byte, 4 Bytes in an IP address)

@param str
@return uint
@author Ryan
"""

def dot2ip(dot :str) -> int :
    tem = dot.split(".")
    int_ip = [int(tem[i]) % 256 for i in range(4)]
    return (int_ip[0] << 24) + (int_ip[1] << 16) + (int_ip[2] << 8) + (int_ip[3])

# def dot2ip2(dotted: str) -> int:
#     a, b, c, d = [ int(i) % 256 for i in dotted.split('.', 3) ]
#     print(a,b,c,d)
#     return (a << 24) + (b << 16) + (c << 8) + d



