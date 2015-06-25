import sublime, sublime_plugin
#　import requests
import urllib.request, http.client, http.cookiejar
import json
# from tkinter import *

class SendCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		useridfile = open("D:\\1.txt", 'r')
		userid = {'id': useridfile.readline()}

		usernamefile = open("D:\\2.txt", 'r')
		username = {'username': usernamefile.readline()}

		content = self.view.substr(sublime.Region(0, self.view.size()))
		body = {'body': content}
		postContent = [userid, username, body]

		url = 'http://127.0.0.1:5000/index'

		# process data & need to be bytes
		jsondata = json.dumps(postContent)
		jsondatabytes = jsondata.encode('utf-8')

		# works well post function
		headers = {}
		headers['Content-Type'] = "application/json"
		headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
		req = urllib.request.Request(url, headers=headers)
		resq = urllib.request.urlopen(req, jsondatabytes)
		
