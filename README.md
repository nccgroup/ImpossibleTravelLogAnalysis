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

you will then see:
```
impossibletravel.py ..\Speed-of-light-test-data\sampledataexample.csv
[i] NCC Group Impossible Travel Analysis - 1.0
[i] https://github.com/nccgroup/ImpossibleTravelLogAnalysis
[!]  user621 had traveled on 2019-04-09 01:44:00 at speed 32909.547 m/s (118474.37 km/h) for 0.05 hrs
[!] user9406 had traveled on 2019-04-11 11:03:00 at speed 7376.450 m/s (26555.22 km/h) for 0.23 hrs
[!] user3027 had traveled on 2019-04-12 18:07:00 at speed 94516.879 m/s (340260.76 km/h) for 0.03 hrs
[!] user6995 had traveled on 2019-04-20 16:47:00 at speed 4718.706 m/s (16987.34 km/h) for 1.10 hrs
[!] user1566 had traveled on 2019-04-24 23:00:00 at speed 8512.756 m/s (30645.92 km/h) for 0.30 hrs
[!] user4090 had traveled on 2019-04-28 16:12:00 at speed 3640.331 m/s (13105.19 km/h) for 0.62 hrs
[!] user2577 had traveled on 2019-05-06 11:29:00 at speed 5441.884 m/s (19590.78 km/h) for 0.50 hrs
[!] user7743 had traveled on 2019-05-06 20:30:00 at speed 17065.947 m/s (61437.41 km/h) for 0.15 hrs
[!] user5822 had traveled on 2019-05-24 16:23:00 at speed 75868.560 m/s (273126.82 km/h) for 0.03 hrs
[!] user6431 had traveled on 2019-05-26 05:09:00 at speed 5722.403 m/s (20600.65 km/h) for 0.67 hrs
[!]   user56 had traveled on 2019-05-30 10:43:00 at speed 11834.590 m/s (42604.52 km/h) for 0.43 hrs
[!] user8663 had traveled on 2019-05-30 18:39:00 at speed 7466.536 m/s (26879.53 km/h) for 0.47 hrs
[!] user4256 had traveled on 2019-05-31 08:22:00 at speed 53195.909 m/s (191505.27 km/h) for 0.07 hrs
[!] user1528 had traveled on 2019-06-01 13:59:00 at speed 3645.914 m/s (13125.29 km/h) for 0.92 hrs
```

## Windows Binary Release
A version compiled with pyinstaller to a single .exe can be found on the Releases here:
https://github.com/nccgroup/ImpossibleTravelLogAnalysis/releases

This is used in the same way e.g.
```
..\output\impossibletravel.exe" ..\Speed-of-light-test-data\sampledataexample.csv
[i] NCC Group Impossible Travel Analysis - 1.0
[i] https://github.com/nccgroup/ImpossibleTravelLogAnalysis
[!]  user621 had traveled on 2019-04-09 01:44:00 at speed 32909.547 m/s (118474.37 km/h) for 0.05 hrs
[!] user9406 had traveled on 2019-04-11 11:03:00 at speed 7376.450 m/s (26555.22 km/h) for 0.23 hrs
[!] user3027 had traveled on 2019-04-12 18:07:00 at speed 94516.879 m/s (340260.76 km/h) for 0.03 hrs
[!] user6995 had traveled on 2019-04-20 16:47:00 at speed 4718.706 m/s (16987.34 km/h) for 1.10 hrs
[!] user1566 had traveled on 2019-04-24 23:00:00 at speed 8512.756 m/s (30645.92 km/h) for 0.30 hrs
```

## Requirements
* See requirements.txt
* The Maxmin GeoIP city database https://dev.maxmind.com/geoip/geoip2/geolite2/

## Author
Stephen van der Baan

## License
Released under AGPL - see LICENSE