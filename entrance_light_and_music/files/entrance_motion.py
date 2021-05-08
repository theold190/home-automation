#!/usr/bin/env python
import argparse
import datetime
import logging
import os
import soco
import sys
import time

from gpiozero import MotionSensor
from threading import Timer

log = logging.getLogger(__name__)
timer = None


def motion_detected():
    log.debug(f"{datetime.datetime.now()}: Motion detected...")

    # cancel timer, so we can properly start the music
    timer.cancel()

    # start the music
    try:
        all_sonos = set()
        for i in range(5):
            try:
                all_sonos = soco.discover()
                break
            except Exception as e:
                log.error(
                    f"Attempt {i}: Can't find any Sonos players ({str(e)}), waiting..."
                )
                time.sleep(5)
        log.debug(f"{datetime.datetime.now()}: {len(all_sonos)} Sonos players detected")
        for sonos in all_sonos:
            if sonos.is_coordinator:
                sonos.play()

    except Exception as e:
        log.error(f"{datetime.datetime.now()}: {str(e)}")
    finally:
        # make sure to exit application after music was started
        exit_application()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Script start music if motion is detected."
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument(
        "--duration",
        type=int,
        default=30 * 60,
        help="For how long to monitor motion (in seconds)",
    )

    return parser.parse_args()


def exit_application():
    log.debug(f"{datetime.datetime.now()}: Exiting application")
    os._exit(0)


def main():
    args = parse_args()
    if args.debug:
        log.addHandler(logging.StreamHandler())
        log.setLevel(logging.DEBUG)

    global timer
    timer = Timer(args.duration, exit_application)
    timer.start()
    log.debug(
        f"{datetime.datetime.now()}: Motion timer is set for {args.duration} seconds"
    )

    pir = MotionSensor(pin=17)
    pir.when_motion = lambda: motion_detected()
    try:
        while True:
            pir.wait_for_motion()
    except KeyboardInterrupt:
        log.error("Leaving...")

if __name__ == "__main__":
    main()
