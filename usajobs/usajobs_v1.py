import sys
import urllib2
import re

#local folder to store saved job postings
OUTPUT_DIRECTORY = '/Users/dev/Code/git/usajobs/html_dl' 
#string that matches desired job postings
pattern = re.compile('Park Ranger \(Protection\)')

#range of webpages based on control number
#estimated range is 320000000-41000000000
#example of 'Park Ranger (Protection)' at https://www.usajobs.gov/GetJob/ViewDetails/347178700
#current range loads 10 pages, one of which matches query
for num in range(347178695, 347178705):
	html = "https://www.usajobs.gov/GetJob/ViewDetails/%i" % num
	
	#open web page
	try:
		req = urllib2.Request(html)
		response = urllib2.urlopen(req)
		the_page = response.read()
		
		#search for string and save any pages that match as a .txt file to build data set
		if re.search(pattern, the_page):
			print "match found -> ", html
			f = open('%s/%s.txt' %(OUTPUT_DIRECTORY, num), 'wb')
   	 		f.write(the_page)
   	 		f.write("\n")
   	 		f.close()
		else:
			print "No match..."

	#bypass any html errors (e.g. "Error 404: Page not found")		
	except IOError:
		print "Page not found:", num
		
quit()