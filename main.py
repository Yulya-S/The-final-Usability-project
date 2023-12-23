import details
import pygame
import menues

clock = pygame.time.Clock()

details.screen.fill((210, 191, 210))
end_game = True

menu = menues.menu()

while end_game:
    clock.tick(30)

    menu.hover(pygame.mouse.get_pos())
    menu.draw(pygame.mouse.get_pos())

    pygame.display.update()
    for event in pygame.event.get():
        wind = menu.press(event, pygame.mouse.get_pos())
        if wind != None:
            menu = wind()

        if event.type == pygame.QUIT:
            end_game = False

pygame.quit()
