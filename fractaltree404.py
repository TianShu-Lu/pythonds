import turtle

def tree(branch_len):
    if branch_len > 5: # 递归结束条件：如果树干太短则不画
        t.forward(branch_len)  # 画树干
        t.right(20)  # 转向右边画出右边的小树
        tree(branch_len-15)
        t.left(40) # 画左边的小树
        tree(branch_len-15)
        t.right(20)  # 回正
        t.backward(branch_len)


# 主程序
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor("green")
t.pensize(2)
tree(75)
t.hideturtle()
turtle.done()
