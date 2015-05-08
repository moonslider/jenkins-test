#!/usr/bin/python
def test(arg1, arg2):
	arg1 = float(arg1)
	arg2 = float(arg2)
	assert arg2 != 0, 'Bad dividend -- arg1: %f arg2: %f' % (arg1, arg2)
	ratio = arg1 / arg2
	print 'ratio:', ratio

test(1, 2)
test(1, 0)
