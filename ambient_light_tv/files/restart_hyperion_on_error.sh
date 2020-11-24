#!/bin/bash
set -euxo pipefail

# Sometimes hyperion service gets in a state that it stops function. In those cases you see errors in the logs, while
# service continues to run. This script is meant to restart hyperion service whenever one of the following errors are
# detected:
#
# Error 1:
# Nov 20 18:23:04 raspberrypi hyperiond[521]: 2020-11-20T18:23:04.252 hyperiond V4L2:/DEV/VI : <ERROR> Throws error nr:
# VIDIOC_DQBUF error code 19, No such device
# Nov 20 18:23:04 raspberrypi hyperiond[521]: 2020-11-20T18:23:04.267 hyperiond V4L2:/DEV/VI : <ERROR>
# VIDIOC_STREAMOFF  error code  19, No such device
# Nov 20 18:23:04 raspberrypi [521]: Throws error nr: VIDIOC_DQBUF error code 19, No such device
# Nov 20 18:23:04 raspberrypi [521]: VIDIOC_STREAMOFF  error code  19, No such device
#
# Error 2:
# Cannot identify '/dev/video0' error code 2, No such file or directory
# Nov 21 20:30:04 raspberrypi [9600]: Throws error nr: Cannot identify '/dev/video0' error code 2, No such file or
# directory

exit_code=0
sudo systemctl status hyperiond@pi.service | tail -n 2 | \
  grep -v "No such device" | \
  grep -v "Cannot identify '/dev/video0' error code" > /dev/null || exit_code=$?

if [ $exit_code -ne 0 ]; then
  printf "Restarting hyperiond service due to encountered error on %s\n" "$(date)"
  sudo systemctl restart hyperiond@pi.service
fi
