import matplotlib.colors as mcolors
import random


def random_color_generator():
    color = random.choice(list(mcolors.CSS4_COLORS.keys()))
    return color


random_color = random_color_generator()

from simpletk import *
from tkinter.messagebox import *
app =TApplication("Тестовая форма")
app.minsize = (400,200)
app.maxsize = (500,300)
app.position = (1100,500)

def AskOnExit(event):
    if askokcancel('Подтверждение выхода',"Выйти?"):
        app.destroy()

def ColOnClick(event):
    random_color = random_color_generator()
    app.background = random_color


app.onCloseQuery = AskOnExit
app.onClick = ColOnClick


app.run()
