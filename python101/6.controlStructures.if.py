#!/usr/bin/python
def function1():
	print "Hi. I'm function1."
def function2():
	print "Hi. I'm function2."
def function3():
	print "Hi. I'm function3."

mapper = {'one': function1, 'two': function2, 'three': function3}

while 1:
	code = raw_input('Enter "one", "two", "three", or "quit": ')
	if code == 'quit':
		break
	if code not in mapper:
		continue
	mapper[code]()
