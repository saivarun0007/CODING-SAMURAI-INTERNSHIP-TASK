import pygame

pygame.init()
pygame.display.set_caption("𝐂𝐨𝐝𝐢𝐧𝐠 𝐒𝐚𝐦𝐮𝐫𝐚𝐢 𝐈𝐧𝐭𝐞𝐫𝐧 Autonomus-Driving-Simulation")
window = pygame.display.set_mode((1200, 400))
map = pygame.image.load('maps/map5.png')        
car = pygame.image.load('cars/car5.png')     
car = pygame.transform.scale(car, (30, 60))

car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    clock.tick(60)
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15

    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]

    # Change direction (take turns)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        car = pygame.transform.rotate(car, -90)
        cam_x_offset = 30
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x += 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y += 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x += 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)

    # Drive forward
    if direction == 'up' and up_px == 255:
        car_y -= 2
    elif direction == 'right' and right_px == 255:
        car_x += 2
    elif direction == 'down' and down_px == 255:
        car_y += 2

    window.blit(map, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
