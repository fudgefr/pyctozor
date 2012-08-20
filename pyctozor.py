import pyexiv2
import os
# This is 2.7 python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--dry-run", help="Dry run: will print what it should have done",
		    action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
		    action="store_true")
parser.add_argument("source_dir",help="Directory where initial pictures are to be found")
parser.add_argument("-d", "--destdir", help="Destination dir in which sorted files will be copied to",
		    action="store_true")
parser.add_argument("-H", "--hardlinks", help="Use hardlinks for the whole sorting, instead of copying. Depends on platform")
args = parser.parse_args()

if args.verbose:
	print 'Verbose mode on'


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
