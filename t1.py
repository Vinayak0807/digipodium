import pgzrun
import math

# Set the screen dimensions
HEIGHT = 700
WIDTH = 1000
w, h = WIDTH, HEIGHT

# Load music and play it (assuming 'remix' is a valid music file)
# music.play('remix')  # Commented out for testing without sound

# Create Actor instances for characters
p = Actor('ironman', (w // 2, h // 2))
e = Actor('alien', (w // 2, 200))
c = Actor('coin', (w // 2, h - 100))

# Flag to track game over state
game_over = False

def draw():
    # Clear the screen with a white background
    screen.fill('white')
    
    # Draw the characters on the screen
    p.draw()
    e.draw()
    c.draw()
    
    # Draw game over message if game is over
    if game_over:
        screen.draw.text("Game Over", center=(w // 2, h // 2), fontsize=60, color='red')

def update():
    global game_over
    
    if not game_over:
        enemy_update()
        coin_update()
        player_update()
        
        # Check for collision between ironman and coin
        if p.colliderect(c):
            game_over = True
        
        # Check for collision between ironman and alien
        if p.colliderect(e):
            game_over = True

def enemy_update():
    global e
    
    # Move the alien in a circular path
    angle = math.radians(clock.time * 50)  # Adjust the rotation speed as needed
    radius = 150  # Adjust the radius of the circular path
    e.x = w // 2 + int(radius * math.cos(angle))
    e.y = h // 2 + int(radius * math.sin(angle))

def coin_update():
    global c
    
    # Move the coin in an elliptical path
    angle = math.radians(clock.time * 30)  # Adjust the rotation speed as needed
    a = 200  # Horizontal radius of the ellipse
    b = 100  # Vertical radius of the ellipse
    c.x = w // 2 + int(a * math.cos(angle))
    c.y = h // 2 - int(b * math.sin(angle))  # Inverted sin to make the coin move in the opposite direction

def player_update():
    global game_over
    
    # Control the player character's movement based on keyboard input
    if keyboard.left:
        p.x -= 5
    if keyboard.right:
        p.x += 5
    if keyboard.up:
        p.y -= 5
    if keyboard.down:
        p.y += 5
    
    # Keep the player within the screen bounds
    p.x = max(p.width // 2, min(w - p.width // 2, p.x))
    p.y = max(p.height // 2, min(h - p.height // 2, p.y))

pgzrun.go()



