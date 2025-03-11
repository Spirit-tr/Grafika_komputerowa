import pygame

pygame.init()

WIDTH, HEIGHT = 300, 300
BG_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Figura - Koło i Kwadrat")

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

circle_radius = 80
square_size = 80
center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    screen.fill(BG_COLOR)

    pygame.draw.circle(screen, BLACK, center, circle_radius)

    square_rect = pygame.Rect(0, 0, square_size, square_size)
    square_rect.center = center
    pygame.draw.rect(screen, YELLOW, square_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
