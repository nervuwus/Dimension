import turtle

def init(coord_X: int, coord_Y: int) -> bool:
    if type(coord_X and coord_Y) is int:
        turtle.begin_fill()
        turtle.speed(0)
        turtle.goto(coord_X, coord_Y)
        return True
    else: return False

def square():
    for _ in range(0, 4):
        turtle.forward(30)
        turtle.left(90)

def difference(add_coord: int = 3) -> int:
    if type(add_coord) is int:
        x = turtle.xcor()
        y = turtle.ycor()
        turtle.goto(x + 3, y + 3)
    else: return -1

def reliable():
    pass

def fill():
    pass

def stop():
    turtle.end_fill()
    return True

def save(filename: str) -> str:
    turtle.getcanvas().postscript(file=f'{filename}.eps')
    return f"save as {filename}.eps"