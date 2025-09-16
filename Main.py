from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup( width=500,height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color would u like to choose: "
                                                          "red/orange/yellow/purple/green/blue ")
print(user_bet)

p_positions = [-100,-50,0,50,100,150]
all_turtles = []

color = ["red","orange", "yellow","purple","green","blue"]

for x in range(0,6):
    timmy = Turtle(shape = "turtle")
    timmy.color(color[x])
    timmy.penup()
    timmy.goto(x=-230, y = p_positions[x])
    all_turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Yay you won! The {winning_color} turtle is the winner. ")

            else:
                print(f"Ayy you lost.. The {winning_color} turtle is the winner ")


        random_distance = random.randint(1,10)
        turtle.forward(random_distance)
screen.exitonclick()
