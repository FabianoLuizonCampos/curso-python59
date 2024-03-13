import pygame
import random


class Shot(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        # Carregando a imagem para uso
        self.image = pygame.image.load("data/shot.png")
        # Redimensionando a imagem para o retangulo em 100%
        self.image = pygame.transform.scale(self.image, [50, 50])
        # Ajustando a posição do morcego
        # self.image = pygame.transform.flip()
        # Ajustando no retangulo
        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(50, 50, 10, 10)

        self.speed = 4

    def update(self, *args):
        
        self.rect.x += self.speed

        if self.rect.right > 840:
            self.kill()
