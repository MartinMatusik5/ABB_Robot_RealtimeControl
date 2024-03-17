import socket
import egm.egm_pb2 as abbegm
import pygame
from time import sleep

# Sampling period in seconds
dt = 0.1
max_speed = 100

offset_x = 0
offset_y = 0
offset_z = 0 
 

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

if __name__ == '__main__':

    try:
        while True:
            pygame.event.pump()           
        
            
            offset_x += joysticks[0].get_axis(1) * max_speed * dt
            offset_y += joysticks[0].get_axis(0) * max_speed * dt
            offset_z += joysticks[0].get_axis(5) * max_speed * dt

            sensor_msg.header.seqno += 1
            sensor_msg.planned.cartesian.pos.x = offset_x + 1000
            sensor_msg.planned.cartesian.pos.y = offset_y 
            sensor_msg.planned.cartesian.pos.z = offset_z + 350  
            sensor_msg.planned.cartesian.euler.x = 0
            sensor_msg.planned.cartesian.euler.y = 0
            sensor_msg.planned.cartesian.euler.z = 0
            socketUDP.sendto(sensor_msg.SerializeToString(), (ip_addr, port))
            
            sleep(dt)

    except KeyboardInterrupt:
        socketUDP.close()
        print("\rTHE END")
