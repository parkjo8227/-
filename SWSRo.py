import turtle as t

rx = [] ; ry = []
move_cnt = 0

def move_robot(action):
    t.color("black")
    if action == 0:
        for i in range(move_cnt):
            t.goto(rx[i],ry[i])
    elif action == 1:
        t.color("blue")
        for i in range(move_cnt-1,-1,-1):
            t.goto(rx[i],ry[i])
    elif action == 2:
        t.color("red")
        t.goto(rx[move_cnt-1],ry[move_cnt-1])
    elif action == 3:
        t.color("yellow")
        t.goto(rx[0],ry[0])

def clicked(x,y):
    global move_cnt
    move_cnt += 1
    rx.append(x)
    ry.append(y)

def list_clear():
    global move_cnt
    del rx[1:move_cnt]
    del ry[1:move_cnt]
    move_cnt = 1

def key_move():
    move_robot(0)
def key_back():
    move_robot(1)
def key_s():
    move_robot(2)
def key_home():
    move_robot(3)
def key_clear():
    list_clear()
    t.clear()
def key_charge():
    t.pencolor("green")
    t.goto(405,-230)

t.setup(950,580)
t.title("탐사로봇 이동경로 지정/복귀(Space/S/BackSpace/H/C/X)")
t.bgpic(picname="floor.gif")
t.hideturtle()

t.addshape("robot.gif")
t.shape("robot.gif")
t.pensize(2)
t.speed(3)
t.penup()
clicked(295,-120)
t.goto(405,-230)
t.showturtle()
t.pendown()

t.onkey(key_move, "space")
t.onkey(key_back, "BackSpace")
t.onkey(key_s, "s")
t.onkey(key_home, "h")
t.onkey(key_clear, "c")
t.onkey(key_charge, "x")
t.onscreenclick(clicked)
t.listen()
