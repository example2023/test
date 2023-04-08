import pgzrun
#comment
WIDTH = 600 # Ширина окна
HEIGHT = 300 # Высота окна

TITLE = "Инопланетный раннер" # Заголовок окна игры
FPS = 30 # Количество кадров в секунду

alien = Actor('alien', (50, 240))
fon = Actor("fon")

def draw():
    fon.draw()
    alien.draw()
    
def update(dt):
    alien.x = alien.x + 5
    
pgzrun.go()
