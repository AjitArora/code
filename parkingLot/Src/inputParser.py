import code
from Controller import Controller

class inputParser:
	def __init__(self):
		self.controller = Controller()

	def print_output(self, line):
		ret = self.controller.run_cmd(line)
		if type(ret) == list:
			for r in ret:
				print r,
		else:
			print ret
		print " "

	def file_reader(self, input_file):
		fin = open(input_file, "r")
		for line in fin:
			line = line.split("\n")[0]
			self.print_output(line)

	def interactiveConsole(self):
		while True:
			line = raw_input()
			if line == "exit":
				break
			self.print_output(line)

	def run(self, args):
		arg_len = len(args)
		if arg_len > 1:
			self.file_reader(args[1])
		else:
			self.interactiveConsole()
