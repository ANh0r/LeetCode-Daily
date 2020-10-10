import IPy


def is_ip(address):
    if '.' not in address:
        print("lack of dot '.'")
        return False
    try:
        IPy.IP(address)
        return True
    except Exception as e:
        print(e)
        return False


def ip2dot(ip: int) -> str:
    p1 = (ip >> 24) % 256
    p2 = (ip >> 16) % 256
    p3 = (ip >> 8) % 256
    p4 = ip % 256
    return f'{p1}.{p2}.{p3}.{p4}'


def dot2ip(dot :str) -> int :
    tem = dot.split(".")
    int_ip = [int(tem[i]) % 256 for i in range(4)]
    return (int_ip[0] << 24) + (int_ip[1] << 16) + (int_ip[2] << 8) + (int_ip[3])



def main():
    # tips = '''Warning: This test just for CORRECT form of IP address and NO DESIGN for validating the format.
    #  Please input normal and right input, thank you.'''
    while 1:
        input_ip = input("Please input the ip address with '.' ")
        # print("*******"+tips+"******\n")
        if is_ip(input_ip):
            ans = dot2ip(input_ip)
            print(f'{input_ip} dot transfer to ip(unsigned int) is {ans}')
            input2 = int(input("input the uint you got to validate the dot address:"))
            if input2 > 4294967295 or input2 <= 0:
                print("input error!\n")
                continue
            print(f'{input2} is the ip of dot {ip2dot(input2)}')


if __name__ == "__main__":
    main()