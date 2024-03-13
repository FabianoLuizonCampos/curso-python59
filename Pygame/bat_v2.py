import pygame
import random


class Bat(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        
        # Carregando todos os quadros do GIF
        self.gif_frames = []
        gif_path = "data/bat-x4.gif"
        gif = pygame.image.load(gif_path)
        frame_width = gif.get_width() // 3  # Divida a largura total pelo número de quadros
        frame_height = gif.get_height()
        for i in range(4):  # Supondo que há 4 quadros no GIF
            frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)
            frame.blit(gif, (0, 0), (i * frame_width, 0, frame_width, frame_height))
            self.gif_frames.append(frame)

        # Redimensionando a imagem para o retângulo em 100%
        self.image = pygame.transform.scale(self.gif_frames[0], [100, 100])
        
        # Ajustando a posição do morcego
        self.rect = pygame.Rect(50, 50, 100, 100)
        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(2, 400)
        
        self.speed = 1 + random.random() * 2

        # Inicialize o contador de quadros e o temporizador
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_delay = 100  # Tempo de atraso entre os quadros em milissegundos

    def update(self, *args):

        # Atualize o temporizador
        self.frame_timer += args[0].elapsed

        # Se o tempo de atraso para o próximo quadro passou
        if self.frame_timer >= self.frame_delay:
            # Avance para o próximo quadro
            self.frame_index = (self.frame_index + 1) % len(self.gif_frames)
            self.image = pygame.transform.scale(self.gif_frames[self.frame_index], [100, 100])
            # Reinicie o temporizador
            self.frame_timer = 0

        # Movimento horizontal do morcego
        self.rect.x -= self.speed

        # Se o morcego sair da tela, remova-o do grupo de sprites
        if self.rect.right < 0:
            self.kill()
