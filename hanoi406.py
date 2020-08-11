'''
汉诺塔问题：一次只能搬走一个盘子，且大盘子不能叠在小盘子上。利用递归思想解决。不论多少个盘子都可以分解为是两个盘子的挪动问题，递归结束条件是只有一个盘子。最小规模问题是
挪动一个盘子
'''


def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)  # 先把大盘子上的所有小盘子挪走到中间柱子上
        moveDisk(height, fromPole, toPole)  # 再把大盘子挪到目标柱子上
        moveTower(height - 1, withPole, fromPole, toPole)  # 再把所有小盘子挪到目标柱子


def moveDisk(disk, fromPole, toPole):
    print(f"move disk{disk} from {fromPole} to {toPole}")


moveTower(3, "#1", "#2", "#3")
