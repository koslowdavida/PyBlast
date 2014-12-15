
__author__ = 'David Koslow'
import pygame
import pygame.key
import playerShip
import enemyShip
import Bullet

pygame.init()





#Define PI
PI = 3.141592653


# Define some colors and white and black
ORANGE = (255, 200, 0)
PURPLE = (255, 0, 255)
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)
YELLOW = (255, 255, 0)

#Create basic window
windowx = 1800
windowy = 1000
size = (windowx, windowy)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyBlast")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Enemy Purge
def enemy_purge(enemy_list, player):
    for i, o in enumerate(enemy_list):
        #No Health? Kill it (remove it from the enemy_list)
        if o.health < 1 and o.bump == False:
            player.radius = player.radius + o.radius//9
            player.level += 1
            player.damage += 1
            del enemy_list[i]
        elif o.health < 1 and o.bump == True:
            player.radius = player.radius - o.radius
            del enemy_list[i]
        #Offscreen? Kill it (remove it from the enemy_list)
        if o.y > windowy+50:
            del enemy_list[i]

    return enemy_list

#Enemy Spawn
def enemy_spawn(enemy_list):
    x = enemyShip.EnemyShip(windowx)
    enemy_list.append(x)
    return enemy_list

#Enemy Move
def enemy_move(enemy_list):
    if len(enemy_list) > 0:
        for i, o in enumerate(enemy_list):
            if o.direction == "up":
                o.y = o.y - o.speed
            else:
                o.y = o.y + o.speed
            #print (o.y)
    return enemy_list

#Enemy Draw
def update_enemy(enemy_list):
    for i, o in enumerate(enemy_list):
            pygame.draw.circle(screen, o.color, [o.x, o.y], o.radius, 0)


#Enemy Fire graphic

#Enemy Death Graphic



#Bullet Purge
def bullet_purge(bullet_list):
    #print ("bullet purge")
    for i, o in enumerate(bullet_list):
        #Offscreen? Delete it (remove it from the bullet_list)
        if o.y + int(.5 * o.radius) > windowy + 50 or o.y + o.radius < -20 or o.bump == True:
            del bullet_list[i]
            #print ("Bullet gone")

    return bullet_list

#Bullet spawn
def bullet_spawn(bullet_list, ship):
    #print ("Bullet spawns at " + str(ship.y))
    if ship.direction == "up":
        x = Bullet.Bullet(ship.x, ship.y-(int(.9*ship.radius)), ship.direction, ship.radius, ship.damage)
        bullet_list.append(x)
        #print("new bullet")
        return bullet_list
    if ship.direction == "down":
        x = Bullet.Bullet(ship.x, ship.y+(int(.9*ship.radius)), ship.direction, ship.radius, ship.damage)
        bullet_list.append(x)
        #print("new bullet")
        return bullet_list


#Bullet Move
def bullet_move(bullet_list):
    if len(bullet_list) > 0:
        for i, o in enumerate(bullet_list):
            if o.direction == "up":
                o.y = o.y - o.speed
            else:
                o.y = o.y + o.speed
            #print (o.y)
    return bullet_list

#Bullet Draw
def update_bullets(bullet_list):
    for i, o in enumerate(bullet_list):
        if o.direction == "up":
            pygame.draw.circle(screen, o.color, [o.x, o.y], o.radius, 0)
        else:
            pygame.draw.circle(screen, YELLOW, [o.x, o.y], o.radius, 0)


#Movement Subroutines
def moveup(y):
    #dShip's y coordinate is passed in and modified up
    return y-5

def movedown(y):
    ##Ship's y coordinate is passed in and modified down
    return y+5

def moveleft(x):
    ##Ship's x coordinate is passed in and modified to the left
    return x-5


def moveright(x):
    #Ship's x coordinate is passed in and modified to the right
    return x+5

#Circle_Position_Update
def update_circle(x, y, radius, level):
    if level > 127:
        level = 127
    pygame.draw.circle(screen, (255, level << 1, level << 1), [x, y], radius, 0)
    return

#Player Fire graphic
def shoot (x, y, radius):
    pygame.draw.circle(screen, YELLOW, [x, y- int(.9*radius)], radius//2, 0)

    #print("!BANG!")
    return 1

#Collision function
def collide(bullet_list, enemy_list, player, collision_flash_bang):
    #print (player.x, player.y)
    for i, o in enumerate(bullet_list):
        for f, p in enumerate(enemy_list):
            if o.direction == "up" and o.x+o.radius > p.x-p.radius and o.x-o.radius < p.x+p.radius and o.y+o.radius < p.y+p.radius and o.y+o.radius > p.y-p.radius and o.bump == False:
                o.bump = True
                p.health = p.health - o.damage
                print ("collision")
                #collision_flash_bang = 1
            if p.x + p.radius > player.x-player.radius and p.x - p.radius < player.x+player.radius and p.y - p.radius < player.y+player.radius and p.y + p.radius > player.y-player.radius:
                player.radius = player.radius - p.health
                p.health = 0
                p.bump = True
                collision_flash_bang = 1
        if o.direction == "down" and o.x > player.x-player.radius and o.x < player.x+player.radius and o.y < player.y+player.radius and o.y > player.y-player.radius and o.bump == False:
            o.bump = True
            player.radius = player.radius - o.damage
            player.health = player.health - o.damage
            print ("collision")
            collision_flash_bang = 1
    return collision_flash_bang

def flash(windowx, windowy):
    pygame.draw.circle(screen, ORANGE, [windowx//2, windowy//2], windowx, 0)

#PRINT YOU LOSE




































# -------- Main Program Loop -----------



#Control Flags
wflag = 0
sflag = 0
aflag = 0
dflag = 0
shootflag = 0
shootstopper = 0
pygame.key.set_repeat(0, 200)
collision_flash_flag = 0

#Game Pieces
player = playerShip.PlayerShip(windowx, windowy)
enemy_list = []
bullet_list = []
enemy_spawn_flag = 0
enemy_bullet_spawn_flag = 0
enemy_spawn_count = 0
player_death = False





while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close
            print("User asked to quit.")
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            #print (pressed)
            if pressed[119] == 1:
                wflag = 1
                print("W")
            if pressed[119] == 0:
                wflag = 0
            if pressed[115] == 1:
                sflag = 1
                print("S")
            if pressed[115] == 0:
                sflag = 0
            if pressed[97] == 1:
                aflag = 1
                print("A")
            if pressed[97] == 0:
                aflag = 0
            if pressed[100] == 1:
                dflag = 1
                print("D")
            if pressed[100] == 0:
                dflag = 0
            if pressed[32] == 1 and shootstopper == 0:
                shootflag = 1
                #print("SHOOT")
            if pressed[32] == 0:
                shootflag = 0
        elif event.type == pygame.KEYUP:
            pressed = pygame.key.get_pressed()
            if pressed[119] == 1:
                wflag = 1
                print("W")
            if pressed[119] == 0:
                wflag = 0
            if pressed[115] == 1:
                sflag = 1
                print("S")
            if pressed[115] == 0:
                sflag = 0
            if pressed[97] == 1:
                aflag = 1
                print("A")
            if pressed[97] == 0:
                aflag = 0
            if pressed[100] == 1:
                dflag = 1
                print("D")
            if pressed[100] == 0:
                dflag = 0
            if pressed[32] == 1:
                shootflag = 1
                #print("SHOOT")
                shootstopper = 0
            if pressed[32] == 0:
                shootflag = 0
                shootstopper = 0
            #print("release")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
    # # --- Game logic should go hereLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGICLOGIC

    ##############################################SPAWN/DEATH########################################################
    #Enemy Purge

    enemy_list = enemy_purge(enemy_list, player)


    #Enemy Spawn
    if enemy_spawn_count > 19 and len(enemy_list) < player.level + 25   :
        enemy_list = enemy_spawn(enemy_list)
        enemy_spawn_count = 0
        #print ("E spawned")
    else:
        if enemy_spawn_count < 20:
            enemy_spawn_count += 1
        #print ("e spawn in" + str(80 - enemy_spawn_count))

    #################################################################################################################

    ##############################################BULLETS############################################################

    for shipnum, enemyship in enumerate(enemy_list):
        if enemyship.shoot_countdown == 0:
            bullet_spawn(bullet_list, enemyship)
            enemyship.shoot_countdown = enemyship.shoot_countdown_static
        else:
            enemyship.shoot_countdown -= 1

    if shootflag == 1 and shootstopper != 1:
        bullet_list = bullet_spawn(bullet_list, player)

    #Move the Bullets
    bullet_list = bullet_move(bullet_list)
    #Purge Offscreen bullets or those that collide (bump)
    bullet_list = bullet_purge(bullet_list)
    #################################################################################################################

    ##############################################PLAYER MOVE########################################################
    if wflag == 1:
        player.y = moveup(player.y)
    if sflag == 1:
        player.y = movedown(player.y)
    if aflag == 1:
        player.x = moveleft(player.x)
    if dflag == 1:
        player.x = moveright(player.x)
    #################################################################################################################

    ##############################################ENEMY MOVE#########################################################
    enemy_list = enemy_move(enemy_list)
    #################################################################################################################

    ##############################################COLLISION##########################################################
    collision_flash_flag =  collide(bullet_list, enemy_list, player, collision_flash_flag)
    #################################################################################################################












    # --- Drawing code should go hereDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAWDRAW

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    if collision_flash_flag == 1:
        print ("flash")
        flash(windowx, windowy)
        collision_flash_flag = 0
    if shootflag == 1 and shootstopper != 1:
        shootstopper = shoot(player.x, player.y, player.radius)

    update_bullets(bullet_list)
    update_enemy(enemy_list)
    update_circle(player.x, player.y, player.radius, player.level)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
pygame.quit()
