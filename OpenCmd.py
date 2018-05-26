import sublime
import sublime_plugin
import os

class OpenCmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		file_name = self.view.file_name()
		index = file_name.rfind('\\') + 1
		full_path = '"' + file_name[:index] + '"'
		cmd = 'cd ' + full_path + ' & start cmd'
		os.system(cmd)
