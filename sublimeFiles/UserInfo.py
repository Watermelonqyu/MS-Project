import sublime, sublime_plugin
import json

class UserInfoCommand(sublime_plugin.TextCommand):
	class jcontent:
		def __init__(self):
			self.userid = None
			self.username = None

	def on_done():
		
	sublime.active_window().show_input_panel(
			'Please Input User ID (should be number)', '',
			None, None, None)
