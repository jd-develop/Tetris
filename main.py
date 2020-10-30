#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Jeu de Tetris
    Dev by Jean Dubois
"""
import pygame

pygame.init()

__version__ = "alpha 0.0.1"
__author__ = "Jean Dubois <jd-develop@laposte.net>"

pygame.display.set_caption("PyTetris")
screen = pygame.display.set_mode((400, 400))  # 820, 528

running = True

while running:
    # boucle du jeu
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quitter le jeu
            running = False
            pygame.quit()
