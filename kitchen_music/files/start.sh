#!/bin/bash
set -euxo pipefail
WORK_DIR="/home/pi/music"

"${WORK_DIR}"/.venv/bin/python -u "${WORK_DIR}"/kitchenMusic.py
