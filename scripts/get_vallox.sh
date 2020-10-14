#!/bin/sh

/usr/bin/python /etc/openhab2/scripts/get_vallox.py > /server/temp/kwl_data
chgrp openhab /server/temp/kwl_data

