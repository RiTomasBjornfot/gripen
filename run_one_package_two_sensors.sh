#!/usr/bin/bash
./pygatt.py tyresensor.json &
./reader.py tyresensor.json &
./pygatt.py accsensor.json &
./reader.py accsensor.json &
