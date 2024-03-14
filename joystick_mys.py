import pygame
import pyautogui

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print(joysticks[0].get_numaxes())

while True:
    pygame.event.pump()  
    axis_x = joysticks[0].get_axis(0)
    axis_y = joysticks[0].get_axis(1)
    print("Poloha joysticku - X:", axis_x, "Y:", axis_y)
    
    # Získání rozměrů obrazovky
    screenWidth, screenHeight = pyautogui.size()
    
    # Přepočet hodnoty z rozsahu (-1, 1) na rozsah (0, screenWidth) pro osu X
    mouseX = int((axis_x + 1) * screenWidth / 2)
    # Přepočet hodnoty z rozsahu (-1, 1) na rozsah (0, screenHeight) pro osu Y
    mouseY = int((axis_y + 1) * screenHeight / 2)
    
    # Nastavení nové pozice myši
    pyautogui.moveTo(mouseX, mouseY)
