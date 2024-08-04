import pgzrun
import random

WIDTH = 500
HEIGHT = 500

ash = Actor('ash')
ash.pos = (400,100)
pikachu = Actor('pikachu')
pikachu.pos = (150,300)
speed = 7
score = 0

def draw():
    screen.clear()
    pikachu.draw()
    ash.draw()
    screen.draw.text('score:' + str(score) ,center = (50,10), fontsize = 30 )


def place():
    pikachu.x = random.randint(0,WIDTH)
    pikachu.y = random.randint(0,HEIGHT)

def move():
    pikachu.x += speed
    pikachu.y += speed

  
def update():
    global score, speed
    move()
    if keyboard.left:
        ash.x = ash.x - 2
    if keyboard.right:
        ash.x = ash.x + 2
    if keyboard.up:
        ash.y = ash.y - 2
    if keyboard.down:
        ash.y = ash.y + 2
    if ash.colliderect(pikachu):
        score = score + 1
        place()

    if ash.left < 0:
        ash.left = 0
    if ash.right > WIDTH:
        ash.right = WIDTH
    if ash.top < 0:
        ash.top = 0
    if ash.bottom > HEIGHT:
      ash.bottom = HEIGHT

    if pikachu.left < 0:
        speed = speed*-1
    if pikachu.right > WIDTH:
        speed = speed*-1
    if pikachu.top <0:
        speed = speed*-1
    if pikachu.bottom > HEIGHT:
        speed = speed*-1

pgzrun.go()