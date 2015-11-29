import sublime, sublime_plugin
#　import requests
import urllib.request, http.client, http.cookiejar, urllib.parse
import json
import subprocess, time
# from tkinter import *

class SendCommand(sublime_plugin.TextCommand):

	def on_addr_done(self, text):
		if "http" in text:
			serverAddr = text
			userfile = open("D:\\2.txt", 'w')
			userfile.write(text)
		else:
			text1 = "http://" + text
			serverAddr = text1
			userfile = open("D:\\2.txt", 'w')
			userfile.write(text1)
		
	def on_uname_done(self, text):
		usernamef = text
		userfile = open("D:\\1.txt", 'w')
		userfile.write(usernamef)

	def run(self, edit):
		# username
		usernamefile = open("D:\\1.txt", 'r')
		global usernamef
		usernamef = usernamefile.readline()
		if usernamef == '':
			sublime.active_window().show_input_panel('Please input user name: ',
												 '',
                    							 self.on_uname_done, None, None)

		username = {'username': usernamef}

		# server address
		global serverAddr 
		existFile = open("D:\\2.txt", 'r')
		existAddr = existFile.readline()
		if existAddr == '':
			sublime.active_window().show_input_panel('Please input the server address',
												 '',
                    							 self.on_addr_done, None, None)
		else:
			serverAddr = existAddr

		# user's program
		content = self.view.substr(sublime.Region(0, self.view.size()))
		body = {'program': content}

		filePath = "D:\\3.py"
		programFile = open(filePath, 'w')
		programFile.write(content)
		
		proc = subprocess.Popen(["C:\\Program Files (x86)\\Python\\python.exe", "-u", "D:\\3.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		(out, err) = proc.communicate()
		outstr = out.decode("utf-8").split()
		errstr = err.decode("utf-8")

		allOut = ""
		for perOutLine in outstr:
			allOut += perOutLine
		
		print ("HERE INOUTPUT", outstr)
		print ("HERE INOUTPUT", errstr)
		output = {'output': (allOut)}
		postContent = [username, body, output]

		print (serverAddr)
		# process data & need to be bytes
		jsondata = json.dumps(postContent)
		jsondatabytes = jsondata.encode('utf-8')

		# works well post function
		headers = {}
		headers['Content-Type'] = "application/json"
		headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
		req = urllib.request.Request(serverAddr, headers=headers)
		resq = urllib.request.urlopen(req, jsondatabytes)
		
