#!/usr/bin/env python3

import socket
import egm.egm_pb2 as abbegm
from time import sleep
import pygame

# Sampling period in seconds
dt = 0.1
max_speed = 100

offset_x = 0
offset_y = 0

ip_addr = "127.0.0.1"
port = 6599

socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# socketUDP.bind((ip_addr, 6510))
# robot_msg = abbegm.EgmRobot()
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
            offset_x = offset_x + joysticks[0].get_axis(1) * max_speed * dt
            offset_y = offset_y + joysticks[0].get_axis(0) * max_speed * dt
            #axis_x = joysticks[0].get_axis(0)
            #axis_y = joysticks[0].get_axis(1)
            #print("Poloha joysticku - X:", offset_x, "Y:", offset_y)
            sensor_msg.header.seqno += 1
            sensor_msg.planned.cartesian.pos.x = offset_x + 1000
            sensor_msg.planned.cartesian.pos.y = offset_y 
            sensor_msg.planned.cartesian.pos.z = 350
            sensor_msg.planned.cartesian.euler.x = 0
            sensor_msg.planned.cartesian.euler.y = 0
            sensor_msg.planned.cartesian.euler.z = 0
            socketUDP.sendto(sensor_msg.SerializeToString(), (ip_addr, port))
            # msg, _ = socketUDP.recvfrom(1400)
            # robot_msg.ParseFromString(msg)
            # print(robot_msg.planned.cartesian.pos.x)
            sleep(dt)

    except KeyboardInterrupt:
        socketUDP.close()
        print("\rTHE END")