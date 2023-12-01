# import  another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen

timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.position()
for steps in range(100):
    for c in ('blue','red','green'):
        timmy.color(c)
        timmy.forward(500)
        timmy.right(500)
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
