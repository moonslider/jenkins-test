#!/usr/bin/python
lookup = {}
def fruitfunc():
	print "I'm a fruit."
def vegetablefunc():
	print "I'm a vegetable."

lookup = {'fruit':fruitfunc, 'vegetable':vegetablefunc}
print lookup
if lookup.has_key('fruit'):
	print 'contains key "fruit"'
if 'fruit' in lookup:
	print 'contains key "fruit"'
print lookup['fruit']
for key in lookup:
	print 'key:%s' % key
	lookup[key]()
