import sys
import urllib2
import re


OUTPUT_DIRECTORY = '/Users/dev/pthw/usajobs/html_dl'
pattern = re.compile('Park Ranger \(Protection\)')

for num in range(320000000, 330000000):
	html = "https://www.usajobs.gov/GetJob/ViewDetails/%i" % num
	
	try:
		req = urllib2.Request(html)
		response = urllib2.urlopen(req)
		the_page = response.read()
		
		if re.search(pattern, the_page):
			print "match found -> ", html
			f = open('%s/%s.txt' %(OUTPUT_DIRECTORY, num), 'wb')
   	 		f.write(the_page)
   	 		f.write("\n")
   	 		f.close()
		else:
			print "No match..."
			
	except IOError:
		print "Page not found:", num
		
quit()