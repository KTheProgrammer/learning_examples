from turtle import Turtle, Screen

sammy = Turtle()
sammy.shape()
sammy.color("green")

for i in range(3):
  sammy.forward(100)
  sammy.right(120)
for i in range(4):
  sammy.color("red")
  sammy.forward(100)
  sammy.right(90)
for i in range(5):
  sammy.color("black")
  sammy.forward(100)
  sammy.right(72)
for i in range(6):
  sammy.color("blue")
  sammy.forward(100)
  sammy.right(60)
for i in range(7):
  sammy.color("purple")
  sammy.forward(100)
  sammy.right(51.4)
for i in range(8):
  sammy.color("orange")
  sammy.forward(100)
  sammy.right(45)
for i in range(9):
  sammy.color("grey")
  sammy.forward(100)
  sammy.right(40)
for i in range(10):
  sammy.color("pink")
  sammy.forward(100)
  sammy.right(36)
  
screen = Screen()
screen.exitonclick()
