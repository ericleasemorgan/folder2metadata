#!/usr/bin/env python

# folder2metadata.py - given a directory, output a CSV file suitable for the Reader

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# December 31, 2021 - at the cabin; functional but not elegant


# configure
HEADER   = [ 'file', 'author', 'title', 'date' ]
METADATA = 'metadata.csv'

# require
from   pathlib import Path
import pandas as pd
import sys

# get input
if len( sys.argv ) != 2 : sys.exit( "Usage: " + sys.argv[ 0 ] + " <directory>" )
directory = sys.argv[ 1 ]

# initialize
directory = Path( directory )

# process each file in the given directory
metadata = []
for filename in directory.glob( '*' ) :

	# get the filename and its suffix
	file      =  filename.name
	if file[ 0 ] == '.' : continue
	suffix    =  filename.suffixes[ 0 ]
	if suffix == '.csv' : continue
	
	# parse and build record
	parts  = file.replace( suffix, '' ).split( '-' )
	author = parts[ 0 ]
	title  = file.replace( suffix, '' )
	date   = parts[ 2 ]
	record = [ file, author, title, date ]

	# update
	metadata.append( record )

# create a dataframe
metadata = pd.DataFrame( metadata, columns=HEADER )

# configure output, output, and done
output = directory/METADATA
metadata.to_csv( output, index=False )
exit()
