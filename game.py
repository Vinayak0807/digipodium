import pgzrun
from random import randint

HEIGHT=700
WIDTH=1000
w, h = WIDTH, HEIGHT
music.play('remix')
p=Actor('ironman',(w//2,h//2))
e=Actor('alien',(w//2,200))
c=Actor('coin',(w//2,h-100))
score = 0
game_state = 0
def draw():
    if game_state == 0:
        screen.fill('white')
        p.draw()
        e.draw()
        c.draw()
        screen.draw.text(f'score :{score}',(10,10), color='red')
    elif game_state == 1:
        screen.draw.text(f'Game over', (w//2, h//2),color='red')
    elif game_state == 2:
        screen.draw.text(f'you win', (w//2, h//2),color='red')  
        pass


def update():
 if game_state == 0:
    enemy_update()
    player_update()
    score_update()

def enemy_update():
    if c.x > e.x:
        e.x += 2
    if c.x < e.x:
        e.x -= 2
    if c.y > e.y:
        e.y += 2
    if c.y < e.y:
        e.y -= 2    


def score_update():
    global score , game_state
    if p.colliderect(c):
        score += 10
        c.x = randint(0,w)    
        c.y = randint(0,h)   
        sounds.action.play() 
    if e.colliderect(c):
        score -= 10
        c.x = randint(0,w)    
        c.y = randint(0,h)   
        sounds.action.play()    
    if score <= -50:
        game_state = 1
    if score >= 50:
        game_state = 2        
def player_update():
    if keyboard.left:
        p.x -= 7
    elif keyboard.right:    
        p.x += 7
    elif keyboard.up:
        p.y -= 7
    elif keyboard.down:
        p.y += 7            
pgzrun.go()