#!/usr/bin/env python

import flicklib
import time
import os
import soco


@flicklib.flick()
def flick(start, finish):
    global flick_txt
    flick_txt = start + " - " + finish


def play(all_sonos):
    for sonos in all_sonos:
        if sonos.is_coordinator:
            sonos.play()


def pause(all_sonos):
    for sonos in all_sonos:
        if sonos.is_coordinator:
            sonos.pause()


flick_action = {"west - east": play, "east - west": pause}


def discover_all_sonos():
    all_sonos = set()
    while True:
        try:
            all_sonos = soco.discover()
            break
        except Exception:
            print("Can't find sonos")
            time.sleep(5)
    print("Sonos detected")
    return all_sonos


def run_flick(all_sonos):
    global flick_txt
    flick_txt = ""

    while True:
        if flick_txt in flick_action.keys():
            flick_action.get(flick_txt)(all_sonos)
            print("flick_txt: %s" % (flick_txt))
            flick_txt = ""
        time.sleep(0.1)


def main():
    all_sonos = discover_all_sonos()
    run_flick(all_sonos)


if __name__ == "__main__":
    main()
