import sys
from vallox_websocket_api import Client
from pprint import pprint


client = Client('192.168.178.26')
mode = str(sys.argv[1])
if mode == 'A_CYC_STATE':
	metrics = client.fetch_metrics(['A_CYC_STATE'])
elif mode == 'A_CYC_SUPP_FAN_SPEED':
	metrics = client.fetch_metrics(['A_CYC_SUPP_FAN_SPEED'])
elif mode == 'A_CYC_EXTR_FAN_SPEED':
	metrics = client.fetch_metrics(['A_CYC_EXTR_FAN_SPEED'])
elif mode == 'A_CYC_TEMP_EXTRACT_AIR':
	metrics = client.fetch_metrics(['A_CYC_TEMP_EXTRACT_AIR'])
elif mode == 'A_CYC_TEMP_EXHAUST_AIR':
	metrics = client.fetch_metrics(['A_CYC_TEMP_EXHAUST_AIR'])
elif mode == 'A_CYC_TEMP_OUTDOOR_AIR':
	metrics = client.fetch_metrics(['A_CYC_TEMP_OUTDOOR_AIR'])
elif mode == 'A_CYC_TEMP_SUPPLY_AIR':
	metrics = client.fetch_metrics(['A_CYC_TEMP_SUPPLY_AIR'])
elif mode == 'A_CYC_CELL_STATE':
	metrics = client.fetch_metrics(['A_CYC_CELL_STATE'])

pprint(metrics)
