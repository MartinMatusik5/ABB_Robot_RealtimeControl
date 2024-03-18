import socket
import egm.egm_pb2 as abbegm
import pygame
from time import sleep
import threading

# Sampling period in seconds
dt = 0.1
max_speed = 100
rotation_speed = 15

offset_x = 0
offset_y = 0
offset_z = 0 

offset_rx = 0
offset_ry = 0
offset_rz = 0
 

ip_addr = "127.0.0.1"
port = 6599

socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sensor_msg = abbegm.EgmSensor()

sensor_msg.header.seqno = 0
sensor_msg.header.mtype = abbegm.EgmHeader.MessageType.MSGTYPE_CORRECTION

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print(joysticks[0].get_numaxes())

control_mode = "CARTESIAN"
lock_mode = False

# Původní hodnoty
original_values = {"offset_x": 0, "offset_y": 0, "offset_z": 0, "offset_rx": 0, "offset_ry": 0, "offset_rz": 0}

def reset_values():
    global offset_x, offset_y, offset_z, offset_rx, offset_ry, offset_rz
    offset_x = original_values["offset_x"]
    offset_y = original_values["offset_y"]
    offset_z = original_values["offset_z"]
    offset_rx = original_values["offset_rx"]
    offset_ry = original_values["offset_ry"]
    offset_rz = original_values["offset_rz"]
    print("Hodnoty obnoveny")

def gripper():
    gripper_state = "opened"
    while True: 
        if joysticks[0].get_button(0) and gripper_state == "opened": 
            gripper_state = "closed"
            print("close")
        elif not joysticks[0].get_button(0) and gripper_state == "closed":  
            gripper_state = "opened"
            print("open")

if __name__ == '__main__':

    try:
        # Vytvoření vlákna pro ovládání gripperu
        #threading.Thread(target=gripper, name="gripper", daemon=True).start()

        while True:
            pygame.event.pump()

            # Stisknutí tlačítka
            if not joysticks[0].get_button(2):
                offset_x += joysticks[0].get_axis(1) * max_speed * dt
                offset_y += joysticks[0].get_axis(0) * max_speed * dt
                offset_z += joysticks[0].get_axis(5) * max_speed * dt
            else:
                offset_rx += joysticks[0].get_axis(0) * rotation_speed * dt
                offset_ry += joysticks[0].get_axis(1) * rotation_speed * dt
                offset_rz += joysticks[0].get_axis(5) * rotation_speed * dt   
        
            # Tlačítko pro resetování hodnot offsetu
            if joysticks[0].get_button(26):  
                reset_values()

            sensor_msg.header.seqno += 1
            sensor_msg.planned.cartesian.pos.x = offset_x
            sensor_msg.planned.cartesian.pos.y = offset_y 
            sensor_msg.planned.cartesian.pos.z = offset_z
            sensor_msg.planned.cartesian.euler.x = offset_rx
            sensor_msg.planned.cartesian.euler.y = offset_ry
            sensor_msg.planned.cartesian.euler.z = offset_rz
            socketUDP.sendto(sensor_msg.SerializeToString(), (ip_addr, port))
            
            sleep(dt)

    except KeyboardInterrupt:
        socketUDP.close()
        print("\rTHE END")
