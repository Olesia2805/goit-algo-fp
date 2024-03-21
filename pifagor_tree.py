import turtle
import math

def draw_pifagor_tree(depth, size):

    if depth == 0:
        return
    
    turtle.forward(size)
    turtle.left(45)
    draw_pifagor_tree(depth - 1, size / math.sqrt(2))
    turtle.right(90)
    draw_pifagor_tree(depth - 1, size / math.sqrt(2))
    turtle.left(45)
    turtle.backward(size)

def main():

    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.color("green")
    draw_pifagor_tree(8, 200)
    turtle.done()

if __name__ == "__main__":
    main()
