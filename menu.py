import imp
from turtle import position
from ursina import *
from ursina import PositionLimiter

app = Ursina()

bar_1 = Entity(model = 'cube', scale = (3,1,0), texture = '43bba1622c60137.png', position = Vec3(0,2,0))
bar_1_button = Button(model = 'cube', scale = (0.36,0.12), texture = '43bba1622c60137.png', position = Vec3(0,0.246,0))



app.run()