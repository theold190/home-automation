#!/usr/bin/env python
from gpiozero import MotionSensor, LED
from threading import Timer

import datetime
import sys
import time

relays = [LED(3), LED(4)]

lights_timeout = 180
lights_off_timer = None

debug = True


def getTimer(start=False):
    timer = Timer(lights_timeout, turn_lights_off)
    if start:
        timer.start()
    return timer


def turn_lights_off():
    if debug:
        print("{}: Turning lights off".format(datetime.datetime.now()))
    for relay in relays:
        relay.on()


def turn_lights_on():
    global lights_off_timer
    if lights_off_timer:
        lights_off_timer.cancel()
    lights_off_timer = getTimer(True)
    for relay in relays:
        relay.off()


def motion_detected():
    if debug:
        print("{}: Motion detected....".format(datetime.datetime.now()))

    turn_lights_on()


if __name__ == '__main__':
    pir = MotionSensor(pin=14, pull_up=False, active_state=False)
    pir.when_motion = lambda: motion_detected()
    turn_lights_off()
    try:
        while True:
            pir.wait_for_motion()
    except KeyboardInterrupt:
        print("Leaving...")
