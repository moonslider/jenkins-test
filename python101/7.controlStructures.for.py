#!/usr/bin/python
collection = [111, 222, 333]
for item in collection:
	print 'item:', item

aDict = {'cat': 'furry and cute', 'dog': 'friendly and smart'}
print aDict
print aDict.keys()
print aDict.values()
for key in aDict.keys():
	print 'A %s is %s.' % (key, aDict[key])

for key in aDict:
	print 'A %s is %s.' % (key, aDict[key])

anIter = iter([11,22,33])
for item in anIter:
	print 'item:', item


def t(collection):
	icollection = iter(collection)
	for item in icollection:
		yield '||%s||' % item

for x in t(collection):
	print x
