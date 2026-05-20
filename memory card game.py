import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Card Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 90, 200)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

# Font
font = pygame.font.SysFont(None, 60)

# Grid settings
ROWS, COLS = 4, 4
CARD_SIZE = 100
PADDING = 20

# Generate card values
values = list(range(1, 9)) * 2
random.shuffle(values)

# Create cards
cards = []
for row in range(ROWS):
    for col in range(COLS):
        x = col * (CARD_SIZE + PADDING) + 120
        y = row * (CARD_SIZE + PADDING) + 50

        cards.append({
            "rect": pygame.Rect(x, y, CARD_SIZE, CARD_SIZE),
            "value": values.pop(),
            "revealed": False,
            "matched": False
        })

first_card = None
second_card = None
waiting = False
wait_time = 0

clock = pygame.time.Clock()

running = True

while running:
    screen.fill(WHITE)

    # Draw cards
    for card in cards:
        if card["revealed"] or card["matched"]:
            pygame.draw.rect(screen, GREEN, card["rect"])
            text = font.render(str(card["value"]), True, BLACK)
            text_rect = text.get_rect(center=card["rect"].center)
            screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, BLUE, card["rect"])

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not waiting:
            mouse_pos = pygame.mouse.get_pos()

            for card in cards:
                if (
                    card["rect"].collidepoint(mouse_pos)
                    and not card["revealed"]
                    and not card["matched"]
                ):
                    card["revealed"] = True

                    if first_card is None:
                        first_card = card
                    elif second_card is None:
                        second_card = card
                        waiting = True
                        wait_time = pygame.time.get_ticks()

    # Check match
    if waiting:
        current_time = pygame.time.get_ticks()

        if current_time - wait_time > 1000:
            if first_card["value"] == second_card["value"]:
                first_card["matched"] = True
                second_card["matched"] = True
            else:
                first_card["revealed"] = False
                second_card["revealed"] = False

            first_card = None
            second_card = None
            waiting = False

    # Winning message
    if all(card["matched"] for card in cards):
        win_text = font.render("YOU WIN!", True, BLACK)
        screen.blit(win_text, (280, 550))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()