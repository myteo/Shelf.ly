import serial
import time
import requests
import json
firebase_url = 'https://consumerapp-3051e.firebaseio.com/'
#Connect to Serial Port for communication
ser = serial.Serial('COM3', 9600, timeout=0)
#Setup a loop to send led values at fixed intervals
#in seconds
fixed_interval = 3
while 1:
  try:
    #led value obtained from Arduino + PIRSensor          
    led_val = ser.readline()
    print('time: ' + str(time.time()) + ', v: ' + led_val)
    if led_val[:3] == 'LOW':
      print('sending')
      data = {'shelfly': 1}
      result = requests.put(firebase_url+'hasLowStocks.json', data=json.dumps(data))
      print('Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text)
    time.sleep(fixed_interval)
  except IOError:
    print('Error! Something went wrong.')
  time.sleep(fixed_interval)
