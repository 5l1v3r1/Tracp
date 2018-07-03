#!/usr/bin/python
#[SCRIPT]: Tracp
#[JOB]: Trace IP Address And Get GeoIP Info
#[CodedBy]: Oseid Aldary

## Libraries
from sys import argv,stdout;from copy import copy; import json,urllib2,socket
from time import sleep

## Colors
rd = "\033[1;31m"
gr = "\033[1;32m"
yl = "\033[1;33m"
bl = "\033[1;34m"
pu = "\033[1;35m"
cy = "\033[1;36m"
wi = "\033[1;37m"

## Slow Motion Print
def pprint(text):
   for c in text + "\n":
    stdout.write(c)
    stdout.flush()
    sleep(3./140)

## Check Internet Connection
server = "www.google.com"
def check():
  try:
     IP = socket.gethostbyname(server)
     con = socket.create_connection((IP, 80), 2)
     return True
  except:
	pass
  return False
checker = check()
##

## Script Founctions

def single_scan(ip):
 if checker ==True:
  try:
	   url = "http://ip-api.com/json/"
           reponse = urllib2.urlopen(url + str(ip) )
           name = reponse.read()
           labs = json.loads(name)
	   theip = labs['query']
           if ip ==" ":
             pprint(gr+"\n["+wi+"#"+gr+"] Get GeoIP Info About Your IP[ "+wi+str(theip)+gr+" ] ...Wait")
           else:
             pprint(gr+"\n["+wi+"#"+gr+"] Get GeoIP Info About TARGET[ "+rd+str(ip)+gr+" ] ...Wait")
	   test = labs['regionName']
           print(rd+"INFO"+gr+":["+wi+str(theip)+gr+"]===:")
	   sleep(0.10)
           print(gr + "\t\t IP: " +wi+theip)
	   sleep(0.10)
           print(gr+ "\t\t Status: " +wi+ labs['status'])
           sleep(0.10)
           print(gr+ "\t\t Region: " +wi+ test)
           sleep(0.10)
           print(gr + "\t\t Country: " +wi+ labs['country'])
           sleep(0.10)
           print(gr + "\t\t City: " +wi+ labs['city'])
           sleep(0.10)
           print(gr + "\t\t ISP: "+wi + labs['isp'])
           sleep(0.10)
           print(gr + "\t\t Lat,Lon: "+wi + str(labs['lat']) + "," + str(labs['lon']))
           sleep(0.10)
           print(gr + "\t\t ZIPCODE: "+wi + labs['zip'])
           sleep(0.10)
           print(gr + "\t\t TimeZone: " +wi+ labs['timezone'])
           sleep(0.10)
           print(gr + "\t\t AS: " +wi+ labs['as'])
           sleep(0.10)
           print(pu+"===============================\n"+wi)
  except:
	pprint(yl+"\n["+rd+"!"+yl+"] Error: Please Check IP Addr Or Choice Other IP Addr")
	exit(1)
 else:
     pprint(rd+"["+yl+"!"+rd+"]"+yl+" Please Check Your Internet Connection "+rd+"!!!")
     exit(1)

def many_scan(ip2):
 if checker ==True:
        i = ip2.strip()
	try:
	   url = "http://ip-api.com/json/"
           reponse = urllib2.urlopen(url + str(i) )
           name = reponse.read()
           labs = json.loads(name)
	   theip = labs['query']
           pprint(gr+"\n["+wi+"#"+gr+"] Get GeoIP Info About TARGET[ "+rd+str(i)+gr+" ] ......Wait")
	   test = labs['regionName']
           print(rd+"INFO"+gr+":["+wi+str(theip)+gr+"]===:")
	   sleep(0.10)
           print(gr + "\t\t IP: " +wi+theip)
	   sleep(0.10)
           print(gr+ "\t\t Status: " +wi+ labs['status'])
           sleep(0.10)
           print(gr+ "\t\t Region: " +wi+ test)
           sleep(0.10)
           print(gr + "\t\t Country: " +wi+ labs['country'])
           sleep(0.10)
           print(gr + "\t\t City: " +wi+ labs['city'])
           sleep(0.10)
           print(gr + "\t\t ISP: "+wi + labs['isp'])
           sleep(0.10)
           print(gr + "\t\t Lat,Lon: "+wi + str(labs['lat']) + "," + str(labs['lon']))
           sleep(0.10)
           print(gr + "\t\t ZIPCODE: "+wi + labs['zip'])
           sleep(0.10)
           print(gr + "\t\t TimeZone: " +wi+ labs['timezone'])
           sleep(0.10)
           print(gr + "\t\t AS: " +wi+ labs['as'])
           sleep(0.10)
           print(pu+"===============================\n"+wi)
        except KeyboardInterrupt:
	    pprint(rd+"\n["+yl+"CTRL+C"+rd+"]"+yl+" Exiting.....\n")
	    exit(1)
        except:
	     pprint(yl+"\n["+rd+"!"+yl+"] No GeoIP Info Found About This Target["+rd+i+yl+"]!\n")
 else:
     pprint(rd+"["+yl+"!"+rd+"]"+yl+" Please Check Your Internet Connection "+rd+"!!!")
     exit(1)
## Help Msg
if len(argv) !=2:
	pprint(gr+"\n[~]-[===="+wi+" GEOIP INFO FINDER "+gr+"===]-[~]")
	pprint(gr+"[~][====By{>"+wi+" Oseid Aldary"+gr+" <} ===][~]\n")
        print(wi+"Usage: python Tracp.py <1 OR 2>\n\t1: For Single Scan   ::> [Single IP Addr Scan]\n\t2: For Scan From IPs File   ::> [Many IPs Addr Scan]")
        exit(1)

ask = argv[1]
if ask =="1":
	print("\n[>] Press Enter Without Set IP For Show Info About You GeoIP INFO :)\n")
	ip = raw_input(gr+"\n[@]"+wi+" Enter SingleIP|> ")
        if ip =="":
	    single_scan(" ")
	else:
	   single_scan(ip)
elif ask =="2":
        try:
	 thefile = raw_input(gr+"["+wi+"@"+gr+"]"+wi+"Enter IPs File{> ")
         while thefile =="" or thefile is None:
		 thefile = raw_input(gr+"!["+wi+"@"+gr+"]"+wi+"Enter IPs File{?> ")
        except KeyboardInterrupt:
			print(" ")
			exit(1)
	try:
           test = open(thefile, 'r')
        except:
	  pprint(yl+"["+rd+"!"+yl+"] No Such File: "+wi+str(thefile))
	  exit(1)
        for ip2 in test:
            if not ip2:
		print("Nothing Into Ths File !!")
		break
            many_scan(ip2)
else:
   print(wi+"Usage: python Tracp.py <1 OR 2>\n\t1: For Single Scan   ::> [Single IP Addr Scan]\n\t2: For Scan From IPs File   ::> [Many IPs Addr Scan]")
   print(wi+"\nNo Such Option: "+rd+ask)

##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
