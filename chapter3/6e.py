import turtle
wn=turtle.Screen()
turt = turtle.Turtle()

sides = int(input("How many sides?"))
lengthofsides = int(input("How long should the sides be ?"))

for i in range (sides):
    turt.forward(100)
    turt.left(360/sides)