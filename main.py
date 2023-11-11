import turtle
import os

# Set up the screen
window = turtle.Screen()
window.title("Space Invaders")
window.bgcolor("black")
window.setup(width=600, height=600)

# Create the player spaceship
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player_speed = 15

# Create a list of enemies (aliens)
enemies = []

# Create the enemy spaceship
for _ in range(5):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = 100  # Initial enemy X position
    y = 250  # Initial enemy Y position
    enemy.setposition(x, y)
    enemies.append(enemy)

# Create a bullet for the player
bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 20
bullet_state = "ready"

# Function to move the player left
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

# Function to move the player right
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

# Function to fire a bullet
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# Keyboard bindings
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += 2  # Adjust the speed of the enemies
        enemy.setx(x)

        # Check for collision with player
        if player.distance(enemy) < 20:
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            window.bye()

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check if the bullet has hit the top edge
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

window.mainloop()
