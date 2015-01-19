#!/usr/bin/python

import json, urllib
from pylab import *
import time, datetime



def graphdata(source):
   url = "https://localdata-sensors.herokuapp.com/api/sources/ci4lr75vd000b02ypdlm6qbly/entries?startIndex=0&count=1000000"
   filename="sensordata.txt"

   # Local vars
   time_format = "%Y-%m-%dT%H:%M:%S.000Z"

   # Get data depending on source: web or file
   if source=="web":
      print "Getting data from web"
      sensordata = urllib.urlopen(url).read()
   else:
      print "Getting data from local file"
      sensordatafile = open(filename, "r")
      sensordata = sensordatafile.readline()


   tstampdata = eval(sensordata)

   
   list_ts = []
   list_sound = []
   list_airqual_r = []
   list_dust = []
   list_light = []
   list_temp = []
   list_airqual = []
   list_humidity = []
   for i in tstampdata:
      # {'sound': 1908, 'location': [6.13995, 46.220411], 'airquality_raw': 26, 'dust': -1, 'light': 14, 'uv': 301.82, 'temperature': 25.6, 'airquality': 'WarmUp', 'humidity': 48.5}
#      print i['timestamp']
#      print i['data']['sound']
#      print i['data']['location']
#      print i['data']['airquality_raw']
#      print i['data']['dust']
#      print i['data']['light']
#      print i['data']['temperature']
#      print i['data']['airquality']
#      print i['data']['humidity']
      ts = time.mktime(time.strptime(i['timestamp'], time_format))
      list_ts.append(ts)
      list_sound.append(i['data']['sound'])
      list_airqual_r.append(i['data']['airquality_raw'])
      list_dust.append(i['data']['dust'])
      list_light.append(i['data']['light'])
      list_temp.append(i['data']['temperature'])
      list_airqual.append(i['data']['airquality'])
      list_humidity.append(i['data']['humidity'])
   # Show temp
   plot(list_ts, list_temp) 
   xlabel('time (s)')
   ylabel('temperature')
   title('Temperature')
   grid(True)
   show()
   # Show sound
   plot(list_ts, list_sound) 
   xlabel('time (s)')
   ylabel('sound')
   title('Sound')
   grid(True)
   show()
   # Show air quality raw
   plot(list_ts, list_airqual_r) 
   xlabel('time (s)')
   ylabel('air quality raw')
   title('Air quality raw')
   grid(True)
   show()
   # Show dust
   plot(list_ts, list_dust) 
   xlabel('time (s)')
   ylabel('dust')
   title('Dust')
   grid(True)
   show()
   # Show dust
   plot(list_ts, list_humidity) 
   xlabel('time (s)')
   ylabel('humidity')
   title('Humidity')
   grid(True)
   show()



# Main
#graphdata("local")
graphdata("web")
