import os
import sys
import re
import shutil
try:
	import optparse
except Exception, e:
	print 'pyctozor needs python 2.6 to run and does not support 2.7. Contributions are welcome!'
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

version="%prog 0.0.1"

def ParseArguments(parser=None):
	"""
	This function takes a parser argument and return parsed arguments
	"""
	assert parser != None, "Internal error"
	parser.add_option("-n", "--dryrun", help="Dry run: will print what it should have done",
		action="store_true")
	parser.add_option("-v", "--verbose", help="increase output verbosity",
		action="store_true")
	parser.add_option("-f", "--format", help="Will only deal with picture's format FORMAT",
		default="")
	if (os.name == 'posix'):
		parser.add_option("-H", "--hardlinks", help="Use hardlinks for the whole sorting, instead of copying. Depends on platform.",action="store_true")
	(options, args) = parser.parse_args()
	if len(args) != 2:
		parser.error("incorrect number of arguments")
	
	assert os.path.isdir(args[0]), "%s should be a directory" % str(args[0])
	assert os.path.isdir(args[1]), "%s should be a directory" % str(args[1])
	
	return (options,args)

def FolderRead(rootdir=None,extension=None,callback=None):
	"""
	Descend rootdir for files with name matching regexp extension, 
	and launch callback for each file it finds
	callback prototype is callback(path,file)
	"""
	assert rootdir!=None, "Internal Error"
	assert extension!=None, "Internal Error"

	file_re=re.compile(extension)
	for root, subFolders, files in os.walk(rootdir):
		# root is path to directory
		# subFolders is list of subdirectories inside root
		# files is list of files inside root
		for f in files:
			if file_re.match(f):
				file_metadata=pyexiv2.metadata.ImageMetadata(os.path.join(root,f))
				file_metadata.read()
				if options.verbose:
					print "File %s EXIF metadata are %s" % (f,file_metadata["Exif.Image.DateTime"].value)
				tag_root='file_metadata["Exif.Image.DateTime"]'
				tag_value_list=['%s.value.year' %tag_root,
					'%s.value.month' %tag_root,
					'%s.value.day' %tag_root]

				format_path='%s'
				for p in tag_value_list[1:]:
					format_path=os.path.sep.join([format_path,"%s"])
				new_file_path = os.path.join(dest_dir,format_path % eval(','.join(tag_value_list)))

				if not os.path.exists(new_file_path):
					if not options.dryrun:
						try:
							os.makedirs(new_file_path)
						except:
							print 'Error in making directory %s' % new_file_path
					else:
						print 'mkdir %s' % new_file_path
				if not os.path.isdir(new_file_path):
					raise IOError, "%s already exists and is not a directory" % new_file_path
				print 'Copy every files in %s to %s' % (root,new_file_path)
				if options.dryrun:
					print "cp %s %s" % (os.path.join(root,f),new_file_path)
				else:
					try:
						shutil.copy2(os.path.join(root,f), new_file_path)
					except shutil.Error:
						print 'Error with copying %s to %s intercepted...' % (os.path.join(root,f),new_file_path)
		for s in subFolders:
			FolderRead(s,extension,callback)


def main():
	ext_re=r"^.*\.?%s$" % options.format
	if options.verbose:
		print 'Will treat %s files' % ext_re
	FolderRead(source_dir,ext_re, None)
	pass

usage = "usage: %prog [options] source_dir dest_dir"
parser = optparse.OptionParser(usage=usage,version=version)
(options,args) = ParseArguments(parser)
if options.verbose:
	print 'Verbose mode on'
source_dir=args[0]
dest_dir=args[1]

main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
