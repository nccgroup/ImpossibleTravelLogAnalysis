#
# (c)2019 NCC Group Plc
# Steven van der Baan
# Released under AGPL
# https://github.com/nccgroup/ImpossibleTravelLogAnalysis
#

import csv
import os
import sys
from datetime import datetime

import click
import geoip2.database
from geopy import distance

FMT = '%Y-%m-%d %H:%M:%S'


def ip2location(citydb, address):
    try:
        loc = citydb.city(address)
        lat = loc.location.latitude
        lon = loc.location.longitude
        return (lat, lon)
    except:
        return 'unknown'


@click.command(context_settings={'help_option_names': ['-h', '--help'],
                                 })
@click.option('-v', '--verbose / --no-verbose', default=False, help="Show more info")
@click.option('-s','--max-speed',default=3600, help="Threshold for speeding detection in m/s, default=3600 (1000 km/h)")
@click.argument('csvfile', type=click.File('r'))

def main(verbose, max_speed, csvfile, ):

	
    users = {}

    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'geolite2DB')
    if not os.path.exists(dir_path + '/GeoLite2-City.mmdb'):
        print("[!] Ensure that the GeoLite2-City.mmdb exists in %s from https://dev.maxmind.com/geoip/geoip2/geolite2/" % (dir_path))
        sys.exit(1)

    citydb = geoip2.database.Reader(dir_path + '/GeoLite2-City.mmdb')
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        user = row['User']
        iploc = ip2location(citydb, row['IP'])
        location = {'IP': row['IP'], 'geo': iploc}

        if user in users:
            oldIp = users[user]['location']['IP']
            oldTime = users[user]['time']
            time = abs((datetime.strptime(row['When'], FMT) - datetime.strptime(oldTime, FMT)).total_seconds())
            if time == 0:
                time = 1
            if iploc != 'unknown' and users[user]['location']['geo'] != 'unknown':
                dist = distance.distance(iploc, users[user]['location']['geo']).meters
                speed = dist / time
                if speed > max_speed:  # 1000 Km/h
                    print('[!] %8s had traveled on %s at speed %06.3f m/s (%06.2f km/h) for %03.2f hrs' % (user, row['When'], speed, speed * 3.6,time / 3600))
                elif verbose:
                    print('[!] %8s had traveled on %s at speed %06.3f m/s (%06.2f km/h) for %03.2f hrs' % (user, row['When'], speed, speed * 3.6,time / 3600))
            else:
                if verbose:
                    print('%s traveled from %s to %s in % hrs' % (user, oldIp, row['IP'], time / 3600))
        users[user] = {'time': row['When'], 'location': location}


if __name__ == '__main__':
	print("[i] NCC Group Impossible Travel Analysis - 1.0")
	print("[i] https://github.com/nccgroup/ImpossibleTravelLogAnalysis")
    
	main()
