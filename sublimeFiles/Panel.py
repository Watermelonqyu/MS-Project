import sublime, sublime_plugin

class PanelCommand(sublime_plugin.TextCommand):
    def prompt_sequence(self, g):
        def progress(result):
            def on_done(text):
                if text.isdigit():
                    userfile = open("D:\\1.txt", 'w')
                    userfile.write(text)
                else:
                    userfile = open("D:\\1.txt", 'w')
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
        # userid = yield ('Please input user ID (only digit)', '')
        username = yield ('Please input user Name (real name)', '')

        sublime.message_dialog("successfully input information")

    def run(self, edit):
        self.prompt_sequence(self.getUserInfo())
