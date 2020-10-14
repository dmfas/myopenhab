#!/usr/bin/python

import sys
from shutil import copyfile
from vallox_websocket_api import Client
from pprint import pprint

src='/volatile/expendable/temp/kwl_data_new'
dst='/volatile/expendable/temp/kwl_data'

outfile = open(src, 'w+')
client = Client('192.168.178.26')
metrics = client.fetch_metrics([
		'A_CYC_STATE',
		'A_CYC_SUPP_FAN_SPEED',
		'A_CYC_EXTR_FAN_SPEED',
		'A_CYC_TEMP_EXTRACT_AIR',
		'A_CYC_TEMP_EXHAUST_AIR',
		'A_CYC_TEMP_OUTDOOR_AIR',
		'A_CYC_TEMP_SUPPLY_AIR',
		'A_CYC_CELL_STATE',
		'A_CYC_RH_VALUE'
		])

pprint(metrics, stream=outfile)
outfile.close()

copyfile(src, dst)

