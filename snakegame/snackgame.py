
import pygame 
import random
from pygame.locals import *
import os
pygame.mixer.init()

def home_screen():
    pygame.init()           # pygame initialization
    pygame.font.init()      # pygame font initialization    
    screen=pygame.display.set_mode((700,500))     # set the size of the home screen/window
    pygame.display.set_caption("Snacke Game By Ayushi>>>")   # set the title of the home screen/window
    x = 150
    y = 150
    text_color=(0,225,0)
    spf = 60     # frame rat eof game
    clock = pygame.time.Clock()   # clock object to control the frame rate of the game
    running = True     # variable to control the game loop
    img=pygame.image.load(r'C:\pytho\miniprojects\snakegame\snake (2).png').convert()
    start=pygame.mixer.Sound(r'C:\pytho\miniprojects\snakegame\sounds\spiderman-meme-song.mp3')
    start.play(-1)
    while running:    
        screen.fill((0,0,0))     # fill the screen with black color
        screen.blit(img,(x+140,y-80))   # blit the image on the screen at the specified position
        board(screen,"___Welcome to Snake Game___",x-50,y+50,text_color)  
        board(screen,"Press Space to start >>>",x,y+100,text_color)
        board(screen,"Press Esc to quit XXX",x,y+150,text_color)
        for event in pygame.event.get():
            if event.type == QUIT:  # if the user closes the window
                running = False
            elif event.type == KEYDOWN: # if the user presses a key
                if event.key == K_ESCAPE: # if the user presses the escape key
                    running=False
                elif event.key == K_SPACE:  # if the user presses the space key
                    game_over = False  # set the game_over variable to False
                    snake_list = [] # initialize the snake list
                    snake_length = 1    
                    score = 0
                    start.stop()
                    snake_main(game_over,snake_list,snake_length,score)  # call the game function       
        pygame.display.update()         # update the display
    clock.tick(spf)  # control the frame rate of the game


def snake_main(game_over,snake_list,snake_length,score):
    pygame.init()         
    pygame.font.init()
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Snacke Game By Ayushi>>>")
    
    block_x = 0
    block_y = 0
    x=2
    y=2
    bg=pygame.image.load(r'C:\pytho\miniprojects\snakegame\bg.jpg').convert_alpha()
    block_size = 15
    snake_color = (10, 15, 10)
    food_x = random.randint(0,700-block_size)     # generate a random number between 0 and 500-block_size (width)
    food_y = random.randint(0,500-block_size)     # generate a random number between 0 and 500-block_size (height)
    inti_speed = 12
    screen.fill((12, 6, 160))
    screen.blit(bg,(0,0))
    text_color=(225,0,0)
    clock = pygame.time.Clock()
    if not os.path.exists(r'C:\pytho\miniprojects\snakegame\highscore.txt'): # check if the high score file exists
                    with open(r'C:\pytho\miniprojects\snakegame\highscore.txt','w') as f:
                        f.write("0")
    with open(r'C:\pytho\miniprojects\snakegame\highscore.txt','r') as f:  # open the high score file in read mode
        high_score = int(f.read())
    # screen.blit(block1,(block_x,block_y))
    pygame.draw.rect(screen,snake_color,(block_x,block_y,block_size,block_size))    # draw a rectangle on the screen at the specified position
    pygame.draw.rect(screen,(209, 23, 26),(food_x,food_y,block_size,block_size))
    pygame.display.flip()
    
    bgmusic=pygame.mixer.Sound(r'C:\pytho\miniprojects\snakegame\Run-Amok(chosic.com).mp3')
    running=True
    bgmusic.set_volume(0.20)    # set the volume of the background music
    bgmusic.play(-1)  # play the background music in a loop
    while running:  
        for event in pygame.event.get():
            if game_over==True:
                with open (r'C:\pytho\miniprojects\snakegame\highscore.txt','w') as f:   # open the high score file in write mode
                    f.write(str(high_score))   # write the high score to the file
                screen.fill((0,0,0))
                board(screen,f" Game Over ! ",270,200,text_color)
                board(screen,f" Press Enter to Restart ",200,250,text_color)
                pygame.display.update()
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        home_screen()
                        
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
                    
                elif event.key == K_UP:
                    block_y -= inti_speed   # move the block up by inti_speed units
                    score, snake_length,high_score, game_over,food_x,food_y=draw_block(game_over,bg,screen,block_x,block_y,x,y,block_size,food_x,food_y,snake_length,snake_list,snake_color,clock,score,high_score,bgmusic)    # draw the block on the screen
                    
                elif event.key == K_DOWN:
                    block_y += inti_speed    # move the block down by inti_speed units
                    score, snake_length,high_score, game_over,food_x,food_y=draw_block(game_over,bg,screen,block_x,block_y,x,y,block_size,food_x,food_y,snake_length,snake_list,snake_color,clock,score,high_score,bgmusic)    # draw the block on the screen
                    
                elif event.key == K_LEFT:
                    block_x -= inti_speed   # move the block left by inti_speed units
                    score, snake_length,high_score, game_over,food_x,food_y=draw_block(game_over,bg,screen,block_x,block_y,x,y,block_size,food_x,food_y,snake_length,snake_list,snake_color,clock,score,high_score,bgmusic)    # draw the block on the screen
                    
                elif event.key == K_RIGHT:
                    block_x += inti_speed   # move the block right by inti_speed units
                    score, snake_length,high_score, game_over,food_x,food_y=draw_block(game_over,bg,screen,block_x,block_y,x,y,block_size,food_x,food_y,snake_length,snake_list,snake_color,clock,score,high_score,bgmusic)    # draw the block on the screen
                    
                elif event.key == K_a:  # when you press the 'a' key, score incresed by 3                    
                    score+=3            # cheating mode

            elif event.type == QUIT:
                running = False
                
                
def board(screen,s,x,y,color):
    font=pygame.font.SysFont('Arial',40)    # create a font object
    text=font.render(s,True,color)      # render the text on the screen
    screen.blit(text,(x,y))                 # draw the text on the screen


def plot_snake(window,snake_color,snake_list,snake_size):
    for x,y in snake_list:  # for each point in the snake list
        pygame.draw.rect(window,snake_color,[x,y,snake_size,snake_size]) # draw a rectangle at that point


def draw_block(game_over,bg,screen,block_x,block_y,x,y,block_size,food_x,food_y,snake_length,snake_list,snake_color,clock,score,high_score,bgmusic):
    achivement=pygame.mixer.Sound(r'C:\pytho\miniprojects\snakegame\sounds\anime-wow-sound-effect.mp3')
    game_over_sound=pygame.mixer.Sound(r'C:\pytho\miniprojects\snakegame\sounds\baby-laughing-meme.mp3')
    eating=pygame.mixer.Sound(r'C:\pytho\miniprojects\snakegame\sounds\achievement-video-game-type-1-230515.mp3')
    text_color=(0,0,225)
    screen.fill((12, 6, 160))
    screen.blit(bg,(0,0))
    board(screen,f" Score : {score}                                   Highscore : {high_score}",x,y,text_color)
    pygame.draw.rect(screen,(209, 23, 26),(food_x,food_y,block_size,block_size))
    if abs(block_x-food_x)<7 and abs(block_y-food_y)<7: # if the snake eats the food 
        score+=10    # increase the score by 10
        eating.set_volume(0.50)
        eating.play()
        food_x=random.randint(0,700-block_size) # reset food's random potition
        food_y=random.randint(0,500-block_size)
        snake_length+=2 # increase the snake's length by 2 units
        if score > high_score:  # if the current score is higher than the high score
            high_score = score
            achivement.set_volume(0.50)
            achivement.play()  # play the achievement sound
    head=[]
    head_x=block_x
    head_y=block_y
    head.append(head_x)
    head.append(head_y)
    if head in snake_list[:-1]: # if the snake eats itself
        game_over = True
        bgmusic.stop()
        game_over_sound.set_volume(0.50)
        game_over_sound.play()  # play the game over sound
    snake_list.append(head)
    if len(snake_list)>snake_length: # if the snake's length(list) is greater than the snake_length
        del snake_list[0]
    if block_x<0 or block_x>=700 or block_y<0 or block_y>=500:  # if the snake goes out of the screen
        game_over = True
        bgmusic.stop()
        game_over_sound.set_volume(0.50)
        game_over_sound.play()    # play the game over sound
    plot_snake(screen,snake_color,snake_list,block_size)    #  draw the snake on the screen
    pygame.display.update()
    clock.tick(60)
    return score, snake_length,high_score, game_over,food_x,food_y


home_screen()  # stating the game              