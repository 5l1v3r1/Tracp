#!/usr/bin/python
#$$$$$$$$$$$$$$$$

#>>>>{> Welcome <}<<<<#
#--------------------------------
#[>] SCRIPT{> Tracp             #
#[>] Job{> GET TARGET GEOIP INFO#
#[>] CodedBy{> Oseid Aldary #####
#############################
# LIBRARIES #
import optparse,socket,json,urllib2;from time import sleep; from sys import platform as useros
# COLORS #
if useros =="linux" or useros =="linux2":
 rd = "\033[1;31m"
 gr = "\033[1;32m"
 yl = "\033[1;33m"
 pu = "\033[1;35m"
 cy = "\033[1;36m"
 wi = "\033[1;37m"
else:
 rd = ""
 gr = ""
 yl = ""
 pu = ""
 cy = ""
 wi = ""
#################

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
                           reponse = urllib2.urlopen(url + str(t) )
                           name = reponse.read()
                           labs = json.loads(name)
                           theip = labs['query']
                           print(gr+"\n["+yl+str(loop)+gr+"] Get GeoIP Info About TARGET[ "+rd+str(theip)+gr+" ] ...Wait")
			   loop +=1
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
                            reponse = urllib2.urlopen(url + str(t) )
                            name = reponse.read()
                            labs = json.loads(name)
                            theip = labs['query']
                            print(gr+"\n["+yl+str(loop)+gr+"] Get GeoIP Info About TARGET[ "+rd+str(theip)+gr+" ] ...Wait")
			    loop +=1
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
                            reponse = urllib2.urlopen(url + str(tar) )
                            name = reponse.read()
                            labs = json.loads(name)
			    theip = labs['query']
                            print(gr+"\n["+wi+"#"+gr+"] Get GeoIP Info About TARGET[ "+rd+str(theip)+gr+" ] ...Wait")
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

