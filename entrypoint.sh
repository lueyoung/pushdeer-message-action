#!/bin/bash

python3 /src/messager.py \
  --enable "${INPUT_ENABLE}" \
  --pushkey "${INPUT_PUSHKEY}" \
  --text "${INPUT_TEXT}" \
  --desp "${INPUT_DESP}"
