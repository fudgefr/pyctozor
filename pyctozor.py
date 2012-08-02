import pyexiv2
import os
# This is 2.7 python 
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args=parser.parse_args()

if args.verbose:
	print 'Verbose mode on'

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
