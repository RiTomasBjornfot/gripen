#!/usr/bin/bash
./plotter.py unit1.json &
./writer.py unit1.json &
./reader.py unit1.json &
./pygatt.py unit1.json
