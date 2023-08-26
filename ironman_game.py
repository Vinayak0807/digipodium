import pgzrun
from random import randint

HEIGHT = 700
WIDTH = 1000
w, h = WIDTH, HEIGHT
music.play('remix')
p = Actor('ironman', (w // 2, h // 2))
e = Actor('alien', (w // 2, 200))
c = Actor('coin', (w // 2, h - 100))
score = 0
game_state = -1  # -1: Start screen, 0: In-game, 1: Game Over, 2: Victory

def draw():
    global game_state
    if game_state == -1:
        start_screen()
    elif game_state == 0:
        screen.fill('black')  
        p.draw()
        e.draw()
        c.draw()
        screen.draw.text(f'Score: {score}', (10, 10), color='cyan', fontsize=30)
    elif game_state == 1:
        screen.draw.text('Game Over', (w // 2, h // 2), color='red', fontsize=60)
    elif game_state == 2:
        screen.draw.text('You Win', (w // 2, h // 2), color='yellow', fontsize=60)

def update():
    global game_state
    if game_state == 0:
        enemy_update()
        player_update()
        score_update()

def start_screen():
    screen.fill('black') 
    screen.draw.text('Space Adventure Game', (w // 2, h // 2 - 60), color='blue', fontsize=60, align='center')
    screen.draw.text('Press SPACE to Start', (w // 2, h // 2 + 60), color='cyan', fontsize=40, align='center')

def on_key_down(key):
    global game_state
    if game_state == -1 and key == keys.SPACE:
        game_state = 0

def enemy_update():
    if c.x > e.x:
        e.x += 3
    if c.x < e.x:
        e.x -= 3
    if c.y > e.y:
        e.y += 3
    if c.y < e.y:
        e.y -= 3

def score_update():
    global score, game_state
    if p.colliderect(c):
        score += 10
        c.x = randint(0, w)
        c.y = randint(0, h)
        sounds.action.play()  
    if e.colliderect(c):
        score -= 10
        c.x = randint(0, w)
        c.y = randint(0, h)
        sounds.action.play()  
    if score <= -60:
        game_state = 1
    if score >= 60:
        game_state = 2

def player_update():
    global p
    if keyboard.left:
        p.x -= 8
    elif keyboard.right:
        p.x += 8
    elif keyboard.up:
        p.y -= 8
    elif keyboard.down:
        p.y += 8
    
    
    if p.right < 0:
        p.left = WIDTH
    if p.left > WIDTH:
        p.right = 0
    if p.bottom < 0:
        p.top = HEIGHT
    if p.top > HEIGHT:
        p.bottom = 0

pgzrun.go()



