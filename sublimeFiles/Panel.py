import sublime, sublime_plugin

class PanelCommand(sublime_plugin.TextCommand):
    '''
    userfile = open("D:\\1.txt", 'r')
    content = ""
    userneme = ""
    userid = " 
   #if userfile.readline():
        # read the file
    for line in userfile:
        if "username" in line:
            username = line.split()[1]
        else: 
            userid = line.split()[1]

        print("successfully read")

    print("try get file content", userneme, userid)
    '''
    def prompt_sequence(self, g):
        def progress(result):
            def on_done(text):
                if text.isdigit():
                    userfile = open("D:\\1.txt", 'w')
                    userfile.write(text)
                else:
                    userfile = open("D:\\2.txt", 'w')
                    userfile.write(text)
    

            try:
                progress.caption, progress.initial_text = g.send(result)
                sublime.active_window().show_input_panel(
                    progress.caption,
                    progress.initial_text,
                    progress, on_done, None
                )
            except StopIteration:
                pass


        progress(None)

    def getUserInfo(self):
        userid = yield ('Please input user ID (only digit)', '')
        username = yield ('Please input user Name (real name)', '')

        sublime.message_dialog("successfully input information")

    def run(self, edit):
        self.prompt_sequence(self.getUserInfo())
