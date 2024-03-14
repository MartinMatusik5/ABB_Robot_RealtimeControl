#!/usr/bin/env python3

import socket
import egm.egm_pb2 as abbegm
from time import sleep
import random


ip_addr = "127.0.0.1"
port = 6599

socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# socketUDP.bind((ip_addr, 6510))
# robot_msg = abbegm.EgmRobot()
sensor_msg = abbegm.EgmSensor()

sensor_msg.header.seqno = 0
sensor_msg.header.mtype = abbegm.EgmHeader.MessageType.MSGTYPE_CORRECTION

if __name__ == '__main__':

    try:
        while True:
            sensor_msg.header.seqno += 1
            sensor_msg.planned.cartesian.pos.x = 1000
            sensor_msg.planned.cartesian.pos.y = random.uniform(-200, 200)
            sensor_msg.planned.cartesian.pos.z = 350
            sensor_msg.planned.cartesian.euler.x = 0
            sensor_msg.planned.cartesian.euler.y = 0
            sensor_msg.planned.cartesian.euler.z = 0
            socketUDP.sendto(sensor_msg.SerializeToString(), (ip_addr, port))
            # msg, _ = socketUDP.recvfrom(1400)
            # robot_msg.ParseFromString(msg)
            # print(robot_msg.planned.cartesian.pos.x)
            sleep(0.5)

    except KeyboardInterrupt:
        socketUDP.close()
        print("\rTHE END")