# Новогодняя открытка
from logging import root
from tkinter import *
from PIL import ImageTk, Image
import random

def happy_new_year(name):
    global indicator, indicator_count, root, cHeight, cWidth, canvas
    print(f'С Новым годом, {name}!')  # Press Ctrl+F8 to toggle the breakpoint.
    root = Tk()
    root.title(f'С Новым годом, {name}!')
    root.resizable(width=False, height=False)
    cWidth = 1280
    cHeight = 720

    canvas = Canvas(root, width=cWidth, height=cHeight, bg='#002655')
    canvas.pack()
    image = Image.open('yelka.png')
    image = image.resize((450, 511), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
    image = ImageTk.PhotoImage(image)
    canvas.create_image(80, 100, image=image, anchor=NW)

    text = '''
Пусть отзовется искоркой тепла,
Этот праздник славный в сердце каждом,
Так, чтоб душа от счастья расцвела,
И чтобы сказкой стала жизнь однажды!
Он воплотит заветные мечты,
Самые прекрасные и смелые надежды,
И в мире станет больше доброты.
В этот праздник зимний, белоснежный!
    '''.strip()
    canvas.create_text(cWidth * 2 / 3, cHeight / 2, text=text, fill='white', font='Times 24 bold' )
    create_snow("tagOne", 0)
    create_snow("tagTwo", 1)
    indicator = canvas.create_oval(23, -5, 28, 0, fill="white")
    indicator_count = 0
    motion()
    root.mainloop()


def create_snow(t, n):
    global indicator, indicator_count, root, cHeight, cWidth, canvas
    for i in range(500):
        x = random.randint(1, cWidth)
        y = random.randint(-cHeight * n - 8, cHeight * (1 - n))
        w = random.randint(3, 8)
        canvas.create_oval(x, y, x + w, y + w, fill="white", tag=t)

def motion():
    global indicator, indicator_count, root, cHeight, cWidth, canvas

    canvas.move("tagOne", 0, 1)
    canvas.move("tagTwo", 0, 1)
    canvas.move(indicator, 0, 1)
    if canvas.coords(indicator)[1] < cHeight + 1:
        root.after(20, motion)
    else:
        canvas.move(indicator, 0, -cHeight -5)
        root.after(20, motion)
        if indicator_count == 0:
            canvas.delete("tagOne")
            create_snow("tagOne", 1)
            indicator_count = 1
        else:
            canvas.delete("tagTwo")
            create_snow("tagTwo", 1)
            indicator_count = 0

if __name__ == '__main__':
    happy_new_year('Дима')