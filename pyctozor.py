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
	parser.add_option("source_dir",help="Directory where initial pictures are to be found")
	parser.add_option("destination_dir",help="Parent directory where pictures will be copied to")
	if (os.name == 'posix'):
		parser.add_option("-H", "--hardlinks", help="Use hardlinks for the whole sorting, instead of copying. Depends on platform.",action="store_true")
	args = parser.parse_args()

	assert os.path.isdir(args.source_dir), "source_dir should be a directory"
	assert os.path.isdir(args.destination_dir), "destination_dir should be a directory"
	
	return args

def main():
	parser = optparse.OptionParser()
	args = ParseArguments(parser)
	if args.verbose:
		print 'Verbose mode on'
	pass

main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
