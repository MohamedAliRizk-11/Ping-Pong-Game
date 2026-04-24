# -*- coding: utf-8 -*-
"""
created on fri apr 24 03:47:16 2026
@author: mohamed ali
"""

import pygame
import sys
import random
import os
from collections import deque

pygame.init()

# screen 
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ping pong ")
clock = pygame.time.Clock()

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

base_dir = os.path.dirname(__file__)

# images
fire_img = pygame.image.load(os.path.join(base_dir,"fire.png")).convert_alpha()
ice_img = pygame.image.load(os.path.join(base_dir,"snow.png")).convert_alpha()
scissors_img = pygame.image.load(os.path.join(base_dir,"cut.png")).convert_alpha()

fire_img = pygame.transform.scale(fire_img,(30,30))
ice_img = pygame.transform.scale(ice_img,(30,30))
scissors_img = pygame.transform.scale(scissors_img,(30,30))

icon_size = (18,18)
fire_icon = pygame.transform.scale(fire_img,icon_size)
ice_icon = pygame.transform.scale(ice_img,icon_size)
scissors_icon = pygame.transform.scale(scissors_img,icon_size)

# players
player_default_h = 80
ai_default_h = 80

player = pygame.Rect(20,height//2 - 40,10,player_default_h)
ai = pygame.Rect(width - 30,height//2 - 40,10,ai_default_h)

ball = pygame.Rect(width//2,height//2,12,12)

base_speed = 6
speed_x = base_speed * random.choice([-1,1])
speed_y = base_speed * random.choice([-1,1])

# score
player_score = 0
ai_score = 0
font = pygame.font.SysFont(None,50)

# items 

def spawn_item():
    return pygame.Rect(
        random.randint(60,width-60),
        random.randint(60,height-60),
        30,30
    )

fire = spawn_item()
ice = spawn_item()
scissors = spawn_item()

# states
ball_fire = False

player_frozen = False
ai_frozen = False
freeze_p = 0
freeze_ai = 0

player_cut = False
ai_cut = False

# speed boost
def boost_speed():
    global speed_x,speed_y
    speed_x *= 1.3
    speed_y *= 1.3

#  BFS Algorithm
def bfs_ai(ai_rect,ball_rect):

    queue = deque()
    visited = set()

    start = ai_rect.centery
    target = ball_rect.centery

    queue.append((start,0))
    visited.add(start)

    while queue:
        pos,depth = queue.popleft()

        if abs(pos-target) < 8:
            return pos

        if depth > 8:
            continue

        for move in [-6,0,6]:
            new_pos = pos + move

            if 0 <= new_pos <= height and new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos,depth+1))

    return start

# draw ui 
def draw_list(x,y,effects):

    box = pygame.Surface((140,30),pygame.SRCALPHA)
    box.fill((70,70,70,120))
    screen.blit(box,(x,y))

    xx = x + 5
    for icon in effects:
        screen.blit(icon,(xx,y+6))
        xx += 20


# game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    player.centery = pygame.mouse.get_pos()[1]

   
    if not ai_frozen:
        target = bfs_ai(ai,ball)

        if ai.centery < target:
            ai.y += 5
        elif ai.centery > target:
            ai.y -= 5

    ai.y = max(0,min(height - ai.height,ai.y))

    
    ball.x += speed_x
    ball.y += speed_y

    if ball.top <= 0 or ball.bottom >= height:
        speed_y *= -1

  
    if ball.colliderect(player):
        ball.left = player.right
        speed_x = abs(speed_x)
        speed_y += random.uniform(-2,2)
        if ball_fire:
            boost_speed()
        ball_fire = False

    if ball.colliderect(ai):
        ball.right = ai.left
        speed_x = -abs(speed_x)
        speed_y += random.uniform(-2,2)
        if ball_fire:
            boost_speed()
        ball_fire = False

# fire item

    if ball.colliderect(fire):
        ball_fire = True
        boost_speed()
        fire = spawn_item()

# ice item

    if ball.colliderect(ice):
        if speed_x > 0:
            ai_frozen = True
            freeze_ai = 120
        else:
            player_frozen = True
            freeze_p = 120
        ice = spawn_item()

# scissors item

    if ball.colliderect(scissors):
        if speed_x > 0:
            ai.height = player_default_h // 2
            ai_cut = True
        else:
            player.height = player_default_h // 2
            player_cut = True
        scissors = spawn_item()

   
    if freeze_p > 0:
        freeze_p -= 1
        if freeze_p == 0:
            player_frozen = False

    if freeze_ai > 0:
        freeze_ai -= 1
        if freeze_ai == 0:
            ai_frozen = False

# goals
    if ball.left <= 0:
        ai_score += 1
        ball.center = (width//2,height//2)
        speed_x = base_speed * random.choice([-1,1])
        speed_y = base_speed * random.choice([-1,1])

        player.height = player_default_h
        ai.height = ai_default_h

        player_cut = False
        ai_cut = False

    if ball.right >= width:
        player_score += 1
        ball.center = (width//2,height//2)
        speed_x = base_speed * random.choice([-1,1])
        speed_y = base_speed * random.choice([-1,1])

        player.height = player_default_h
        ai.height = ai_default_h

        player_cut = False
        ai_cut = False

 
    screen.fill((0,0,0))

    pygame.draw.rect(screen,red,player)
    pygame.draw.rect(screen,blue,ai)
    pygame.draw.ellipse(screen,white,ball)

    screen.blit(fire_img,(fire.x,fire.y))
    screen.blit(ice_img,(ice.x,ice.y))
    screen.blit(scissors_img,(scissors.x,scissors.y))

    score = font.render(f"{player_score} : {ai_score}",True,white)
    screen.blit(score,(width//2 - 40,10))

# effects ui
    player_effects = []
    ai_effects = []

    if player_frozen:
        player_effects.append(ice_icon)
    if ai_frozen:
        ai_effects.append(ice_icon)

    if player_cut:
        player_effects.append(scissors_icon)
    if ai_cut:
        ai_effects.append(scissors_icon)

    draw_list(width//2 - 230,10,player_effects)
    draw_list(width//2 + 70,10,ai_effects)

    pygame.display.flip()
    clock.tick(60)