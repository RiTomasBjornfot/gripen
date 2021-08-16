#!/usr/bin/bash
./plotter.py unit2.json &
./writer.py unit2.json &
./reader.py unit2.json &
./pygatt.py unit2.json
