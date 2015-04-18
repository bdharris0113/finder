#! bin/python

'''
ASSUMPTIONS:  
you are running ubuntu/linux.
ssh logs are stored at /var/log/auth.log  
'''

import os,re,urllib2


def finder():
	'''
	looks at auth.log files for any failed attempts to ssh into server.
	uses urllib2 and ip-tracker.org to locate location of failed ip.
	parses html from urllib2 and prints data
	'''
	os.system("cat /var/log/auth.log | grep Fail > test.txt")

	f = open('test.txt','r')
	lines = f.readlines()
	f.close()

	#allow for duplicate ip addresses; will add a running count of attempts / address
	ip_addr = []
	for line in lines:
		temp_ip = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',line)
		ip_addr.append(temp_ip[0])

	ip_addr = ['8.8.8.8','14.137.191.255','216.239.63.255','208.67.222.222','198.153.194.2','205.210.42.205','2.63.255.255','5.35.159.255','1.0.127.255']
	#ip_addr = ['2.63.255.255']
	for ip in ip_addr:

		try:
			url = 'http://www.ip-tracker.org/locator/ip-lookup.php?ip='+ip

			temp = urllib2.urlopen(url)
			html = temp.readlines()
			temp.close()

			temp_data = html[208:215]
			for line in temp_data:
				if line[:29] == "</td></tr><tr><th class=track":
					data = line


			cont = re.findall("Country:</th><td>.*?\&",data)
			reg = re.findall('data-simpleopenweather-city=.*?>',data)

			state = re.findall("State:</th><td class='tracking lessimpt'>.*?<",data)
			city = re.findall("City Location:</th><td class='vazno'>.*?<",data)

			if state == []:
				state = re.findall("State:</th><td.*?>.*?<",data)
				state = state[0][14:]
				state = re.findall(">.*?<",state)
				state = state[0][1:-1]
			else:
				state = state[0][41:-1]

			if city == []:
				city = re.findall("City Location:</th><td>.*?<",data)
				city = city[0][24:-1]

			else:
				city = city[0][37:-1]

			if cont == []:
				cont = 'Unknown'
			else:
				cont = cont[0][18:-2]

			print "%s : %s , %s , %s" %(ip,cont,state,city)
		except:
			print "could not locate ip \n"



finder()