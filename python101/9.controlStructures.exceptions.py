#!/usr/bin/python
try:
	x = y
except:
	print 'y not defined'

try:
	myfile = file('amissingfile.py', 'r')
except IOError:
	print 'amissingfile.py is missing'

try:
	f = open('abcdefxyz.txt', 'r')
	d = {}
	x = d['name']
except (IOError, KeyError), e:
	print 'The error is --', e

class E(RuntimeError):
	def __init__(self, msg):
		self.msg = msg
	def getMsg(self):
		return self.msg

try:
	raise E('my test error')
except E, obj:
	print 'Msg:', obj.getMsg()

class GeneralException(Exception):
	pass
class SimpleException(GeneralException):
	pass
class ComplexException(GeneralException):
	pass
def some_func_that_throws_exceptions():
#	raise SimpleException, 'this is a simple error'
	raise ComplexException, 'this is a complex error'
def test():
	try:
		some_func_that_throws_exceptions()
	except GeneralException, e:
		if isinstance(e, SimpleException):
			print e
		else:
			raise
test()
