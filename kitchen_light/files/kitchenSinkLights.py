#!/usr/bin/env python
from gpiozero import MotionSensor, LED
from threading import Timer

import datetime
import sys
import time

relay = LED(4)

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
    relay.on()


def turn_lights_on():
    global lights_off_timer
    if lights_off_timer:
        lights_off_timer.cancel()
    lights_off_timer = getTimer(True)
    relay.off()


def motion_detected():
    if debug:
        print("{}: Motion detected....".format(datetime.datetime.now()))

    turn_lights_on()


def run(pirs, singleRun=False):
    current = [None for pir in pirs]
    previous = [None for pir in pirs]
    try:
        while True:
            for i, pir in enumerate(pirs):
                # Read PIR state
                current[i] = pir.motion_detected

                # If the PIR is triggered
                if current[i] and not previous[i]:
                    # print("    Motion detected!")
                    # Record previous state
                    previous[i] = True
                # If the PIR has returned to ready state
                elif not current[i] and previous[i]:
                    # print("    No Motion")
                    previous[i] = False
                else:
                    # print("    Just started")
                    previous[i] = current[i]

            time.sleep(0.3)
    except KeyboardInterrupt:
        print("Leaving...")


if __name__ == '__main__':
    pir = MotionSensor(pin=14)
    pir.when_motion = lambda: motion_detected()
    relay.on()

    run([])
