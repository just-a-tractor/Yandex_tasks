from mymapapi import *
import pygame
from random import choice, randint


cities = ["Нью-йорк", "Москва", "Лондон", "Венеция", "Барселона"]
city = 0

pygame.init()
count = randint(0, 4)
screen = pygame.display.set_mode((450, 450))
screen.blit(pygame.image.load(get_file_map({"ll": get_coordinates(cities[city]),
                                            "l": choice(["map", "sat"])})), (0, 0))
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            city = randint(0, 4)
            screen.fill((0, 0, 0))
            screen.blit(pygame.image.load(get_file_map({"ll": get_coordinates(cities[city]),
                                                        "l": choice(["map", "sat"])})), (0, 0))

            pygame.display.flip()

pygame.quit()
