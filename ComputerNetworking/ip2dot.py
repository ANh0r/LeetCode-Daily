"""
ip2dot:uint to ip address like xx.xxx.x.x
tips:
1.the reverse method of dot2ip
2.so the top 1st part(4 in total) will be the uint >> 24
3.as above,forward.

@param uint
@return str
@author Ryan
"""

def ip2dot(ip: int) -> str:
    p1 = (ip >> 24) % 256
    p2 = (ip >> 16) % 256
    p3 = (ip >> 8) % 256
    p4 = ip % 256
    return f'{p1}.{p2}.{p3}.{p4}'