#!/usr/bin/python
import sys
print 'Output with no newline'
sys.stdout.write("Some output")
print ''

class Writer:
	def __init__(self, filename):
		self.filename = filename
	def write(self, msg):
		f = file(self.filename, 'a')
		f.write(msg)
		f.close()

sys.stdout = Writer('tmp.log')
print 'Log message A'
print 'Log message B'

