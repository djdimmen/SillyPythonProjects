import pygame
from random import randint, choice

WIDTH = 800
HEIGHT = 400
TEXT_COLOR = (64, 64, 64)
BOX_COLOR = '#c0e8ec'

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Player Walk objects
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0

        # Player Jump objects
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index +=0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.jump_sound.play()
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 0.8
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        if self.type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = randint(170, 210)
            self.animation_speed = 0.3
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 310
            self.animation_speed = 0.1
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(WIDTH+100, WIDTH+300), y_pos))

    def animation_state(self):
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def obstacle_speed(self):
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        speedup = elapsed_time // 10
        if self.type == 'fly':
            self.rect.x -= 5 + (speedup * 1.2)
        else:
            self.rect.x -= 4 + speedup

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.obstacle_speed()
        self.destroy()

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surf = score_font.render(f'Score: {current_time}', False, TEXT_COLOR)
    score_rect = score_surf.get_rect(center=(WIDTH/2, HEIGHT/8))
    screen.blit(score_surf, score_rect)
    return current_time

def display_instructions():
    inst_surf = score_font.render('Press Space to jump', False, TEXT_COLOR)
    inst_rect = inst_surf.get_rect(midtop=(WIDTH/2, HEIGHT/8+25))
    screen.blit(inst_surf, inst_rect)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snail Jump")
clock = pygame.time.Clock()
score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
start_time = 0
score = 0
running = True
game_active = False
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.3)

# Player Group
player = pygame.sprite.GroupSingle()
player.add(Player())

# Obstacle Group
obstacle_group = pygame.sprite.Group()

# Create static surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,randint(-20,20),2)
player_stand_rect = player_stand.get_rect(center=(WIDTH/2, (HEIGHT/2) + 50))

game_name = score_font.render('Snail Jump', False, TEXT_COLOR)
game_name_rect = game_name.get_rect(center=(WIDTH/2, HEIGHT/7))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while running:
    # Poll for events
    # pygame.QUIT event means the user clicked X to close your window
    bg_music.play(loops=-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = pygame.time.get_ticks()
                game_active = True

    if game_active:
        # Draw the background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()
        display_instructions()

        # Draw and update the player
        player.draw(screen)
        player.update()

        # Draw and update the obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()
    else:
        # Fill Screem
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        
        # Print Score
        score_message = score_font.render(f'Score: {score}', False, TEXT_COLOR)
        score_message_rect = score_message.get_rect(center=(WIDTH/2, HEIGHT/8))
        
        # Print Game Over
        g_o_message = score_font.render('Game Over!', False, TEXT_COLOR)
        g_o_message_pos = (WIDTH/2, score_message_rect.y + 60)
        g_o_message_rect = g_o_message.get_rect(midtop=g_o_message_pos)

        # Print "Space to Restart"
        restart_message = score_font.render("Press 'Space' to start again", False, TEXT_COLOR)
        restart_message_pos = (WIDTH/2, g_o_message_rect.y + 60)
        restart_message_rect = restart_message.get_rect(midtop=restart_message_pos)

        # Print "Space to Start"
        start_message = score_font.render("Press 'Space' to start", False, TEXT_COLOR)
        start_message_pos = (WIDTH/2, HEIGHT/3)
        start_message_rect = start_message.get_rect(midtop=start_message_pos)

        if score != 0:
            screen.blit(score_message, score_message_rect)
            screen.blit(g_o_message, g_o_message_rect)
            screen.blit(restart_message, restart_message_rect)
        else:
            screen.blit(game_name, game_name_rect)
            screen.blit(start_message, start_message_rect)


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics
    # flip() the display to put your work on screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()