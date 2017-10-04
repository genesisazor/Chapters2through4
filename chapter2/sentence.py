import turtle
wn = turtle. Screen()
owen = turtle.Turtle()

def make_square(turt,size, num):
    for j in range(num):
         turt.forward(size)
         turt.left(90)
         turt.forward(2*size)

wn=turtle.Screen()
owen=turtle.Turtle()



make_square(owen,20,5)