#!/bin/bash
set -euxo pipefail

exit_code=0
sudo systemctl status hyperiond@pi.service | tail -n 2 | grep -v "No such device" > /dev/null || exit_code=$?

if [ $exit_code -ne 0 ]; then
  printf "Restarting hyperiond service due to encountered error on %s\n" "$(date)"
  sudo systemctl restart hyperiond@pi.service
fi
