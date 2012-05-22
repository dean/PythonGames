from httplib import *
import os.path

def get_link(inp):
	found = inp.find("http://")
	if inp.find("https://")>=0:
		found = inp.find("https://")
	if found>=0:
		end = inp.find(" ", found)
		inp = inp[found:end]
		if inp.find("\"")>= 0:
			end = inp.find("\"")
			return inp[:end]
		return inp
	else:
		return -1 ## If a link is not found in the current string

def collect_links(data):
	links = []
	for line in data.split("\n"):
		link = get_link(line)
		if link != -1:
			links.append(link+"\n")
	return links	

def goto_link(link):
	print "Very beginning of link is ", link
	if link.find("schema") >= 0:
		return
	http = link.find("http://")	
	https = link.find("https://")
	print "http = ", http
	print " https = ", https
	if http >= 0:
		link = link[7:]
		print "http://Link before request: ", link
		con = HTTPConnection(link) #len -1 to get rid of / on end so we can send it for the request
	elif https>=0:
		link = link[8:]
		print "https://Link before request: ", link
		con = HTTPConnection(link)
	else:
		print "nothingLink before request: ", link
		con = HTTPConnection(link)

	print "Past Con: Link before request: ", link
	con.request("GET", "")
	resp = con.getresponse()
	
	FILE = open(filename, "a")
	if resp.status == 200:
		print "Webpage was found successfully and info being added to file! :D\n"
		links = collect_links(resp.read())
		FILE.writelines(links)
		for l in links:
			print "Going to link ", l
			goto_link(l)
	elif resp.status == 404:
		print "Webpage was not found!! :(\n"
	else:
		print resp.status, resp.reason
	con.close()
	FILE.close()

filename = "webLinks.txt"
if os.path.exists(filename):
	FILE = open(filename, "a")
	FILE.write("")
	FILE.close()
else:
	FILE = open(filename, "w")
	FILE.write("")
	FILE.close()

goto_link("www.google.com")


