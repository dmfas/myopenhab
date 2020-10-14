import sys
from vallox_websocket_api import Client

client = Client('192.168.178.26')
args=len(sys.argv)
mode = int(sys.argv[1])
if args >= 3:
	duration = int(sys.argv[2])

if mode == 0:
	client.set_values({'A_CYC_BOOST_TIMER': str(0)})
	client.set_values({'A_CYC_STATE': 'C_CYC_STATE_HOME'})
#	print "setting mode home."
	print "0"
elif mode == 1:
	client.set_values({'A_CYC_BOOST_TIMER': str(0)})
	client.set_values({'A_CYC_STATE': 'C_CYC_STATE_AWAY'})
#	print "setting mode away."
	print "1"
elif mode == 2:
	client.set_values({'A_CYC_BOOST_TIMER': str(duration)})
#	print "boosting for " + str(duration) + " minutes."
	print "2"
elif mode == 5:
	client.set_values({'A_CYC_MODE': '5'})
#	print "Turning off."
	print "5"


