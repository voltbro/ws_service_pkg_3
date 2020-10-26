#!/bin/bash

python -m compileall -f ./scripts/service_configuration.py
mv ./scripts/service_configuration.pyc ./run/service_configuration.pyc
