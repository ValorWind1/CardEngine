import pyglet
def playMusic():
    try:

        music = pyglet.media.load(file)

        music.play()
    except:
        print("error")


pyglet.app.run()
