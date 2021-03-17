import pygame
from pygame.locals import *
import random

pygame.init()

sure = 30
skor = 0

pygame.display.set_caption("Hit da Button")
icon = pygame.image.load("assets/ico/ico.png")
pygame.display.set_icon(icon)       
        
font = pygame.font.Font('freesansbold.ttf', 24)
baslat = pygame.Rect(400, 300, 50, 25)

def baslangic():
    baslangic_ekran = pygame.display.set_mode( (800,600) )
    
    baslat_buton = pygame.Rect(310, 235, 175, 50)
    credits_buton = pygame.Rect(310, 305, 175, 50)
    cikis_buton = pygame.Rect(310, 375, 175, 50)
    
    baslat_yazi = font.render('Start', True, (255, 255, 255))
    credits_yazi = font.render('Credits', True, (255, 255, 255))
    quit_yazi = font.render('Quit', True, (255, 255, 255))
    
    background = pygame.image.load("assets/etc/bg_w_name.png")
    while True:
        baslangic_ekran.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        tiklandi = False

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    tiklandi = True
    
            if event.type == pygame.QUIT:
                pygame.quit()
         
        if tiklandi:
            if baslat_buton.collidepoint( (mx, my) ):
                oyun()
            elif credits_buton.collidepoint( (mx, my) ):
                about_and_credits()
            elif cikis_buton.collidepoint( (mx, my) ):
                pygame.quit()
                print("Quitted!")
         
        baslangic_ekran.blit(background, ((0, 0)))
        pygame.draw.rect(baslangic_ekran, (0, 255, 0), baslat_buton)
        pygame.draw.rect(baslangic_ekran, (192, 192, 192), credits_buton)
        pygame.draw.rect(baslangic_ekran, (192, 192, 192), cikis_buton)
        baslangic_ekran.blit(baslat_yazi, ((365, 250)))
        baslangic_ekran.blit(credits_yazi, ((345, 320)))
        baslangic_ekran.blit(quit_yazi, ((365, 390)))
        pygame.display.update()

def about_and_credits(): # This part is only a picture.
    running = True
    background = pygame.image.load("assets/etc/credits.png")
    credit_ekran = pygame.display.set_mode( (800,600) )
    while running:
        tiklandi = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    baslangic()           
    
            if event.type == pygame.QUIT:
                running = False
                print("Game Closed.")
            
        credit_ekran.blit(background, (0, 0))
        pygame.display.update()
        
def oyun():
    oyun_ekran = pygame.display.set_mode( (800,600) )
    enemy_button = pygame.Rect(random.randint(10, 500), random.randint(10, 500), 50, 25)
    killer_button = pygame.Rect(random.randint(10, 500), random.randint(10, 500), 50, 25)
    score = 0
    click_num = 7
    win_score = 25
    
    background = pygame.image.load("assets/etc/bg.png")
    running = True
    while running:
        tiklandi = False
        oyun_ekran.fill((0, 0, 0))
        scoreText = font.render(f'Score: {score}', True, (255, 255, 255))
        toWin = font.render(f'To Win: {win_score - score}', True, (255, 255, 255))
        toLose = font.render(f'To Lose: {click_num}', True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    tiklandi = True
    
            if event.type == pygame.QUIT:
                running = False
        
        mx, my = pygame.mouse.get_pos()
        
        if tiklandi:
            if enemy_button.collidepoint( (mx, my) ):
                tiklandi = False
                score += 1
                enemy_button = pygame.Rect(random.randint(10, 500), random.randint(10, 500), 50, 25)
            else:
                click_num -= 1
                if click_num == 0:
                    the_end()
        
        if score > win_score:
            print("Score!!")
            the_end()
        
        oyun_ekran.blit(background, (0, 0))
        pygame.draw.rect(oyun_ekran, (10, 255, 10), enemy_button)
        oyun_ekran.blit(scoreText, (350, 10))
        oyun_ekran.blit(toWin, (350, 45))
        oyun_ekran.blit(toLose, (350, 80))
        pygame.display.update()
        

def the_end(): # This part is also only a picture.
    end_screen = pygame.display.set_mode( (800, 600) )
    background = pygame.image.load("assets/etc/the_end.png")
    
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    baslangic()     
                
        end_screen.blit(background, (0, 0))
        pygame.display.update()

baslangic()
