import pygame

colors = {
    'black': (0,0,0),
    'white': (255,255,255),
    '2': (224, 247, 250),
    '4': (179, 229, 252),
    '8': (129, 212, 250),
    '16': (79, 195, 247),
    '32': (41, 182, 246),
    '64': (3, 169, 244),
    '128': (3, 155, 229),
    '256': (2, 136, 209),
    '512': (2, 119, 189),
    '1024': (1, 87, 155),
    '2048': (0, 78, 140)
}

board = [{-1,-1,-1,-1},
{-1,-1,-1,-1},
{-1,-1,-1,-1},
{-1,-1,-1,-1}
         ]

def initScreen():
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    screen.fill(['white'])
    pygame.display.update()

isGameRunnig = True

def setEventListener():
    global isGameRunning
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                isGameRunning = False
            elif event == pygame.K_DOWN:
                print("아래")
            elif event == pygame.K_UP:
                print("위")
            elif event == pygame.K_RIGHT:
                print("오른쪽")

def drawDisplay():
    global isGameRunnig
    baseX = 35
    baseY = 35
    blockHeight = 100
    blockWidth = 100
    blocckSize = (100,100)
    margin = 10

    for i in range(4):
        for j in range(4):
            x = (blockWidth + margin) * j + baseX
            y = (blockHeight + margin) * i + baseY
            date = str(board[i][j])

    pygame.draw



def run2048():
    pygame.init()
    initScreen()
    print("2048 게임 시작")

    while isGameRunnig:
        setEventListener()

        for event in pygame.event.get():
            pass
    pygame.quit()

run2048()
