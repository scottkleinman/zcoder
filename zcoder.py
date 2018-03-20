#####################################################################
# Title: zcoder.py                                                  #
# Author: Scott Kleinman                                            #
# Contact: scott.kleinman@csun.edu                                  #
# Date: July 30, 2014                                               #
# Version: 1.01                                                     #
# This work is licensed under a Creative Commons Attribution-       #
# NonCommercial-ShareAlike 4.0 International License:               #
# http://creativecommons.org/licenses/by-nc-sa/4.0/                 #
# See bottom of code for use.                                       #
#####################################################################

#####################################################################
# Encodes Unicode .txt files as Z-Code for use with tools that      #
# cannot process the Unicode and decodes Z-code back to Unicode.    #
#                                                                   #
# Works with all files in directory indicated under Configuration,  #
# including files in subdirectories. Creates equivalent directory   #
# structure for output. To decode z-encoded files not created by    #
# this tool, place them in the encodeddir folder.                   #
#                                                                   #
# See the bottom of code for commands to call the encoding and      #
# decoding functions.                                               #
#####################################################################

# Configuration -- Enter the source folder here without trailing slash
sourcedir = 'C:\Users\Confucius\Documents\chinese'
encodeddir = sourcedir+'-encoded'
decodeddir = sourcedir+'-decoded'

# Global replacement dictionaries
encoding_replacements = {
    '\u':'qq', '1':'zonez', '2':'ztwoz',
    '3':'zthrz', '4':'zfourz', '5':'zfivez',
    '6':'zsixz', '7':'zsevenz', '8':'zeightz',
    '9':'zninez', '0':'zqeroz'
}

decoding_replacements = {
    b'qq': b'\\u', b'zonez': b'1', b'ztwoz': b'2',
    b'zthrz': b'3', b'zfourz': b'4', b'zfivez': b'5',
    b'zsixz': b'6', b'zsevenz': b'7', b'zeightz': b'8',
    b'zninez': b'9', b'zqeroz': b'0'
}

# Python library imports
import os, fnmatch, codecs, re

# Z-Encoder Function (Important: output files contain escaped line breaks)
def z_encode(directory, encoding_replacements, filePattern):
    print('Encoding...')
    # Walk though the directories
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        # Read each file
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with codecs.open(filepath, 'r', encoding='utf-8') as f:
                s = f.read()
            # Small routine to remove whitespace and encode as Unicode escapes
            pattern = re.compile(r'\s+')
            s = re.sub(pattern, ' ', s)
            s = s.encode('unicode-escape')
            # Replace the Unicode escapes with z-code
            for find, replace in replacements.iteritems():
                s = s.replace(find, replace)
            # Create a new output path
            encodedpath = path.replace(sourcedir, encodeddir)
            outfilepath = os.path.join(encodedpath, filename)
            # Make sure any subfolders exist
            if not os.path.isdir(encodedpath):
                os.mkdir(encodedpath)
            # Write the z-encoded file
            with open(outfilepath, "w") as f:
                f.write(s)

# Z-Decoder Function (Important: output files contain escaped line breaks)
def z_decode(directory, replacements, filePattern):
    # Walk though the directories
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        # Read each file
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with codecs.open(filepath, 'r', encoding='utf-8') as f:
                s = f.read()
            # Replace the z-code with Unicode escapes
            for replace, find in replacements.iteritems():
                s = s.replace(find, replace)
            # Create a new output path
            decodedpath = path.replace(encodeddir, decodeddir)
            outfilepath = os.path.join(decodedpath, filename)
            # Make sure any subfolders exist
            if not os.path.isdir(decodedpath):
                os.mkdir(decodedpath)
            s = s.decode('unicode-escape')
            # Write the de-encoded file
            with codecs.open(outfilepath, "w", encoding='utf-8') as f:
                f.write(s)

# Use: Run the first command to encode Unicode as z-code.
# Run the second to convert z-encoded files to Unicode.
z_encode(sourcedir, replacements, "*.txt") # Uncomment to z-encode texts
#z_decode(encodeddir, replacements, "*.txt") # Uncomment to decode z-encoded texts