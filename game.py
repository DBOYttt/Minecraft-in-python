from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController 


app = Ursina()

class Voxel(Button):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube', 
            origin_y = .5,
            texture = 'gray_cube',
            color = color.color(0, 0, random.uniform(0.9, 1.0)),
            highlight_color = color.lime,
        )

app.run()
