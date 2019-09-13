# Motionoffon
Python script on motioneyeos to turn on/off motion detection by GPiO Pin [switch]
Whole idea of script is watching state of state GPiO pins and setting up a motion detection by localhost command
For cam nr 0:

Motion detection OFF = 'curl http://localhost:8080/0/detection/pause'

Motion detection ON = 'curl http://localhost:8080/0/detection/start'

In my case button is attached to pin 27 and GND on pin 25

You can add script to /data/etc/userinit.sh
a line:
python /data/etc/motionoffon.py&
