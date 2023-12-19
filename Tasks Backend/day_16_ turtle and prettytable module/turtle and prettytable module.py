
# import turtle
# from turtle import Turtle,Screen
# temmy=Turtle()
# temmy.shape("turtle")
# temmy.color("red")
# temmy.forward(100)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
#

# ***************************************************************************

from prettytable import PrettyTable
tabel = PrettyTable()
tabel.add_column("type",["rang rovar","marcedis","honday","masaratiy"])
tabel.add_column("model",["2020","2012","210","2022"])
tabel.add_column("price",["$300000","$200000","$50000","$250000"])
tabel.align="c"
print(tabel)

