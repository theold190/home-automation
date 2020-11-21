#!/bin/bash
set -euxo pipefail

ansible-lint .
yamllint .
python3 -m pycodestyle .

# Shellcheck
find . -name '*.sh' | while IFS='' read -r filepath
do
  shellcheck "$filepath"
done
