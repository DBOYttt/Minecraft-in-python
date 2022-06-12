import imp
from turtle import position
from ursina import *
from ursina import PositionLimiter

app = Ursina()

bar_1_button = Button(model = 'cube', scale = (0.36,0.12), position = Vec3(0,0.1,0), text = 'Play')

bar_2_button = Button(model = 'cube', scale = (0.36,0.12), position = Vec3(0,-0.1,0), text = 'quit', on_click = application.quit)

screen = Entity(model = 'cube', texture = 'minecraftjavaeditiontlo.jpg', scale = (15,8))




app.run()