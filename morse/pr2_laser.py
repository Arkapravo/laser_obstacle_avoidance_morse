# Author : Arkapravo Bhaumik (arkapravobhaumik@gmail.com)
# 10 February 2013, Sunday
# ROS Fuerte, installed at /opt/ros/
# MORSE 0.6 installed at /opt/ros/
# This file should be placed at /opt/ros/morse/share/morse/examples/scenarii/

from morse.builder import *
from morse.builder.extensions.pr2extension import PR2

# Append PR2 robot to the scene
james = PR2()
james.translate(x=6, y=-4, z=0.0)

# Sensors and Actuators for navigation stack
pr2_posture = Sensor('pr2_posture')
james.append(pr2_posture)
pr2_posture.configure_mw('ros')

motion_controller = Actuator('v_omega')
james.append(motion_controller)
motion_controller.configure_mw('ros')

odometry = Sensor('odometry')
james.append(odometry)
odometry.configure_mw('ros')

Sick = Sensor('sick')
Sick.translate(x=0.275, z=0.252)
james.append(Sick)
Sick.properties(Visible_arc=False)
Sick.properties(laser_range=30.0000)
Sick.properties(resolution=1.000)
Sick.properties(scan_window=180.0000)
Sick.configure_mw('ros')

#Set up environment
env = Environment('laas/grande_salle')
env.aim_camera([1.0470, 0, 0.7854])

