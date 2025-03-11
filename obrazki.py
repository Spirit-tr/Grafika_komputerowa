import pygame
import sys
import math

WIDTH, HEIGHT = 600, 600
BG_COLOR = (255, 255, 0)
CENTER = (WIDTH // 2, HEIGHT // 2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("Transformacje Obrazka")

try:
    image = pygame.image.load("shuttle.jpg").convert_alpha()
    img_width, img_height = 300, 300
    image = pygame.transform.scale(image, (img_width, img_height))
except pygame.error:
    print("Błąd: nie można wczytać obrazu. Upewnij się, że 'shuttle.jpg' jest w folderze.")
    pygame.quit()
    sys.exit()

angle = 0
scale = 1.0
flip_x, flip_y = False, False
shear_x, shear_y = 0.0, 0.0  

def shear_image(image, shear_x, shear_y):
    width, height = image.get_size()

    new_width = width + abs(int(shear_x * height))
    new_height = height + abs(int(shear_y * width))

    sheared_image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)

    for y in range(height):
        for x in range(width):
            pixel = image.get_at((x, y))
            if pixel.a > 0:  
                new_x = x + int(shear_x * y)
                new_y = y + int(shear_y * x)
                if 0 <= new_x < new_width and 0 <= new_y < new_height:
                    sheared_image.set_at((new_x, new_y), pixel)

    return sheared_image

def draw_transformed_image():
    scaled_image = pygame.transform.scale(image, (int(img_width * scale), int(img_height * scale)))
    rotated_image = pygame.transform.rotate(scaled_image, math.degrees(angle))
    sheared_image = shear_image(rotated_image, shear_x, shear_y)

    if flip_x or flip_y:
        sheared_image = pygame.transform.flip(sheared_image, flip_x, flip_y)

    rect = sheared_image.get_rect(center=CENTER)
    screen.blit(sheared_image, rect.topleft)

running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  
                scale *= 0.8
            elif event.key == pygame.K_2:
                scale *= 1.2
            elif event.key == pygame.K_3:  
                angle += math.pi / 6
            elif event.key == pygame.K_4:  
                angle -= math.pi / 6
            elif event.key == pygame.K_5:  
                flip_x = not flip_x
            elif event.key == pygame.K_6:  
                flip_y = not flip_y
            elif event.key == pygame.K_7: 
                shear_x -= 0.1
            elif event.key == pygame.K_8: 
                shear_x += 0.1
            elif event.key == pygame.K_9: 
                angle, scale = 0, 1.0
                flip_x, flip_y = False, False
                shear_x, shear_y = 0.0, 0.0

    draw_transformed_image()
    pygame.display.flip()

pygame.quit()
