'''
谢尔宾斯基三角形是由三个尺寸减半的谢尔宾斯基三角形按照品字型堆叠而成的，只能做出degree为有限时候的谢尔宾斯基三角形。degree=0为迭代结束条件
'''

import turtle


def sierpinski(degree, points):
    colormap = ["blue", "red", "green", "white", "yellow", "orange"]
    drawTriangle(points, colormap[degree])
    if degree > 0:
        sierpinski(degree - 1,
                   {"left": points["left"],
                    "top": getMid(points["left"], points["top"]),
                    "right": getMid(points["right"], points["left"])})
        sierpinski(degree - 1,
                   {"left": getMid(points["left"], points["top"]),
                    "top": points["top"],
                    "right": getMid(points["right"], points["top"])})
        sierpinski(degree - 1,
                   {"left": getMid(points["left"], points["right"]),
                    "top": getMid(points["right"], points["top"]),
                    "right": points["right"]})


def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points["top"])
    t.pendown()
    t.begin_fill()
    t.goto(points["left"])
    t.goto(points["right"])
    t.goto(points["top"])
    t.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


t = turtle.Turtle()
points = {"left": (-200, -100),
          "top": (0, 200),
          "right": (200, -100)}
sierpinski(5, points)
turtle.done()


