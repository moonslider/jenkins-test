#!/usr/bin/python
import sys
#reply = "repeat"
#while reply == 'repeat':
#	print 'Hello'
#	reply = raw_input('Enter "repeat" to do it again: ')

def countLines(infilename):
	infile = file(infilename, 'r')
	count = 0
	for line in infile.readlines():
		line = line.strip()
		if line[:2] == '##':
			break
		count += 1
	return count
def usage():
	print 'Usage: python file.py <infilename>'
	sys.exit(-1)
def main():
	args = sys.argv[1:]
	if len(args) != 1:
		usage()
	count = countLines(args[0])
	print 'count:', count

if __name__ == '__main__':
	main()
