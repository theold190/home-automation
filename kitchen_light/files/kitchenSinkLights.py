#!/usr/bin/env python
import argparse
import datetime
import sys
import time

from gpiozero import MotionSensor, LED
from threading import Timer

relays = [LED(3), LED(4)]

lights_timeout = 180
lights_off_timer = None

debug = False


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


def parse_args():
    parser = argparse.ArgumentParser(description='Script to control kitchen sink lights.')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    debug = args.debug

    pir = MotionSensor(pin=14)
    pir.when_motion = lambda: motion_detected()
    turn_lights_off()
    try:
        while True:
            pir.wait_for_motion()
    except KeyboardInterrupt:
        print("Leaving...")
