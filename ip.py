import pygeoip
import sys

def short(ip):
	rec = gi.record_by_name(ip)
	city = rec['city']
	country = rec['country_code']
	print(str(city)+ ', '+str(country))

def long(ip):
	rec = gi.record_by_name(ip)
	city = rec['city']
	country = rec['country_name']
	longitude = rec['longitude']
	lat = rec['latitude']
	print('* Address: '  + ip)
	print('* ' + str(city)+ ', '+str(country))
	print('* Latitude: ' + str(lat) + ', Longitude: '+ str(longitude))

gi = pygeoip.GeoIP('GeoIP.dat')
ip = input("ip: ")

if len(sys.argv) == 1:
    short(ip)
    exit(0)
if sys.argv[1] == "-s":
    short(ip)
elif sys.argv[1] == "-l":
    long(ip)
# default
elif sys.argv[1] == "":
    short(ip)
else:
    print("fool")
    exit(1)
