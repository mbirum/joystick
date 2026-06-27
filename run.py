import pygame
import os
import time
import sys
import subprocess
import select

sleep_interval = 0.001

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count < 1:
	print("No joystick found")
else:
	y_axis_direction = 0
	y_axis_speed_factor = 1
	x_axis_direction = 0
	x_axis_speed_factor = 1
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	print("Initialized joystick")
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.JOYBUTTONDOWN:
				print(f"Button {event.button} pressed")
			elif event.type == pygame.JOYBUTTONUP:
				print(f"Button {event.button} released")
			elif event.type == pygame.JOYAXISMOTION and event.axis == 0:
				if event.value < 0:
					print(f"left {event.value}")
				elif event.value > 0:
					print(f"right {event.value}")
			elif event.type == pygame.JOYAXISMOTION and event.axis == 1:
				if event.value <= 0.05:
					print(f"up {event.value}")
					y_axis_direction = -1
					speed = 10 - (round(abs(event.value),1) * 10)
					if speed < 1:
						speed = 1
					elif speed > 10:
						speed = 10
					speed = speed / 1000
					sleep_interval = speed
				elif event.value >= 0.07:
					print(f"down {event.value}")
					y_axis_direction = 1
					speed = 10 - (round(abs(event.value),1) * 10)
					if speed < 1:
						speed = 1
					elif speed > 10:
						speed = 10
					speed = speed / 1000
					sleep_interval = speed
				else:
					y_axis_direction = 0
