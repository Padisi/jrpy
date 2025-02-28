import numpy as np
import pygame

def movement(player):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.forces += np.array([1.0, 0.0])

    if keys[pygame.K_LEFT]:
        player.forces += np.array([-1.0, 0.0])

    if keys[pygame.K_UP]:
        player.forces += np.array([0.0, -1.0])

    if keys[pygame.K_DOWN]:
        player.forces += np.array([0.0, 1.0])

    if keys[pygame.K_SPACE]:
        if np.linalg.norm(player.forces)<2:
            player.forces += -player.forces
        player.forces = player.forces*0.99
