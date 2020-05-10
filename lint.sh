#!/bin/bash
set -euxo pipefail

ansible-lint .
yamllint .
python3 -m pycodestyle .
