import pygame
import time
import random
import sys
import threading

while True:
    window_x = 377
    window_y = 350
    """map = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]"""
    map = [[0 for _ in range(6)] for _ in range(7)]
    mapWinner = [[0 for _ in range(6)] for _ in range(7)]
    # print(map)
    """j = 0
    while j <= (6 - 1):
        i = 0
        while i <= (7 - 1):
            print(map[i][j], end="")  # end->kein ZeilenUmbruch
            i += 1
        j += 1
        print("")"""

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    yellow = pygame.Color(255, 255, 0)
    orange = pygame.Color(255, 125, 0)
    pink = pygame.Color(255, 0, 255)
    lila = pygame.Color(190, 0, 255)

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption("Vier gewinnt")
    game_window = pygame.display.set_mode((window_x, window_y))

    size = (window_x, window_y)
    screen = pygame.display.set_mode(size)

    def draw_table():
        xVerschiebung = 10
        pygame.draw.rect(
            game_window, green, pygame.Rect(0, 0, 10, 350)
        )  # linker balken
        pygame.draw.rect(
            game_window, green, pygame.Rect(367, 0, 10, 350)
        )  # rechter balken
        pygame.draw.rect(
            game_window, green, pygame.Rect(0, 0, 377, 10)
        )  # oberer Balken
        pygame.draw.rect(
            game_window, green, pygame.Rect(0, 310, 377, 40)
        )  # unterer balken
        while xVerschiebung < 367:
            pygame.draw.rect(game_window, green, pygame.Rect(xVerschiebung, 10, 1, 300))
            xVerschiebung += 51
        font = pygame.font.SysFont(None, 50)
        number = 1
        xVerschiebung = 25
        while number <= 7:
            img = font.render(str(number), True, black)
            screen.blit(img, (xVerschiebung, 314))
            number += 1
            xVerschiebung += 51

    def newCircle(color, column):
        farb = red
        spalte = 0
        if color == 1:
            farb = blue
        match column:
            case 1:
                spalte = 25 + 10
            case 2:
                spalte = 76 + 10
            case 3:
                spalte = 127 + 10
            case 4:
                spalte = 178 + 10
            case 5:
                spalte = 229 + 10
            case 6:
                spalte = 280 + 10
            case 7:
                spalte = 331 + 10
        fallhoehe = 33  # radius +10
        change = 10
        pygame.draw.circle(game_window, farb, ((spalte + 1), fallhoehe), 23, 0)
        s = 0
        sOr = 0
        arrayHoeheNeu = 0
        iteration = 0
        bedingung = True
        while bedingung and fallhoehe <= 287:
            if fallhoehe > 33:
                pygame.draw.circle(
                    game_window, black, ((spalte + 1), (fallhoehe - change)), 23, 0
                )
            # print(map[column - 1][s + 1])
            pygame.draw.circle(game_window, farb, ((spalte + 1), fallhoehe), 23, 0)
            if fallhoehe - 50 >= arrayHoeheNeu:
                arrayHoeheNeu = fallhoehe
                if s <= 4 and iteration >= 1:
                    s += 1
                if s == 5:
                    s -= 1  # für while abfrage
                    sOr = 5
                    # print("hurray")
            fallhoehe += change
            pygame.display.update()
            fps.tick(60)
            iteration += 1
            if not map[column - 1][s + 1] == 0:
                bedingung = False
                while fallhoehe - (50 - 13) <= arrayHoeheNeu:
                    # print("moin")
                    pygame.draw.circle(
                        game_window, black, ((spalte + 1), (fallhoehe - change)), 23, 0
                    )
                    # print(map[column - 1][s + 1])
                    pygame.draw.circle(
                        game_window, farb, ((spalte + 1), fallhoehe), 23, 0
                    )
                    fallhoehe += change
                    pygame.display.update()
                    fps.tick(60)
        t = 0
        if sOr == 5:
            t = 1
        print("")
        # print(s + 1)
        map[column - 1][s + t] = color
        """j = 0
        while j <= (6 - 1):
            i = 0
            while i <= (7 - 1):
                print(map[i][j], end="")  # end->kein ZeilenUmbruch
                i += 1
            j += 1
        print("")"""

    x = 1
    player = 1

    def spalteFree(senk):
        j = 0
        valBol = True
        try:
            while not map[senk][j] == 0:
                j += 1
        except IndexError:
            valBol = False
        return valBol

    # valBol = 0

    # i = 0
    # j = 0

    def winMapHandle(what, c, d, valBol):
        match what:
            case 0:  # set
                if valBol == 0:
                    mapWinner[c][d] = 1
            case 1:  # reset
                if valBol == 0:
                    a = 0
                    while a <= 5:
                        b = 0
                        while b <= 6:
                            mapWinner[b][a] = 0
                            b += 1
                        a += 1
            case _:
                print("mistake")

    def gameOver():
        # print("check")
        valBol = 0
        j = 0
        zahler = 0
        status = None
        while j <= (6 - 1):
            i = 0
            zahler = 0
            while i <= (7 - 1):
                if not map[i][j] == 0:
                    status = map[i][j]
                    if i <= 5 and map[i + 1][j] == status:
                        # print("in progress0")
                        winMapHandle(0, i, j, valBol)
                        zahler += 1
                    else:
                        winMapHandle(1, i, j, valBol)
                        zahler = 0
                    if zahler >= 3:
                        # print("gewonnen0")
                        valBol = status
                        mapWinner[i + 1][j] = 1
                else:
                    winMapHandle(1, i, j, valBol)
                    zahler = 0
                i += 1
            j += 1
        i = 0
        while i <= (7 - 1):
            j = 0
            zahler = 0
            while j <= (6 - 1):
                if not map[i][j] == 0:
                    status = map[i][j]
                    if j <= 4 and map[i][j + 1] == status:
                        # print("in progress1")
                        winMapHandle(0, i, j, valBol)
                        zahler += 1
                    else:
                        winMapHandle(1, i, j, valBol)
                        zahler = 0
                    if zahler >= 3:
                        # print("gewonnen1")
                        valBol = status
                        mapWinner[i][j + 1] = 1
                else:
                    winMapHandle(1, i, j, valBol)
                    zahler = 0
                j += 1
            i += 1
        zahler = 0  # diagonal oben 00 unten
        max = 5
        j = 0
        co = 0
        while j <= 5:
            i = 0
            while i <= max:
                if not map[i][j] == 0:
                    status = map[i][j]
                    if j <= 4 and map[i + 1][j + 1] == status:
                        zahler += 1
                        winMapHandle(0, i, j, valBol)
                    else:
                        winMapHandle(1, i, j, valBol)
                        zahler = 0
                    if zahler >= 3:
                        mapWinner[i + 1][j + 1] = 1
                        valBol = status
                else:
                    winMapHandle(1, i, j, valBol)
                    zahler = 0
                i += 1
                j += 1
            max -= 1
            co += 1
            j = co
        zahler = 0  # diagonal oben 00 unten
        max = 5
        i = 1
        co = 0
        while i <= 5:
            j = 0
            while j <= max:
                if not map[i][j] == 0:
                    status = map[i][j]
                    if i - 1 <= 4 and map[i + 1][j + 1] == status:
                        winMapHandle(0, i, j, valBol)
                        zahler += 1
                    else:
                        winMapHandle(1, i, j, valBol)
                        zahler = 0
                    if zahler >= 3:
                        mapWinner[i + 1][j + 1] = 1
                        valBol = status
                else:
                    winMapHandle(1, i, j, valBol)
                    zahler = 0
                i += 1
                j += 1
            max -= 1
            co += 1
            i = co

        zahler = 0  # diagonal oben 00 unten
        max = 5
        j = 5
        co = 5
        while j >= 0:
            i = 0
            while i <= max:
                if not map[i][j] == 0:
                    status = map[i][j]
                    if j >= 1 and map[i + 1][j - 1] == status:
                        winMapHandle(0, i, j, valBol)
                        zahler += 1
                    else:
                        winMapHandle(1, i, j, valBol)
                        zahler = 0
                    if zahler >= 3:
                        mapWinner[i + 1][j - 1] = 1
                        valBol = status
                else:
                    winMapHandle(1, i, j, valBol)
                    zahler = 0
                i += 1
                j -= 1
            max -= 1
            co -= 1
            j = co
        zahler = 0  # diagonal oben 00 unten
        max = 0
        i = 1
        co = 0
        while i <= 5:
            j = 5
            while j >= max:
                if not map[i][j] == 0:
                    status = map[i][j]
                    if i - 1 <= 4 and j >= 1 and map[i + 1][j - 1] == status:
                        winMapHandle(0, i, j, valBol)
                        zahler += 1
                    else:
                        winMapHandle(1, i, j, valBol)
                        zahler = 0
                    if zahler >= 3:
                        mapWinner[i + 1][j - 1] = 1
                        valBol = status
                else:
                    winMapHandle(1, i, j, valBol)
                    zahler = 0
                i += 1
                j -= 1
            max += 1
            co += 1
            i = co

        return valBol

    def drawVicLine():
        x1 = None
        x4 = None
        y1 = None
        y4 = None
        x1C = 0
        x4C = 0
        y1C = 0
        y4C = 0
        j = 0
        while j <= (6 - 1):
            i = 0
            while i <= (7 - 1):
                if mapWinner[i][j] == 1:
                    if x1 == None:
                        x1 = i
                        y1 = j
                    else:
                        x4 = i
                        y4 = j
                i += 1
            j += 1
        match x1:
            case 0:
                x1C = 35
            case 1:
                x1C = 86
            case 2:
                x1C = 137
            case 3:
                x1C = 188
            case 4:
                x1C = 239
            case 5:
                x1C = 290
            case 6:
                x1C = 341
        match x4:
            case 0:
                x4C = 35
            case 1:
                x4C = 86
            case 2:
                x4C = 137
            case 3:
                x4C = 188
            case 4:
                x4C = 239
            case 5:
                x4C = 290
            case 6:
                x4C = 341
        match y1:
            case 0:
                y1C = 35
            case 1:
                y1C = 85
            case 2:
                y1C = 135
            case 3:
                y1C = 185
            case 4:
                y1C = 235
            case 5:
                y1C = 285
        match y4:
            case 0:
                y4C = 35
            case 1:
                y4C = 85
            case 2:
                y4C = 135
            case 3:
                y4C = 185
            case 4:
                y4C = 235
            case 5:
                y4C = 285
        print("x1")
        print(x1)
        print("x4")
        print(x4)
        print("y1")
        print(y1)
        print("y4")
        print(y4)
        y4CDown = y1C
        while x1 == x4 and y4CDown <= y4C:
            pygame.draw.line(game_window, white, (x1C, y1C), (x4C, y4CDown), 5)
            pygame.display.update()
            fps.tick(60)
            y4CDown += 15
        x4CRight = x1C
        while y1 == y4 and x4CRight <= x4C:
            pygame.draw.line(game_window, white, (x1C, y1C), (x4CRight, y4C), 5)
            pygame.display.update()
            fps.tick(60)
            x4CRight += 15
        x4CLeft = x1C
        y4CDown = y1C
        while (
            x1 > x4 and not y1 == y4 and x4CLeft >= x4C
        ):  # oben rechts nach unten links
            pygame.draw.line(game_window, white, (x1C, y1C), (x4CLeft, y4CDown), 5)
            pygame.display.update()
            fps.tick(60)
            x4CLeft -= 15
            y4CDown += 15
        x4CRight = x1C
        y4CDown = y1C
        while (
            x1 < x4 and not y1 == y4 and x4CRight <= x4C
        ):  # oben links nach unten rechts
            pygame.draw.line(game_window, white, (x1C, y1C), (x4CRight, y4CDown), 5)
            pygame.display.update()
            fps.tick(60)
            x4CRight += 15
            y4CDown += 15

    def celebration():
        fallhoehe = 0
        while fallhoehe <= window_y * 2:
            farbe = int(random.random() * 6.9)
            breite = int(random.random() * (window_x + 0.9))
            abstand = int(random.random() * 100)
            colRan = 0
            change = 10
            match farbe:
                case 0:
                    colRan = red
                case 1:
                    colRan = green
                case 2:
                    colRan = blue
                case 3:
                    colRan = yellow
                case 4:
                    colRan = orange
                case 5:
                    colRan = pink
                case 6:
                    colRan = lila
            pygame.draw.circle(game_window, black, (breite, fallhoehe - change), 8, 0)
            img = pygame.image.load("temp.png")
            screen.blit(img, (0, 0))
            pygame.draw.circle(game_window, colRan, (breite, fallhoehe), 8, 0)
            pygame.display.update()
            fps.tick(60)
            fallhoehe += change

    draw_table()
    fps = pygame.time.Clock()
    pygame.display.update()
    while gameOver() == 0:
        block = False
        try:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.KEYDOWN:
                    # print("2")
                    if event.key == pygame.K_1 and not block:
                        block = True
                        x = 1
                    if event.key == pygame.K_2 and not block:
                        block = True
                        x = 2
                    if event.key == pygame.K_3 and not block:
                        block = True
                        x = 3
                    if event.key == pygame.K_4 and not block:
                        block = True
                        x = 4
                    if event.key == pygame.K_5 and not block:
                        block = True
                        x = 5
                    if event.key == pygame.K_6 and not block:
                        block = True
                        x = 6
                    if event.key == pygame.K_7 and not block:
                        block = True
                        x = 7
            if block:
                if spalteFree(x - 1):
                    newCircle(player, x)
                    pygame.display.update()
                    fps.tick(10)
                    if player == 1:
                        player = 2
                    else:
                        player = 1
        except Exception as e:
            hi = 0
            print(e)
            pygame.quit()
            quit()
    # print(gameOver())
    j = 0
    while j <= (6 - 1):
        i = 0
        while i <= (7 - 1):
            print(mapWinner[i][j], end="")  # end->kein ZeilenUmbruch
            i += 1
        j += 1
        print("")

    if gameOver() == 1:
        pygame.draw.rect(
            game_window, blue, pygame.Rect(0, 310, 377, 40)
        )  # unterer balken
    else:
        pygame.draw.rect(
            game_window, red, pygame.Rect(0, 310, 377, 40)
        )  # unterer balken
    drawVicLine()
    pygame.display.update()
    fps.tick(60)
    pygame.image.save(game_window, "temp.png")
    # print(event)
    celebration()
    celebration()
    # celebration()
    soll = True
    while soll:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.KEYDOWN:
                soll = False
