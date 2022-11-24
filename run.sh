#!/bin/bash

cd /root/nmcrop
pip3 install .
cd /

pytest --pyargs nmcrop

python3 -m nmcrop
