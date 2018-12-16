#!/usr/bin/python
# -*- coding: UTF-8 -*-

#>>>>{> Welcome <}<<<<#
#--------------------------------
#[>] SCRIPT{> Tracp             #
#[>] Job{> GET TARGET GEOIP INFO#
#[>] CodedBy{> Oseid Aldary #####
#############################
# LIBRARIES #
import optparse,socket,json,urllib2;from time import sleep; from os import system as sy
sy("cls||clear")

# COLORS ##################
rd = "\033[1;31m" #>Red   #
gr = "\033[1;32m" #>Green #
yl = "\033[1;33m" #>Yallow#
pu = "\033[1;35m" #>Purple#
cy = "\033[1;36m" #>Cyan  #
wi = "\033[1;37m" #>>White#
###########################

# Check Internet Connection #
server = "www.google.com"
def check():
  try:
     ip = socket.gethostbyname(server)
     con = socket.create_connection((ip, 80), 2)
     return True
  except:
	pass
  return False
check = check()

parse = optparse.OptionParser(wi+"""
Usage:
======
     python Tracp.py -t <TARGET IP>-[OR]-<Many Targets IPs>+[OR]+<File Of Targets IPs>
---------------------------------------------------------------------------------------
Examples:
=========
     1-[Scan Single IP]=> python Tracp.py -t 192.95.39.46
     2-[Scan Many Ips]=> python Tracp.py -t 192.95.39.46,192.95.39.46,etc
     3-[Scan From File]=> python Tracp.py -t IPs.txt
----------------------------------------------------------------------------------------
""",version='2.5')
def Main():
   parse.add_option('-t','-T','--target','--TARGET',dest="tar",type="string")
   (options,args) = parse.parse_args()
   if options.tar !=None:
	tar = options.tar
	if check == True:
		if ',' in tar:
		  targets = tar.split(',')
		  loop = 1
                  ss = []
                  ff = []
		  for t in targets:
			t = t.strip()
			try:
                           url = "http://ip-api.com/json/"
                           response = urllib2.urlopen(url + str(t) )
                           name = response.read()
                           labs = json.loads(name)
                           theip = labs['query'].encode('ascii','replace')
                           print(gr+"\n["+yl+str(loop)+gr+"] Get GeoIP Info About TARGET[ "+rd+str(theip)+gr+" ] ...Wait")
			   loop +=1
	                   test = labs['regionName'].encode('ascii','replace')
                           print(rd+"INFO"+gr+":["+wi+str(theip).encode('ascii','replace')+gr+"]===:")
	                   sleep(0.10)
                           print(gr + "\t\t IP: " +wi+theip.encode('ascii','replace'))
	                   sleep(0.10)
                           print(gr+ "\t\t Status: " +wi+ labs['status'].encode('ascii','replace'))
                           sleep(0.10)
                           print(gr+ "\t\t Region: " +wi+ test.encode('ascii','replace'))
                           sleep(0.10)
                           print(gr + "\t\t Country: " +wi+ labs['country'].encode('ascii','replace'))
                           sleep(0.10)
                           print(gr + "\t\t City: " +wi+ labs['city'].encode('ascii','replace'))
                           sleep(0.10)
                           print(gr + "\t\t ISP: "+wi + labs['isp'].encode('ascii','replace'))
                           sleep(0.10)
                           print(gr + "\t\t Lat,Lon: "+wi + str(labs['lat']).encode('ascii','replace') + "," + str(labs['lon']).encode('ascii','replace'))
                           sleep(0.10)
                           print(gr + "\t\t ZIPCODE: "+wi + labs['zip'].encode('ascii','replace'))
                           sleep(0.10)
                           print(gr + "\t\t TimeZone: " +wi+ labs['timezone'].encode('ascii','replace'))
                           sleep(0.10)
                           print(gr + "\t\t AS: " +wi+ labs['as'].encode('ascii','replace'))
                           sleep(0.10)
                           print(pu+"===============================\n"+wi)
			   ss.append(1)
                        except KeyboardInterrupt:
                                print(rd+"\n["+yl+"CTRL+C"+rd+"]"+yl+" Exiting.....\n")
                                break
			except:
			   print(yl+"\n["+rd+"!"+yl+"] No GeoIP Info Found About This Target["+rd+t+yl+"]!")
			   print(rd+"========================== "+yl+"!!!"+rd+" ============================")
			   ff.append(1)
		  print(wi+"\n[#] Done :)")
		  if len(ss) > 0:
	       	   print(gr+"["+wi+str(len(ss))+gr+"]"+wi+" Targets successfully Found GeoIP Info About Him")
		  if len(ff) > 0:
	 	   print(yl+"["+rd+str(len(ff))+yl+"] Target Filed To Get GeoIP Info About Him "+rd+"!!!")
		  exit(1)
		try:
		   targets = open(tar, 'r')
		   res = True
		except:
		   res = False
		if res == True:
			loop = 1
			ss = []
			ff = []
			for t in targets:
			   t = t.strip()
			   try:
                            url = "http://ip-api.com/json/"
                            response = urllib2.urlopen(url + str(t) )
                            name = response.read()
                            labs = json.loads(name)
                            theip = labs['query'].encode('ascii','replace')
                            print(gr+"\n["+yl+str(loop)+gr+"] Get GeoIP Info About TARGET[ "+rd+str(theip)+gr+" ] ...Wait")
			    loop +=1
	                    test = labs['regionName'].encode('ascii','replace')
                            print(rd+"INFO"+gr+":["+wi+str(theip)+gr+"]===:")
	                    sleep(0.10)
                            print(gr + "\t\t IP: " +wi+theip.encode('ascii','replace'))
	                    sleep(0.10)
                            print(gr+ "\t\t Status: " +wi+ labs['status'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr+ "\t\t Region: " +wi+ test.encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t Country: " +wi+ labs['country'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t City: " +wi+ labs['city'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t ISP: "+wi + labs['isp'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t Lat,Lon: "+wi + str(labs['lat']).encode('ascii','replace') + "," + str(labs['lon']).encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t ZIPCODE: "+wi + labs['zip'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t TimeZone: " +wi+ labs['timezone'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t AS: " +wi+ labs['as'].encode('ascii','replace'))
                            sleep(0.10)
                            print(pu+"===============================\n"+wi)
			    ss.append(1)
			   except KeyboardInterrupt:
                                print(rd+"\n["+yl+"CTRL+C"+rd+"]"+yl+" Exiting.....\n")
                                break
			   except:
			       print(yl+"\n["+rd+"!"+yl+"] No GeoIP Info Found About This Target["+rd+t+yl+"]!")
			       print(rd+"========================== "+yl+"!!!"+rd+" ============================")
			       ff.append(1)
                        print(wi+"\n[#] Done :)")
			if len(ss) > 0:
				print(gr+"["+wi+str(len(ss))+gr+"]"+wi+" Targets successfully Found GeoIP Info About Him")
			if len(ff) > 0:
				print(yl+"["+rd+str(len(ff))+yl+"] Target Filed To Get GeoIP Info About Him "+rd+"!!!")
		else:
			   try:
                            url = "http://ip-api.com/json/"
                            response = urllib2.urlopen(url + str(tar) )
                            name = response.read()
                            labs = json.loads(name)
			    theip = labs['query'].encode('ascii','replace')
                            print(gr+"\n["+wi+"#"+gr+"] Get GeoIP Info About TARGET[ "+rd+str(theip)+gr+" ] ...Wait")
	                    test = labs['regionName'].encode('ascii','replace')
                            print(rd+"INFO"+gr+":["+wi+str(theip).encode('ascii','replace')+gr+"]===:")
	                    sleep(0.10)
                            print(gr + "\t\t IP: " +wi+theip.encode('ascii','replace'))
	                    sleep(0.10)
                            print(gr+ "\t\t Status: " +wi+ labs['status'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr+ "\t\t Region: " +wi+ test.encode('ascii','replace')) 
                            sleep(0.10)
                            print(gr + "\t\t Country: " +wi+ labs['country'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t City: " +wi+ labs['city'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t ISP: "+wi + labs['isp'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t Lat,Lon: "+wi + str(labs['lat']).encode('ascii','replace') + "," + str(labs['lon']).encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t ZIPCODE: "+wi + labs['zip'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t TimeZone: " +wi+ labs['timezone'].encode('ascii','replace'))
                            sleep(0.10)
                            print(gr + "\t\t AS: " +wi+ labs['as'].encode('ascii','replace'))
                            sleep(0.10)
                            print(pu+"===============================\n"+wi)
			   except KeyboardInterrupt:
                                print(rd+"\n["+yl+"CTRL+C"+rd+"]"+yl+" Exiting.....\n")
                                exit(1)
			   except:
			       print(yl+"\n["+rd+"!"+yl+"] No GeoIP Info Found About This Target["+rd+tar+yl+"]!\n")
			   print("[#] Done :)")
	else:
		print(rd+"["+yl+"!"+rd+"]"+yl+" Please Check Your Internet Connection "+rd+"!!!")
		exit(1)
   else:
	print(parse.usage)
	exit(1)
if __name__=="__main__":
	Main()
##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
