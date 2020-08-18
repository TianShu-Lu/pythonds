"""
动态规划算法解决零钱找零问题：
1.从最简单的“一分钱找零”的最优解开始，逐步递加上去到我们所需的找零数
2.递加的过程能保证每一分递加后都是最优解的关键在，前一步更少钱数的最优解已经解出。
"""


def dpnumchange(coinvaluelist, change, minCoins, coinUsed):
    for cent in range(1, change + 1):  # 从1开始递加，逐个计算最优解
        min = cent  # 初始化该cent对应的最优解，最大即为cent
        newcoin = sorted(coinvaluelist)[0]  # 初始化该cent最后一次选择找零的硬币  最差情况为coinvaluelist中最小的硬币值
        for i in [c for c in coinvaluelist if c <= cent]:  # 分别减去不同值的一个硬币，并通过查表查到上一步的最优解
            if minCoins[cent - i] + 1 < min:
                min = minCoins[cent - i] + 1
                newcoin = i
        minCoins[cent] = min  # 把当前cent对应的最优解记录在minCoins中
        coinUsed[cent] = newcoin  # 把最后一次选择的硬币保存在coinUsed中
    return minCoins[change]


def printCoins(change, coinUsed):
    while change:
        print(coinUsed[change])
        change = change - coinUsed[change]


if __name__ == '__main__':
    amt = 63
    coinUsed = [0]*(amt+1)
    minCoins = [0]*(amt+1)
    print(dpnumchange([1, 5, 10, 21, 25], amt, minCoins, coinUsed))
    printCoins(63, coinUsed)  # 疑问1：全局变量和局部变量重名的话可以被函数改变吗？
    print(coinUsed)

