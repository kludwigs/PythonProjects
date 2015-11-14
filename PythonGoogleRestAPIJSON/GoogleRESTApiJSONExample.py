import urllib2
import json


__author__ = 'Karl'
rest_url = 'http://maps.googleapis.com/maps/api/geocode/json?address=chicago&sensor=false'

if __name__ == "__main__":
        req = urllib2.Request(rest_url)
        opener = urllib2.build_opener()
        f = opener.open(req)
        jsoninfo = json.load(f)
        # traverse google APIs JSON array to find the city's latitude and longtitude
        #print latitude and longtitude
        try:
            location = jsoninfo.get('results')[0].get('geometry').get('location')
            city_name = jsoninfo.get('results')[0].get('address_components')[0].get('long_name')
            print city_name,"'s coordinates are:"
            print "latitude = ", location['lat']
            print "longtitude = ", location['lng']
        except:
            print "Couldn't locate requested items"
