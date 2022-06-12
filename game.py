from ursina import * 
from menugame import bar_1_button

if on_click() == application.quit():
    app = Ursina()

    app.run()
