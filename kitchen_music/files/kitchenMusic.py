#!/usr/bin/env python

import flicklib
import time
import os
import soco

@flicklib.flick()
def flick(start,finish):
    global flick_txt
    flick_txt = start + ' - ' + finish

def play(sonos):
  #if sonos.get_current_transport_info()['current_transport_state'] != 'PLAYING':
  #  sonos.volume = 15
  sonos.play()

def pause(sonos):
  sonos.pause()

flick_action = {
  'west - east': play,
  'east - west': pause
}

def main():
  counter = 0
  global flick_txt
  flick_txt = ""

  while True:
    try:
      # sonos = soco.discovery.any_soco()
      sonos = soco.SoCo('192.168.10.156')
      break
    except:
      print("Can't find sonos")
      time.sleep(5)
  print("Sonos detected")

  while True:
    if flick_txt in flick_action.keys():
      flick_action.get(flick_txt)(sonos)
      print("flick_txt: %s" % (flick_txt))
      flick_txt = ""
    time.sleep(0.1)

if __name__ == "__main__":
  main()
