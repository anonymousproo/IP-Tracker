#ip tracker v0.5 provider by Anonymous Pro
#Author Mahfuzur Rahman
#python script
#Follw Me
#visit: www.anonymousproo.com
#github: https://github.com/anonymousproo
#youtube: https://www.youtube.com/anonymouspro1
#Facebook: https://m.facebook.com/anonymousproo1
import os
import urllib2
import json
#For your own IP Coding
url = "http://ip-api.com/json/"
load1 = urllib2.urlopen(url)
read1 = load1.read()
result1 = json.loads(read1)
os.system('clear')
print ('''
\033[1;33m
		$$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
		\_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
  		  $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
  		  $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
  		  $$ |  $$  ____/\033[1;32m          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$< 
  		  $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |\033[1;31m{v3.0}\033[1;31m
		$$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
		\______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__|\033[1;32m
\033[1;33m
''')
print("\033[1;33m==================================================================================================\033[1;33m")
print(   
print(	"\033[1;32mAuthor			:Mahfuzur Rahman\033[1;32m"                                                   )
print(	"\033[1;32Github			:https://github.com/anonymousproo\033[1;32m"
print(	"\033[1;32mYouTube			:https://www.youtube.com/anonymouspro1			{IP Tracker v3.0}\033[1;32m")
print(	"\033[1;32mfacebook		:https://m.facebook.com/anonymousproo1\033[1;32m"
print(	"\033[1;32mcoded by		:ANONYMOUS PRO YTB\033[1;32m"

print"\033[1;33m==================================================================================================\033[1;33m"
print ("\n\033[1;33mYour IP: \033[1;33m" + result1['query'])
print ("\033[1;32mIf You Do Not Want To Track Type Exit\033[1;32m\n")

while True:
    ip = raw_input("\033[1;36mEnter Your Target IP: \033[1;36m")

    if ip == 'exit':
        break
    else:
        #ips Coding
        api = "http://api.ipstack.com/"
        load = urllib2.urlopen(api + ip + '?access_key=fd0c1eae3c2d27ee676af0db2b864b0e')
        read = load.read()
        result = json.loads(read)

        #ip-api
        url = "http://ip-api.com/json/"
        load1 = urllib2.urlopen(url + ip)
        read1 = load1.read()
        result1 = json.loads(read1)





        if result1['status'] == 'success':
            # latitude
            lati = result['latitude']
            lat = "{:.4f}".format(lati)
            # longitude
            lon = result['longitude']
            long = "{:.4f}".format(lon)

            # more info
            more = json.dumps(result['location'])

            # printing information
            print ("\n\033[1;33mAll The Information Of IP Is Here \033[1;33m[" + ip + "] :\n")
            print("\033[1;33mIP: \033[1;33m" + result['ip'])
            print("\033[1;32mIP Type: \033[1;32m" + result['type'])
            print("\033[1;34mContinent Name: \033[1;34m" + result['continent_name'])
            print("\033[1;34mContinent Code: \033[1;34m" + result['continent_code'])
            print("\033[1;33mCountry: \033[1;33m" + result['country_name'])
            print("\033[1;33mCountry Code: \033[1;33m" + result1['countryCode'])
            print("\033[1;32mRegion Name: \033[1;32m" + result['region_name'])
            print("\033[1;32mRegion Code: \033[1;32m" + result['region_code'])
            print("\033[1;36mCity: \033[1;36m" + result['city'])
            print("\033[1;36mZip: \033[1;36m" + result['zip'])
            print("\033[1;33mTimeZone: \033[1;33m" + result1['timezone'])
            print("\033[1;33misp: \033[1;33m" + result1['isp'])
	    print("Do you want to find the exact location with Google Maps?")
	    print("Then search the Google Map using the Latitude or longitude number")
            print("\033[1;36mLatitude: \033[1;36m" + lat)
            print("\033[1;36mlongitude: \033[1;36m" + long)
            print("\033[1;33mMore Information Of IP \033[1;33m:\n" + more)
            print("\n\n")
        else:
            print("\n\033[1;31mSorry, Please Type The IP[" + ip + "] Please try again\033[1;31m\n")
