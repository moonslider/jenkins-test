#!/usr/bin/python
# A basic class
class Basic:
	def __init__(self, name):
		self.name = name
	def show(self):
		print 'Basic -- name: %s' % self.name

obj1 = Basic('Hello')
obj1.show()

# Inheritance
class Special(Basic):
	def __init__(self, name, edible):
		Basic.__init__(self, name)
		self.upper = name.upper()
		self.edible = edible
	def show(self):
		Basic.show(self)
		print 'Special -- upper name: %s.' % self.upper
		if self.edible:
			print "It's edible"
		else:
			print "It's not edible"
	def edible(self):
		return self.edible

print '=' * 30
obj2 = Special('World', True)
obj2.show()

# class data
class C:
	count = 0
	def __init__(self):
		C.count = C.count + 1
	def getcount(self):
		return C.count

c1 = C()
print 'Current count:', c1.getcount()
c2 = C()
print 'Current count:', c2.getcount()

# static methods and class methods
class Advanced(object):
	def __init__(self, name):
		self.name = name
	def Description():
		return 'This is an advanced class.'
	def ClassDescription(cls):
		return 'This is advanced class: %s' % repr(cls)
	Description = staticmethod(Description)
	ClassDescription = classmethod(ClassDescription)

obj1 = Advanced('Welcome')
print obj1.Description()
print obj1.ClassDescription()
print '=' * 30
print Advanced.Description()
print Advanced.ClassDescription()



#Properties
class A(object):
	count = 0
	def __init__(self, name):
		self.name = name
	def set_name(self, name):
		print 'setting name: %s' % name
		self.name = name
	def get_name(self):
		print 'getting name: %s' % self.name
		return self.name
	objname = property(get_name, set_name)

def test():
	a = A('Apple')
	print 'name: %s' % a.objname
	a.objname = 'Banana'
	print 'name: %s' % a.objname
test()
