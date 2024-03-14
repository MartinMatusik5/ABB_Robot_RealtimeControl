import pygame

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print(joysticks[0].get_numaxes())

while True:
    pygame.event.pump()  
    axis_x = joysticks[0].get_axis(0)
    axis_y = joysticks[0].get_axis(1)
    print("Poloha joysticku - X:", axis_x, "Y:", axis_y)
