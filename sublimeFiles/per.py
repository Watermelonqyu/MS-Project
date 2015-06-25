import sublime, sublime_plugin
#　import requests
import json


class perCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Please enter the directory name:", "something", self.on_done1, None, None)
        self.window.show_input_panel("Please enter the desired examples photo range, ex: 40-250", "", self.on_done1, None, None)

    def on_done1(self, user_input):
        global command
        command = command + " " + user_input
        print (command)