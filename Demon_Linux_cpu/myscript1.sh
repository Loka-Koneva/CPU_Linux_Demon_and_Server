#!/bin/bash

while true; do
mpstat 1 1|tail -n 1|awk '{print 100 - $12}' > cpu_data.txt
sleep 10;
done
