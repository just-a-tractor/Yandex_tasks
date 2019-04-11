import pygame
import random


class Minesweeper:
    def __init__(self, w, h, m_count):
        self.width = w
        self.height = h
        self.count = m_count
        self.board = [[0] * h for _ in range(w)]

        self.left = 10
        self.top = 10
        self.cell_size = 50
        color1 = pygame.Color('black')
        color2 = pygame.Color('red')
        self.colors = [color1, color2]

    def check_cell(self, x, y):
            if self.board[x][y] != '1':

                kx1 = 0 if x == 0 else 1
                kx2 = 1 if x == self.width-1 else 2
                ky1 = 0 if y == 0 else 1
                ky2 = 1 if y == self.height-1 else 2

                count = 0

                for i in range(x - kx1, x + kx2):
                    for j in range(y - ky1, y + ky2):
                        if i == x and j == y:
                            continue
                        elif self.board[i][j] == '1':
                            count += 1

                self.board[x][y] = count

    def check_cell2(self, x, y):

        kx1 = 0 if x == 0 else 1
        kx2 = 1 if x == self.width - 1 else 2
        ky1 = 0 if y == 0 else 1
        ky2 = 1 if y == self.height - 1 else 2

        f = x * self.cell_size + self.left
        s = y * self.cell_size + self.top
        font1 = pygame.font.Font(None, 50)
        string_rendered1 = font1.render(str(self.board[x][y]), 1, (200, 255, 200))
        intro_rect1 = string_rendered1.get_rect()
        intro_rect1.y = s
        intro_rect1.x = f
        screen.blit(string_rendered1, intro_rect1)

        if self.board[x][y] == 0:
            self.board[x][y] = '0'
            for i in range(x - kx1, x + kx2):
                for j in range(y - ky1, y + ky2):
                    if (i == x and j == y) or self.board[i][j] == '0':
                        continue
                    self.check_cell2(i, j)

    def start(self):
        for i in range(self.count):
            a = random.randint(0, self.width-1)
            b = random.randint(0, self.height-1)
            self.board[a][b] = '1'
        screen.fill((0, 0, 0))
        for i in range(self.width):
            for j in range(self.height):
                left_lim = i * self.cell_size + self.left
                top_lim = j * self.cell_size + self.top
                cs = [(left_lim, top_lim), (self.cell_size, self.cell_size)]
                pygame.draw.rect(screen, self.colors[int(self.board[i][j])], cs, 0)
                pygame.draw.rect(screen, (255, 255, 255), cs, 1)
                self.check_cell(i, j)

    def get_cell(self, cords):
        cell_x = (cords[0] - self.left) // self.cell_size
        cell_y = (cords[1] - self.top) // self.cell_size
        if (0 > cell_x or cell_x >= self.width or
                0 > cell_y or cell_y >= self.height):
            return None, None
        else:
            return cell_x, cell_y

    def open_cell(self, pos):
        x, y = self.get_cell(pos)
        if (x is not None and y is not None) and type(self.board[x][y]) != str:
            self.check_cell2(x, y)
            f = x * self.cell_size + self.left
            s = y * self.cell_size + self.top
            font1 = pygame.font.Font(None, 50)
            string_rendered1 = font1.render(str(self.board[x][y]), 1, (200, 255, 200))
            intro_rect1 = string_rendered1.get_rect()
            intro_rect1.y = s
            intro_rect1.x = f
            screen.blit(string_rendered1, intro_rect1)


pygame.init()
size = width, height = 520, 770
screen = pygame.display.set_mode(size)
running = True
board = Minesweeper(10, 15, 10)
board.start()
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button != 4 and event.button != 5:
            board.open_cell(event.pos)
    pygame.display.flip()

pygame.quit()
