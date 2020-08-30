"""
解题思路：先把M进制的数转换为10进制，然后再根据402转换为N进制
"""


def sysconvertMN(num, m, n):
    decnum = 0
    for i in range(len(str(num))):
        decnum = decnum + num // (10 ** i) % 10 * (m ** i)
    return sysconvert(decnum, n)


def sysconvert(n, base):
    convertstr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return convertstr[n]
    else:
        return sysconvert(n // base, base) + convertstr[n % base]


if __name__ == '__main__':
    print(sysconvertMN(473, 8, 16))
