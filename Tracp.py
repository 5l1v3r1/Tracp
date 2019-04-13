#!/usr/bin/python
#$$$$$$$$$$$$$$$$
# -*- coding: UTF-8 -*-

#>>>>{> Welcome <}<<<<#
#--------------------------------
#[>] SCRIPT{> Tracp             #
#[>] Job{> GET TARGET GEOIP INFO#
#[>] CodedBy{> Oseid Aldary #####
#############################
# LIBRARIES #
import optparse,socket,json,urllib2;from time import sleep; from os import system as sy,path
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
def check():
  try:
     ip = socket.gethostbyname("google.com")
     con = socket.create_connection((ip, 80), 2)
     return True
  except socket.error:
    pass
  return False
check = check()
ff=0
def getinfo(ip,slp=True):
  url = "http://ip-api.com/json/"
  response = urllib2.urlopen(url +str(ip)).read()
  labs = json.loads(response)
  try:
    info = [
    labs['query'].encode('ascii','replace'),
    labs['status'].encode('ascii','replace'),
    labs['regionName'].encode('ascii','replace'),
    labs['country'].encode('ascii','replace'),
    labs['city'].encode('ascii','replace'),
    labs['isp'].encode('ascii','replace'),
    str(labs['lat']).encode('ascii','replace') + "," + str(labs['lon']).encode('ascii','replace'),
    labs['zip'].encode('ascii','replace'),
    labs['timezone'].encode('ascii','replace'),
    labs['as'].encode('ascii','replace')
    ]
    print(rd+"INFO"+gr+":["+wi+info[0]+gr+"]===:")
    if slp==True:
      sleep(0.10)
      print(gr + "\t\t IP: " +wi+info[0])
      sleep(0.10)
      print(gr+ "\t\t Status: " +wi+info[1])
      sleep(0.10)
      print(gr+ "\t\t Region: " +wi+ info[2])
      sleep(0.10)
      print(gr + "\t\t Country: " +wi+ info[3])
      sleep(0.10)
      print(gr + "\t\t City: " +wi+ info[4])
      sleep(0.10)
      print(gr + "\t\t ISP: "+wi + info[5])
      sleep(0.10)
      print(gr + "\t\t Lat,Lon: "+wi+ info[6])
      sleep(0.10)
      print(gr + "\t\t ZIPCODE: "+wi + info[7])
      sleep(0.10)
      print(gr + "\t\t TimeZone: " +wi+ info[8])
      sleep(0.10)
      print(gr + "\t\t AS: " +wi+ info[9])
      sleep(0.10)
    else:
      print(gr + "\t\t IP: " +wi+info[0])
      print(gr+ "\t\t Status: " +wi+info[1])
      print(gr+ "\t\t Region: " +wi+ info[2])
      print(gr + "\t\t Country: " +wi+ info[3])
      print(gr + "\t\t City: " +wi+ info[4])
      print(gr + "\t\t ISP: "+wi + info[5])
      print(gr + "\t\t Lat,Lon: "+wi+ info[6])
      print(gr + "\t\t ZIPCODE: "+wi + info[7])
      print(gr + "\t\t TimeZone: " +wi+ info[8])
      print(gr + "\t\t AS: " +wi+ info[9])
    print(pu+"===============================\n"+wi)
  except Exception:
    if slp==True:
      print(yl+"["+rd+"-"+yl+"]"+rd+" Target: "+yl+ip)
      sleep(0.10)
      print(yl+"  ["+rd+"!"+yl+"]"+rd+" Something Went Wrong"+yl+" !!!")
      sleep(0.10)
      print(yl+"  ["+rd+"!"+yl+"] "+wi+"Show This GeoIP INFO For This IP Here[ "+gr+"https://whatismyipaddress.com/ip/"+str(ip)+wi+" ]")
      sleep(0.10)
    else:
      print(yl+"["+rd+"-"+yl+"]"+rd+" Target: "+yl+ip)
      print(yl+"  ["+rd+"!"+yl+"]"+rd+" Something Went Wrong"+yl+" !!!")
      print(yl+"  ["+rd+"!"+yl+"] "+wi+"Show This GeoIP INFO For This IP Here[ "+gr+"https://whatismyipaddress.com/ip/"+str(ip)+wi+" ]")      
    print(rd+"===============================\n"+wi)
    global ff
    ff+=1
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
---------------------------------------------------------------------------------------
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
        ss = 0
        abro = 0
        slp = False if len(targets) >=8  else True
        for t in targets:
          if not t.strip(): continue
          t = t.strip()
          try:
            getinfo(t,slp=slp)
            ss+=1
          except(KeyboardInterrupt,EOFError):
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting....\n"+wi)
            abro = 1
            break
        if abro == 0:
          print(wi+"\n[#] Done :)")
        if ss > 0:
          print(gr+"["+wi+str(ss)+gr+"]"+wi+" Targets has successfully find GeoIP Info About them")
        if ff > 0:
          print(yl+"["+rd+str(ff)+yl+"] Targets Failed To Get GeoIP Info About them "+rd+"!!!"+wi)
        exit(1)
      elif path.isfile(tar):
  		 loop = 1
  		 ss = 0
  		 abro = 0
  		 checked = []
  		 slp= lambda: True if len(checked) <=7 else False
  		 with open(tar) as targets:
                   for t in targets:
                     if not t.strip(): continue
                     t = t.strip()
                     if t in checked: continue
                     try:
                      getinfo(t,slp=slp())
                      ss+=1
                     except(KeyboardInterrupt,EOFError):
                        print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting....\n"+wi)
                        abro=1
                        break
                     finally:
                      checked.append(t)
  		 if abro ==0:
                   print(wi+"\n[#] Done :)")
                 if ss > 0:
                   print(gr+"["+wi+str(ss)+gr+"]"+wi+" Targets has successfully find GeoIP Info About them")
                 if ff > 0:
                   print(yl+"["+rd+str(ff)+yl+"] Targets Failed To Get GeoIP Info About them "+rd+"!!!"+wi)
      else:
        if tar =='me' or not tar.strip():
          tar = ""
        try:
          getinfo(tar)
        except(KeyboardInterrupt,EOFError):
          print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting....\n"+wi)
          exit(1)
        finally:
          print("[#] Done :)")
     else:
      print(rd+"["+yl+"!"+rd+"]"+yl+" Please Check Your Internet Connection "+rd+"!!!"+wi)
      exit(1)
   else:
    print(parse.usage)
    exit(1)

if __name__=="__main__":
  Main()

##############################################################
#####################                #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
