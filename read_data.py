import serial, requests
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

while True:	
	# r = requests.post('http://hackmit-spot.herokuapp.com/availability_data', data={'availability':ser.readline()[0]})
	r = requests.post('http://127.0.0.1:5000/temp_data', data={'degrees_f':ser.readline()})
	print r.text