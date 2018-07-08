#!/usr/bin/env python

#
# Wifi/Web driven Rover
import time
import serial
from flask import Flask, render_template, request

app = Flask (__name__, static_url_path = '')

# Connect to the comm port to talk to the Roboclaw motor controller
try:
   # Change the baud rate here if diffrent than 19200
   uno = serial.Serial('/dev/ttyUSB0', 9600)
except IOError:
   print("Comm port not found")
   sys.exit(0)

# Speed and drive control variables
last_direction = -1
speed_offset = 84
turn_tm_offset = 0.166
run_time = 0.750


# A little dwell for settling down time
time.sleep (3)

#
# URI handlers - all the bot page actions are done here
#

# Send out the bots control page (home page)
@app.route ("/")
def index ( ):
   return render_template ('index.html', name = None)

@app.route ("/forward")
def forward ( ):
   global last_direction, run_time

   print "Forward"
   go_forward ( )
   last_direction = 0

   # sleep 100ms + run_time
   time.sleep (0.100 + run_time)

   # If not continuous, then halt after delay
   if run_time > 0:
      last_direction = -1
      halt ( )

   return "ok"

@app.route ("/backward")
def backward ( ):
   global last_direction, run_time

   print "Backward"
   go_backward ( )
   last_direction = 1

   # sleep 100ms + run_time
   time.sleep (0.100 + run_time)

   # If not continuous, then halt after delay
   if run_time > 0:
      last_direction = -1
      halt ( )

   return "ok"

@app.route ("/left")
def left ( ):
   global last_direction, turn_tm_offset

   print "Left"
   go_left ( )
   last_direction = -1

   # sleep @1/2 second
   time.sleep (0.500 - turn_tm_offset)

   # stop
   halt ( )
   time.sleep (0.100)
   return "ok"

@app.route ("/right")
def right ( ):
   global last_direction, turn_tm_offset

   print "Right"
   go_right ( )

   # sleep @1/2 second
   time.sleep (0.500 - turn_tm_offset)
   last_direction = -1

   # stop
   halt ( )
   time.sleep (0.100)
   return "ok"

@app.route ("/ltforward")
def ltforward ( ):
   global last_direction, turn_tm_offset

   print "Left forward turn"
   go_left ( )

   # sleep @1/8 second
   time.sleep (0.250 - (turn_tm_offset / 2))
   last_direction = -1

   # stop
   halt ( )
   time.sleep (0.100)
   return "ok"

@app.route ("/rtforward")
def rtforward ( ):
   global last_direction, turn_tm_offset

   print "Right forward turn"
   go_right ( )

   # sleep @1/8 second
   time.sleep (0.250 - (turn_tm_offset / 2))
   last_direction = -1

   # stop
   halt ( )
   time.sleep (0.100)
   return "ok"

@app.route ("/stop")
def stop ( ):
   global last_direction

   print "Stop"
   halt ( )
   last_direction = -1

   # sleep 100ms
   time.sleep (0.100)
   return "ok"

@app.route ("/panlt")
def panlf ( ):
   global servo_pos

   uno.write('w')

   # sleep 150ms
   time.sleep (0.150)
   return "ok"

@app.route ("/panrt")
def panrt ( ):
   global servo_pos

   uno.write('q')

   # sleep 150ms
   time.sleep (0.150)
   return "ok"

@app.route ("/home")
def home ( ):
   global servo_pos

   print "Home"
   servo_pos = 1250

   servo.set_servo (18, servo_pos)

   # sleep 150ms
   time.sleep (0.150)
   return "ok"

@app.route ("/panfull_lt")
def panfull_lt ( ):
   global servo_pos

   uno.write('z')

   # sleep 150ms
   time.sleep (0.150)
   return "ok"

@app.route ("/panfull_rt")
def panfull_rt ( ):
   global servo_pos

   uno.write('a')

   # sleep 150ms
   time.sleep (0.150)
   return "ok"

@app.route ("/speed_low")
def speed_low ( ):
   global speed_offset, last_direction, turn_tm_offset

   uno.write('p')

   # sleep 150ms
   time.sleep (0.150)
   return "ok"

@app.route ("/speed_mid")
def speed_mid ( ):
   global speed_offset, last_direction, turn_tm_offset

   uno.write('o')

   # sleep 150ms
   time.sleep (0.150)
   return "ok"

@app.route ("/speed_hi")
def speed_hi ( ):
   global speed_offset, last_direction, turn_tm_offset

   uno.write('i')

   # sleep 150ms
   time.sleep (0.150)
   return "ok"

@app.route ("/continuous")
def continuous ( ):
   global run_time

   print "Continuous run"
   run_time = 0

   # sleep 100ms
   time.sleep (0.100)
   return "ok"

@app.route ("/mid_run")
def mid_run ( ):
   global run_time

   print "Mid run"
   run_time = 0.750
   halt ( )

   # sleep 100ms
   time.sleep (0.100)
   return "ok"

@app.route ("/short_time")
def short_time ( ):
   global run_time

   print "Short run"
   run_time = 0.300
   halt ( )

   # sleep 100ms
   time.sleep (0.100)
   return "ok"

#
# Motor drive functions
#
def go_forward():
	uno.write('1')

def go_backward():
	uno.write('4')

def go_left():
    global speed_offset
    uno.write('2')

def go_right():
    global speed_offset
    uno.write('3')


def halt():
    uno.write('s')

if __name__ == "__main__" :
   app.run (host = '0.0.0.0', port = 80, debug = True)
