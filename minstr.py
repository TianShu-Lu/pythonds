from basic.queue import Queue
'''
可以用队列来解，但是比较麻烦；采用字符串切片的方式，把最左端的移到最右端，然后多次比较
'''
def Minstr(startstr):
    min = startstr
    for i in range(len(startstr)-1): # 通过循环一共可以生成n-1个与初始不一样的字符串
        startstr = startstr[1::] + startstr[0]
        if startstr < min:
            min = startstr
    return min


S = input()
print(Minstr(S))