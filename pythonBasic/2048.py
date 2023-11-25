import pygame
import sys
import random

# 기본 설정
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# 다양한 색상 정의
COLORS = {
    0: (255, 255, 255),   # White for empty cells
    2: (255, 255, 128),   # Yellow
    4: (255, 255, 0),     # Dark Yellow
    8: (255, 192, 128),   # Orange
    16: (255, 165, 0),    # Dark Orange
    32: (255, 140, 0),    # Red-Orange
    64: (255, 69, 0),     # Red-Orange (Dark)
    128: (255, 0, 0),     # Red
    256: (255, 0, 128),   # Pink
    512: (255, 0, 255),   # Magenta
    1024: (128, 0, 255),  # Purple
    2048: (75, 0, 130),   # Indigo
}

# 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Game")

# 게임 보드 초기화
board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# 빈 타일 찾기
def empty_tiles():
    return [(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE) if board[x][y] == 0]

# 새로운 타일 추가
def add_tile():
    empty = empty_tiles()
    if empty:
        x, y = random.choice(empty)
        board[x][y] = 2 if random.random() < 0.9 else 4

# 화면에 타일 그리기
def draw_tiles():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            value = board[x][y]
            color = COLORS.get(value, WHITE)
            pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

# 초기 화면 설정 함수
def initScreen():
    screen.fill(WHITE)

# 이동 함수
def move(direction):
    # 이동 전 상태 저장
    original_board = [row[:] for row in board]

    if direction == 'UP':
        # 이동 로직
        for x in range(GRID_SIZE):
            for y in range(1, GRID_SIZE):
                # 이동
                if board[x][y] != 0:
                    for k in range(y, 0, -1):
                        if board[x][k-1] == 0:
                            board[x][k-1] = board[x][k]
                            board[x][k] = 0
                        # 합치기
                        elif board[x][k-1] == board[x][k]:
                            board[x][k-1] *= 2
                            board[x][k] = 0
                            break
                        else:
                            break
    elif direction == 'DOWN':
        # 이동 로직
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE - 2, -1, -1):
                # 이동
                if board[x][y] != 0:
                    for k in range(y, GRID_SIZE - 1):
                        if board[x][k+1] == 0:
                            board[x][k+1] = board[x][k]
                            board[x][k] = 0
                        # 합치기
                        elif board[x][k+1] == board[x][k]:
                            board[x][k+1] *= 2
                            board[x][k] = 0
                            break
                        else:
                            break
    elif direction == 'LEFT':
        # 이동 로직
        for y in range(GRID_SIZE):
            for x in range(1, GRID_SIZE):
                # 이동
                if board[x][y] != 0:
                    for k in range(x, 0, -1):
                        if board[k-1][y] == 0:
                            board[k-1][y] = board[k][y]
                            board[k][y] = 0
                        # 합치기
                        elif board[k-1][y] == board[k][y]:
                            board[k-1][y] *= 2
                            board[k][y] = 0
                            break
                        else:
                            break
    elif direction == 'RIGHT':
        # 이동 로직
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE - 2, -1, -1):
                # 이동
                if board[x][y] != 0:
                    for k in range(x, GRID_SIZE - 1):
                        if board[k+1][y] == 0:
                            board[k+1][y] = board[k][y]
                            board[k][y] = 0
                        # 합치기
                        elif board[k+1][y] == board[k][y]:
                            board[k+1][y] *= 2
                            board[k][y] = 0
                            break
                        else:
                            break

    # 이동 후 상태와 이전 상태가 다르면 새로운 타일 추가
    if original_board != board:
        add_tile()

# 화면 업데이트 함수
def update_screen():
    initScreen()
    draw_tiles()
    pygame.display.flip()

# 게임 오버 여부 확인 함수
def is_game_over():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if board[x][y] == 0:
                return False  # 아직 빈 타일이 있으면 게임 계속 진행

            # 상하좌우 타일 중 하나라도 같은 숫자가 있으면 게임 계속 진행
            if (x < GRID_SIZE - 1 and board[x][y] == board[x + 1][y]) or \
               (y < GRID_SIZE - 1 and board[x][y] == board[x][y + 1]):
                return False

    return True  # 모든 타일이 다르고 빈 타일도 없으면 게임 오버

# 게임 오버 화면
def game_over_screen():
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # 2초 동안 화면 표시
    pygame.quit()
    sys.exit()

# 화면 업데이트 및 게임 오버 여부 확인 함수
def update_and_check_game_over():
    update_screen()
    if is_game_over():
        game_over_screen()

# 게임 루프
def game_loop():
    add_tile()
    add_tile()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 키보드 입력 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move('UP')
                    update_and_check_game_over()
                elif event.key == pygame.K_DOWN:
                    move('DOWN')
                    update_and_check_game_over()
                elif event.key == pygame.K_LEFT:
                    move('LEFT')
                    update_and_check_game_over()
                elif event.key == pygame.K_RIGHT:
                    move('RIGHT')
                    update_and_check_game_over()

# 게임 루프 실행
game_loop()