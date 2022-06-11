from ast import Break
import imp
from tracemalloc import stop
from turtle import position
from ursina import *
from ursina import PositionLimiter

app = Ursina()

bar_1 = Entity(model = 'cube', scale = (3,1,0), texture = '43bba1622c60137.png', position = Vec3(0,2,0))
bar_1_button = Button(model = 'cube', scale = (0.36,0.12), texture = '43bba1622c60137.png', position = Vec3(0,0.246,0))

def action():
    

bar_2_quit = Entity(model = 'cube', scale = (3,1,0), texture = 'Zrzut ekranu 2022-06-11 205741.png', position = Vec3(0,0,0), on_click = action)
bar_2_quit_button = Button(model = 'cube', scale = (0.36,0.12), texture = 'Zrzut ekranu 2022-06-11 205741.png', position = Vec3(0,0,0))



app.run()