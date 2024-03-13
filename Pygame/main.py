import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

########

import random
import pygame
from ghost import Ghost
from bat import Bat
from shoot import Shot

# ---------------------- INICIALIZAÇÃO - INICIO ------------------------------
#inicializando o pygame
pygame.init()

#iniciando a janela com a configuraçao ou resolução de 840x480
#cria um canvas, uma tela em branco para pintar
display = pygame.display.set_mode([840,480])

#mudando o titulo da minha janela
pygame.display.set_caption("SENAI Python")

#criando um grupo de imagem para carregar todas as imagem e desenhar de uma unica vez
objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()


#Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()


#criando o objeto Sprite para carregar a imagem
ghost = Ghost(objectGroup)

# MUSIC
pygame.mixer.music.load("data/alienblues.wav")
pygame.mixer.music.play(-1)

#SOUND
magic = pygame.mixer.Sound("data/magic1.wav")

# TEXT
score_font = pygame.font.Font("font/Pixeltype.ttf", 50)
# score_render = score_font.render('Score: ', False, 'Black') 
# score = score_render.get_rect(center = (420, 50))

# texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
# tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

#Variavel Global para controlar o loop
gameLoop = True
gameOver = False
timer = 20
pontos = 0

#Criando um clock para ajustar os frames por segundo
clock = pygame.time.Clock()

# ---------------------- INICIALIZAÇÃO - FIM --------------------------------

def draw():
    global timer
    global gameLoop
    global gameOver
    global pontos
    #alterando a cor de fundo da janela, utilizar o color picker para escolher a cor
    display.fill([46, 46, 46])

    #Atualiza os objetos em tela
    if not gameOver:
        objectGroup.update()

        #Random dos asteroides
        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.3:
                newBat = Bat(objectGroup, batGroup)

        #Colisao
        collisions = pygame.sprite.spritecollide(ghost, batGroup, False, pygame.sprite.collide_mask)

        if collisions:
            print("GAME OVER!!!")
            gameOver = True
            
        hits = pygame.sprite.groupcollide(shotGroup, batGroup, True, True, pygame.sprite.collide_mask)
        if hits:
            pontos += 1

    

    #Desenhando o grupo de imagem
    objectGroup.draw(display)

    # Inserindo a Pontuação
    score_render = score_font.render(f'Score: {pontos}', False, 'White') 
    display.blit(score_render, (650, 50))

    

    #atualiza a tela 
    pygame.display.update()


def main():
    global gameLoop
    global timer
    global gameOver
    #criar o game loop
    while gameLoop:
        # ajustando em 60fps
        clock.tick(60)
        #verificação de todos os eventos possíveis 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameOver:
                    magic.play()
                    newShot = Shot(objectGroup, shotGroup)                    
                    newShot.rect.center = ghost.rect.center
                    
                      
                        
        draw()
        

if __name__ == "__main__":
    main()