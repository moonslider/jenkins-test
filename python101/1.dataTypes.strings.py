#!/usr/bin/python
#Create a new string from a constant
s1 = 'abcd'
s2 = "I'm OK"
s3 = 'I\'m also OK'
s4 = """A
multi-line
strings.
"""

print s3
print s4

print s2.upper()
print s2.find('OK')
print s2.find('WRONG')
print s2.replace('OK', 'WRONG')
# Type "help(str)" or see http://www.python.org/doc/current/lib/string-methods.html
# for more information on string methods.

state = 'PA'
print 'It never rains in sunny %s.' % state

# write strings to a file and read them from a file
outfile = file('tmp.txt', 'w')
outfile.write('This is A\n')
outfile.write('This is B\n')
outfile.write('This is C\n')
outfile.close()

infile = file('tmp.txt', 'r')
content = infile.read()
print content
infile.close()

infile = file('tmp.txt', 'r')

i = 0
for line in infile.readlines():
	i = i+1
	print 'Line', str(i), ": ", line
infile.close()


for ch in s2:
	print ch


######################################################################################
#Result#
"""
I'm also OK
A
multi-line
strings.

I'M OK
4
-1
I'm WRONG
It never rains in sunny PA.
This is A
This is B
This is C

Line 1 :  This is A

Line 2 :  This is B

Line 3 :  This is C

I
'
m
 
O
K
"""
######################################################################################
