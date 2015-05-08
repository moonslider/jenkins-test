#!/usr/bin/python
# To create a list use
items = []
items = [111, 222, 333]
# To add an item to the end of a list
items.append(444)
print items
# To insert an item into a list
items.insert(0, -1)
print items
# push items onto the right end of a list and pop items off the right end of a list with append and pop
items.append(555)
print items
print items.pop()
print items
for item in items:
	print 'item:', item
