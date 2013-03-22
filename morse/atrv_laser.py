# Author : Arkapravo Bhaumik (arkapravobhaumik@gmail.com)
# 10 February 2013, Sunday
# ROS Fuerte, installed at /opt/ros/
# MORSE 0.6 installed at /opt/ros/
# This file should be placed at /opt/ros/morse/share/morse/examples/scenarii

from morse.builder import *

# Append ATRV robot rob to the scene
rob = Robot('atrv')
rob.translate(x=-9, y=6, z=0.0)

# Append an actuator to castor
motion = Actuator('xy_omega')
motion.translate(z=0.3)
rob.append(motion)

# Append a Gyroscope sensor
gyroscope = Sensor('gyroscope')
gyroscope.translate(z=0.83)
rob.append(gyroscope)

# Configuring the middlewares
gyroscope.configure_mw('ros')
motion.configure_mw('ros')

Sick = Sensor('sick')
Sick.translate(x=0.20, y =-0.02, z=0.95)
rob.append(Sick)
Sick.properties(Visible_arc=False)
Sick.properties(laser_range=30.0000)
Sick.properties(resolution=0.5000)
Sick.properties(scan_window=180.0000)
Sick.configure_mw('ros')

# Append Keyboard Control to pollux
Keyb = Actuator('keyboard')
Keyb.properties(Speed=3.0)
rob.append(Keyb)

#Set up environment
env = Environment('indoors-1/indoor-1')
env.aim_camera([1.0470, 0, 0.7854])

