import sublime, sublime_plugin
#　import requests
import urllib.request, http.client, http.cookiejar
import json
# from tkinter import *

class SendCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# fake user
		# userid = {'id': '00550381'}
		#　username = {'username': 'Qiong'}
		# read information from file
		useridfile = open("D:\\1.txt", 'r')
		# number_id = len(useridfile.readline().split(":"))
		#　print("number_id: ", number_id) 
		userid = {'id': useridfile.readline()}

		usernamefile = open("D:\\2.txt", 'r')
		# numbername = len(usernamefile.readline().split(":"))
		username = {'username': usernamefile.readline()}

		content = self.view.substr(sublime.Region(0, self.view.size()))
		body = {'body': content}
		postContent = [userid, username, body]

		# True user
		'''
		userid = ""
		emailadr = ""
		inputurl = ""
		count = 0
		'''
		url = 'http://127.0.0.1:5000/index'

		# process data & need to be bytes
		jsondata = json.dumps(postContent)
		jsondatabytes = jsondata.encode('utf-8')


		'''
		master = Tk()
		e = Entry(master)
		e.pack()
		e. focus_set()
		b = Button(master, text="OK", width=10, command=callback)
		b.pack()
		'''

		'''
		if count == 0:
			self.view.window().show_input_panel("UserID", 'userid', self.on_done, None, None)
		if count == 1:		
			self.view.window().show_input_panel("Email Address", 'email address', self.on_done, None, None)
		else:
			self.view.window().show_input_panel("Server URL", 'server url', self.on_done, None, None)
		'''

		'''
		# If try the POST method, it will get the 405, method not allowed error
		hserver = urllib.request.Request(url)
		# self.view.insert(edit, 0, str(hserver))
		hserver.add_header('Content-Type', 'application/json; charest=utf-8')
		
		hserver.add_header('Content-Length', len(jsondatabytes))
		
		urldata = urllib.request.Request(url, jsondatabytes)
		url = urllib.request.urlopen(hserver, jsondatabytes)
		# hserver.request('POST', '/index.html', data)

		self.view.insert(edit, 0, str(jsondatabytes))
		
		
		# another way to send post 
		cjar = http.cookiejar.Cookiejar()
		opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
		'''


		
		# works well post function
		headers = {}
		headers['Content-Type'] = "application/json"
		headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
		req = urllib.request.Request(url, headers=headers)
		resq = urllib.request.urlopen(req, jsondatabytes)
		
