def sysconvert(n, base):
    convertstr = "0123456789ABCDEF"
    if n < base:
        return convertstr[n]
    else:
        return sysconvert(n//base, base) + convertstr[n%base]


if __name__ == '__main__':
    print(sysconvert(1453, 16))