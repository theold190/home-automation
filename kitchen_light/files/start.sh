#!/bin/bash
set -euxo pipefail
WORK_DIR="/home/pi/sink_light"

"${WORK_DIR}"/.venv/bin/python -u "${WORK_DIR}"/kitchenSinkLights.py
