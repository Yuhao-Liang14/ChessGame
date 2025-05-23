import os
import sys
import pygame
import algorithm

pygame.init()
al = algorithm.Algorithm()
x = [478, 550, 623, 695, 767, 840, 912, 984, 1056]
y = [77, 149, 222, 294, 366, 452, 524, 597, 669, 741]
xy = {}
for i in range(len(y)):
    for j in range(len(x)):
        xy[str(j)+','+str(i)] = [x[j], y[i]]

screen_width = 1536
screen_height = 793
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("中国象棋1.0")
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
project_dir = os.path.join(project_dir, 'images\\')
ChessBoard = pygame.image.load(project_dir + "象棋棋盘.jpg")
redRook = pygame.image.load(project_dir + "红車.png")
redKnight = pygame.image.load(project_dir + "红馬.png")
redCannon = pygame.image.load(project_dir + "红炮.png")
redGuard = pygame.image.load(project_dir + "红士.png")
redElephant = pygame.image.load(project_dir + "相.png")
redGeneral = pygame.image.load(project_dir + "帥.png")
redPawn = pygame.image.load(project_dir + "兵.png")
blackRook = pygame.image.load(project_dir + "黑車.png")
blackKnight = pygame.image.load(project_dir + "黑馬.png")
blackCannon = pygame.image.load(project_dir + "黑炮.png")
blackGuard = pygame.image.load(project_dir + "黑士.png")
blackElephant = pygame.image.load(project_dir + "象.png")
blackGeneral = pygame.image.load(project_dir + "将.png")
blackPawn = pygame.image.load(project_dir + "卒.png")
lookup = {
    1: redRook,
    2: redKnight,
    3: redElephant,
    4: redGuard,
    5: redGeneral,
    6: redCannon,
    7: redPawn,
    -1: blackRook,
    -2: blackKnight,
    -3: blackElephant,
    -4: blackGuard,
    -5: blackGeneral,
    -6: blackCannon,
    -7: blackPawn
}


def draw(selected=''):
    screen.fill((255, 255, 255))
    screen.blit(ChessBoard, (395, 0))
    for k in range(10):
        for g in range(9):
            if int(al.chessboard[k, g]) != 0:
                a = xy[str(g)+','+str(k)]
                screen.blit(lookup[int(al.chessboard[k, g])], (a[0]-32, a[1]-32))
    if selected:
        if al.chessboard[int(selected.split(',')[1]), int(selected.split(',')[0])] != 0:
            screen.blit(pygame.transform.scale(lookup[int(al.chessboard[int(selected.split(',')[1]), int(selected.split(',')[0])])], (74, 74)), tuple([w - 37 for w in xy[selected]]))


def chosen(x1, y1):
    global x, y
    a, b, e, f = 100, 100, 0, 0
    for c in x:
        if abs(c - x1) < a:
            a = abs(c - x1)
            e = c
    for d in y:
        if abs(d - y1) < b:
            b = abs(d - y1)
            f = d
    for key, value in xy.items():
        if value == [e, f]:
            return key


def choose(x1, y1, x2, y2):
    where = al.chessboard[y1, x1]
    if abs(where) == 1:
        return al.rook(x1, y1, x2, y2)
    elif abs(where) == 2:
        return al.knight(x1, y1, x2, y2)
    elif abs(where) == 3:
        return al.elephant(x1, y1, x2, y2)
    elif abs(where) == 4:
        return al.guard(x1, y1, x2, y2)
    elif abs(where) == 5:
        return al.general(x1, y1, x2, y2)
    elif abs(where) == 6:
        return al.cannon(x1, y1, x2, y2)
    elif abs(where) == 7:
        return al.pawn(x1, y1, x2, y2)
    else:
        return

selected = ''
num = 0
num1 = []
num2 = 1
while True:
    draw(selected)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = event.pos
            if 395 < click_x < 1140:
                selected = chosen(click_x, click_y)
                num += 1
                num1 += [selected.split(',')]
                if num2 % 2 == 1 and num == 1:
                    if not al.chessboard[int(num1[0][1]), int(num1[0][0])] > 0:
                        num1 = []
                        num = 0
                        selected = ''
                elif num2 % 2 == 0 and num == 1:
                    if not al.chessboard[int(num1[0][1]), int(num1[0][0])] < 0:
                        num1 = []
                        num = 0
                        selected = ''
            else:
                selected = ''
                num1 = []
                num = 0
            if num == 2:
                num = 0
                for q in range(2):
                    for p in range(2):
                        num1[q][p] = int(num1[q][p])
                if choose(num1[0][0], num1[0][1], num1[1][0], num1[1][1]):
                    al.chessboard[num1[1][1], num1[1][0]] = al.chessboard[num1[0][1], num1[0][0]]
                    al.chessboard[num1[0][1], num1[0][0]] = 0
                    num2 += 1
                    selected = ''
                    num1 = []
                    red_wins = True
                    for i in range(3, 6):
                        for j in range(3):
                            if al.chessboard[j, i] == -5:
                                red_wins = False
                                break
                        if not red_wins:
                            break
                    if red_wins:
                        for i in range(3, 6):
                            for j in range(7, 10):
                                if al.chessboard[j, i] == -5:
                                    red_wins = False
                                    break
                            if not red_wins:
                                break

                    if red_wins:
                        print('红胜')
                        pygame.quit()
                        sys.exit()

                    black_wins = True
                    for i in range(3, 6):
                        for j in range(3):
                            if al.chessboard[j, i] == 5:
                                black_wins = False
                                break
                        if not black_wins:
                            break
                    if black_wins:
                        for i in range(3, 6):
                            for j in range(7, 10):
                                if al.chessboard[j, i] == 5:
                                    black_wins = False
                                    break
                            if not black_wins:
                                break

                    if black_wins:
                        print('黑胜')
                        pygame.quit()
                        sys.exit()
                else:
                    selected = ''
                    num1 = []

    pygame.display.flip()

