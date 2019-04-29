# Impossible Travel Log Analysis by NCC Group

## About
Basic log analysis tool to detect impossible travel via IP address geographic information

## Expected Data Format
A CSV file with the following headers
```
When,User,Event,IP
```

With the following format
```
2019-04-09 00:00:00,user2493,AUTHSUCCESS,101.193.251.145
```

Where the fields as structured as follows:
* **When** is YYYY-MM-DD HH:MMM:SSS
* **User** is the username
* **Event** is an authentication or other event you care about (only one type per .csv supported at the moment)
* **IP** is an IPv4 address

A script to generate test data along with an example .csv can be found here:
https://github.com/olliencc/Speed-of-light-test-data

## Usage
```
impossibletravel.py [csvfile]
```

e.g.
```
impossibletravel.py ..\Speed-of-light-test-data\sampledataexample.csv
```

## Requirements
* See requirements.txt
* The Maxmin GeoIP city database https://dev.maxmind.com/geoip/geoip2/geolite2/

## Author
Stephen van der Baan

## License
Released under AGPL - see LICENSE