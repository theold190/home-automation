#!/bin/bash
set -euxo pipefail
WORK_DIR="/home/pi/entrance"

"${WORK_DIR}"/.venv/bin/rpi-rf_send -g 27 -p 397 -t 1 83029

