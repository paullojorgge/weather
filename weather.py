#!/usr/bin/python

# My first Python test
# weather.py - ask for a city and display the actual temperature

# Modules
import urllib2
import json
import nltk
import re
import os, sys
from urllib import urlopen

city = raw_input("Insert a city: ")
url = urllib2.urlopen("http://www.timeanddate.com/weather")
hour = url.info()['date'] # get the time of the query
html = url.read()  # get all data
raw = nltk.clean_html(html) # clean the data
#res2 = re.search('(?<=Paris )(.{17})', raw).group() # info by city
res = re.search('(?<=' + re.escape(city) + ')(.{50})', raw) # info by city
data = res.group().split() # convert res to a list
temp = int(float(data[4])) # convert temperature to number
temperature = round(float(temp-32)/9*5,2)
#print temperature
#print data
#print res2
print "##############################"
print "City:", city
print "Time:", data[1], data[2], data[3]
print "Temperature(Celsius):", temperature #, unichr(186), "C"
print "Temperature(Fahrenheit):", temp

 
