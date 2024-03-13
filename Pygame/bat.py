import pygame
import random


class Bat(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        # Carregando a imagem para uso
        self.image = pygame.image.load("data/bat-x4.gif")
        # Redimensionando a imagem para o retangulo em 100%
        self.image = pygame.transform.scale(self.image, [100, 100])
        # Ajustando a posição do morcego
        # self.image = pygame.transform.flip()
        # Ajustando no retangulo
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(2, 400)
        
        self.speed = 1 + random.random() * 2

    def update(self, *args):

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
