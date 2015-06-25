import sublime, sublime_plugin
#　import requests
import json

class UserInfoCommand(sublime_plugin.TextCommand):
# user_id = ""
#　user_name = ""

	class jcontent:
		def __init__(self):
			self.userid = None
			self.username = None

	def on_done():
		
	sublime.active_window().show_input_panel(
			'Please Input User ID (should be number)', '',
			None, None, None)


'''
	def run(self, edit):
		sublime.active_window().show_input_panel(
			'Please Input User ID (should be number)', '',
			None, None, None)

		sublime.active_window().show_input_panel(
			'Please Input User Name (your name)', '',
			None, None, None)
		pass

	

	

	def on_done(user_input):
		sublime.status_message("User said: " + user_input)


	sublime.active_window().show_input_panel(
			'Please Input User ID (should be number)', '',
			on_done(input), 
			None, None)
	sublime.active_window().show_input_panel(
			'Please Input User Name (your name)', '',
			on_done(input), 
			None, None)

	
	user_id = input('Please input your id: ')
	user_name = input('Please input your name')

	jcontent.userid = user_id
	jcontent.username = user_name

		# jcontent.serveraddr = server_address
		# fcontent = [{"userid":jcontent.userid}, {"username":jcontent.username}]
	userfile = open('userInfo.txt', 'w')
	writeC = jcontent.userid + "\n" + jcontent.username
	print("Hello", writeC);
	userfile.write(writeC)



def getInfo():
		user_id = yield ('Please Input User ID (should be number)', '')
		user_name = yield ('Please Input User Name (your name)', '')
        # server_address = yield ('Server Address', '')

		sublime.message_dialog('Your answers: ')
		# prompt_sequence(foo())


	userfile = open('userInfo.txt', 'r')

		# userfile.readline()
	if userfile.readline():
			# read the file
		for line in userfile:
			content += line

			# replace with the correct information
			jcontent = json.dump(content)

		# replace whole file content with user inputs
'''