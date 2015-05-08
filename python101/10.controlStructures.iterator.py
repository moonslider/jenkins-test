#!/usr/bin/python
def generateItems(seq):
	for item in seq:
		yield 'item: %s' % item
anIter = generateItems([])
print 'dir(anIter):', dir(anIter)
anIter = generateItems([111,222,333])
for x in anIter:
	print x
anIter = generateItems(['aaa', 'bbb', 'ccc'])
print anIter.next()
print anIter.next()
print anIter.next()
#print anIter.next()


#
# A class that provides an iterator generator method.
#
class Node:
        def __init__(self, name='<noname>', value='<novalue>', children=None):
                self.name = name
                self.value = value
                self.children = children
                if children is None:
                        self.children = []
                else:
                        self.children = children
        def set_name(self, name): self.name = name
        def get_name(self): return self.name
        def set_value(self, value): self.value = value
        def get_value(self): return self.value
        def iterchildren(self):
                for child in self.children:
                        yield child
        #
        # Print information on this node and walk over all children and
        #   grandchildren ...
        def walk(self, level=0):
                print '%sname: %s  value: %s' % (
                        get_filler(level), self.get_name(), self.get_value(), )
                for child in self.iterchildren():
                        child.walk(level + 1)

#
# An function that is the equivalent of the walk() method in
#   class Node.
#
def walk(node, level=0):
        print '%sname: %s  value: %s' % (
                get_filler(level), node.get_name(), node.get_value(), )
        for child in node.iterchildren():
                walk(child, level + 1)

def get_filler(level):
        return '        ' * level

def test():
        a7 = Node('gilbert', '777')
        a6 = Node('fred', '666')
        a5 = Node('ellie', '555')
        a4 = Node('daniel', '444')
        a3 = Node('carl', '333', [a4, a5])
        a2 = Node('bill', '222', [a6, a7])
        a1 = Node('alice', '111', [a2, a3])
        # Use the walk method to walk the entire tree.
        print 'Using the method:'
        a1.walk()
        print '=' * 30
        # Use the walk function to walk the entire tree.
        print 'Using the function:'
        walk(a1)

test()

