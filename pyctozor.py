import os
try:
	import optparse
except Exception, e:
	print 'pyctozor needs python 2.7 to run'
	raise
finally:
	pass

try:
	import pyexiv2
except Exception, e:
	print 'pyexiv2 module is needed. See http://tilloy.net/dev/pyexiv2/index.html for more details'
	raise
finally:
	pass

def ParseArguments(parser=None):
	"""
	This function takes a parser argument and return parsed arguments
	"""
	assert parser != None, "Internal error"
	parser.add_option("-n", "--dry-run", help="Dry run: will print what it should have done",
		action="store_true")
	parser.add_option("-v", "--verbose", help="increase output verbosity",
		action="store_true")
	if (os.name == 'posix'):
		parser.add_option("-H", "--hardlinks", help="Use hardlinks for the whole sorting, instead of copying. Depends on platform.",action="store_true")
	(options, args) = parser.parse_args()
	if len(args) != 2:
		parser.error("incorrect number of arguments")
	
	assert os.path.isdir(args[0]), "%s should be a directory" % str(args[0])
	assert os.path.isdir(args[1]), "%s should be a directory" % str(args[1])
	
	return (options,args)

def main():
	parser = optparse.OptionParser()
	(options,args) = ParseArguments(parser)
	if options.verbose:
		print 'Verbose mode on'
	pass

main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
