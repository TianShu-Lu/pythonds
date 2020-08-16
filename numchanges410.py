"""
递归算法解决找零兑换问题：
1.基本结束条件（最小问题规模为）：找零面值等于某种硬币
2.减小问题规模，调用自身：对每种硬币减去一次，再分别求出最小找零个数
3.为了解决重复计算的问题：需要用一个列表把 中间找零结果的最优解 保存起来！！递归调用时先查表如果该面值已经存在最优解直接返回最优解的结果，不需要重复调用
"""


def numchange(coinvaluelist, change, knownresults):
    minnum = change
    if change in coinvaluelist:
        knownresults[change] = 1
        return 1  # 最小问题规模，如果找零面值直接等于某一个硬币，返回1
    elif knownresults[change] > 0:
        return knownresults[change]  # 查表成功， 即立即返回已经保存好的结果
    else:
        for coin in [c for c in coinvaluelist if c <= change]:
            num = 1 + numchange(coinvaluelist, change - coin, knownresults)
            if num < minnum:
                minnum = num
                knownresults[change] = minnum
        return minnum


if __name__ == '__main__':
    print(numchange([1, 5, 10, 25, 21], 63, [0] * 64))
