#!/bin/bash
set -euxo pipefail
WORK_DIR="/home/pi/entrance"

"${WORK_DIR}"/NexaTransmitter/NexaController --pin 2 --unit 1 --remote-id 15213030 off
