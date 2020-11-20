#!/bin/bash
set -euxo pipefail
WORK_DIR="/home/pi/entrance"

unit=$1
state=$2

date
sudo "${WORK_DIR}"/NexaTransmitter/NexaController --pin 2 --remote-id 15213030 --unit ${unit} ${state}
