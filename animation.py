import time
from tkinter import*
python_black= "#000000"


def animate():

    animation = Tk()
    canvas = Canvas(animation, width = 800 ,height = 600)
    canvas.pack()
    points = (100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110,)
    canvas.create_polygon(points, outline=python_black,
                fill='red', width=3)


    for x in range (0,100):
        canvas.move(1,8,0)
        animation.update()
        time.sleep(0.01)

    for x in range (0,100):
        canvas.move(1,-8,0)
        animation.update()
        time.sleep(0.01)




def main ():
    animate()

if __name__ == '__main__':
    main()

