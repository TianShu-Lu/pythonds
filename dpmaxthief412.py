"""
动态规划算法解决博物馆大盗问题：
m(i, W)表示前i个宝物中，组合不超过W重量所能获得的最大价值
"""

# 宝物的重量和价值， 本题为5个宝物
tr = [None, {"w": 2, "v": 3}, {"w": 3, "v": 4}, {"w": 4, "v": 8}, {"w": 5, "v": 8}, {"w": 9, "v": 10}]

# 大盗的最大承重
max_w = 20

# 初始化表格m{(i, w)}, 当i为0（表示什么都不取走）或者w为0时，m为0，用字典来创建
m = {(i, w): 0 for i in range(0, len(tr)) for w in range(0, max_w + 1)}

# 从（1,1）开始逐个计算表格
for i in range(1, len(tr)):
    for w in range(1, max_w+1):
        if tr[i]["w"] > w:
            m[(i, w)] = m[(i-1, w)]  # 第一种情况当第i个宝物重量已经大于最大承重
        else:
            m[(i, w)] = max(m[(i-1, w)], m[(i-1, w-tr[i]["w"])] + tr[i]["v"])

print(m[(len(tr)-1, max_w)])
