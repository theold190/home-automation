Ambient light setup
===================
See https://www.instructables.com/id/Make-Your-Own-Ambient-Lighting-With-the-Raspberry-/ for instructions on how to build the setup.

Tips for others
===============
* When using an USB grabber, there is no way to detect HDMI's CEC (when TV is turned off). So, somehow your Pi setup need to detect this.
  * if HDMI splitter gives nothing, then no need for workarounds
  * some HDMI splitters give constant color when there is no signal (ex. blue). Then you should use Hyperion.NG's Signal detection. You do it by adjusting color threshold, first set all channels to 100% and later reduce needed ones with small steps until you get needed results.
