# coding: utf-8
import turtle as t
import lsyslib as ls
t.pencolor('gray')
t.penup()
t.setpos(-400,-300)
t.setheading(40)
t.pendown()
t.delay(0)
t.pensize(2)
#t.tracer(False)

angle = 0
head = 0
position = (0,0)
stack = []

def ffun():
    t.fd(5)

def minusfun():
    global angle
    t.left(angle)

def plusfun():
    global angle
    t.right(angle)

def xfun():
    return

def push():
    global stack
    global position 
    global head 
    position = (t.xcor(),t.ycor())
    head = t.heading()
    stack.append((head,position))

def pop():
    global head
    global position
    global stack
    head,position = stack.pop()
    t.penup()
    t.setpos(position)
    t.setheading(head)
    t.pendown()

angle = 60
r = [('F','F+F--F+F'),('X','F+[[X]-X]-F[-FX]+X')]
dicti = {
        'F':ffun,
        'G':ffun,
        'X':xfun,
        'Y':xfun,
        '+':plusfun,
        '-':minusfun,
        '[':push,
        ']':pop
        }

start = 'F--F--F'
start = ls.findnth(start,r,4)
print(start)
ls.execute(start,dicti)
t.exitonclick()
