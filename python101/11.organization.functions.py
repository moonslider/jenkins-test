#!/usr/bin/python
# A basic function
def test(msg, count):
	for idx in range(count):
		print '%s %d' %(msg, idx)
test('Test #', 4)

# Create a tuple:
val = (test, 'A label:', 5)
val[0](val[1], val[2])


# A function with default arguments
def testDefaultArgs(arg1='default1', arg2='default2'):
	print 'arg1:', arg1
	print 'arg2:', arg2

testDefaultArgs('Explicit value')
testDefaultArgs()

# argument lists and keyword argument lists
def testArgLists_1(*args, **kwargs):
	print 'args:', args
	print 'kwargs:', kwargs

testArgLists_1('aaa', 'bbb', args1='ccc', arg2 = 'ddd')

def testArgLists_2(arg0, arg11, *args, **kwargs):
	print 'arg0: "%s"' % arg0
	print 'args:', args
	print 'kwargs', kwargs
print '=' * 40
testArgLists_2('a first argument', 'aaa', 'bbb', arg1='ccc', arg2='ddd')
