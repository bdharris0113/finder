# finder

looks at auth.log files for any failed attempts to ssh into server.
uses urllib2 and ip-tracker.org to locate location of failed ip.
parses html from urllib2 and prints data
	


ASSUMPTIONS:  
you are running ubuntu/linux.
ssh logs are stored at /var/log/auth.log  

