import pygame
import os
import sys

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player = None
FPS = 50

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')
tile_width = tile_height = 50


def generate_level(level):
    new_player, x, y = None, None, None
    x1 = y1 = 0, 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                x1 = x
                y1 = y
    new_player = Player(x1, y1)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('pr1.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                terminate()
            elif ev.type == pygame.KEYDOWN or \
                    ev.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
try:
    player, level_x, level_y = generate_level(load_level('{}'.format(
        ['lvl1.txt', 'lvl2.txt', 'lvl3.txt', 'lvl4.txt'][int(input('Введите номер файда(просто цифра) из списка:'
                                                                   '\n1)Первый базовый уровень из материалов урока\n'
                                                                   '2)Квадратный уровень\n3)сердечко\n4)лицо\n'))-1])))

except Exception:
    print('Извините, ничего не работает. До свидания.')
    quit()

print('Идите в приложение.')

step = 3
step_flag1 = False
step_flag2 = False
step_flag3 = False
step_flag4 = False
screen.fill((0, 0, 0))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                step_flag1 = True
            if event.key == pygame.K_RIGHT:
                step_flag2 = True
            if event.key == pygame.K_UP:
                step_flag3 = True
            if event.key == pygame.K_DOWN:
                step_flag4 = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                step_flag1 = False
            if event.key == pygame.K_RIGHT:
                step_flag2 = False
            if event.key == pygame.K_UP:
                step_flag3 = False
            if event.key == pygame.K_DOWN:
                step_flag4 = False

    if step_flag1:
        player.rect.x -= step
    if step_flag2:
        player.rect.x += step
    if step_flag3:
        player.rect.y -= step
    if step_flag4:
        player.rect.y += step

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.flip()
