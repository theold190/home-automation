#!/bin/bash
set -euxo pipefail

ansible-lint .
yamllint .
