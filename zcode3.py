#####################################################################
# Title: zcoder3.py                                                 #
# Author: Scott Kleinman                                            #
# Contact: scott.kleinman@csun.edu                                  #
# Date: March 20, 2018                                              #
# This work is licensed under a Creative Commons Attribution-       #
# NonCommercial-ShareAlike 4.0 International License:               #
# http://creativecommons.org/licenses/by-nc-sa/4.0/                 #
#####################################################################

#####################################################################
# Encodes Unicode .txt files as Z-Code for use with tools that      #
# cannot process the Unicode and decodes Z-code back to Unicode.    #
#                                                                   #
# Run with the following command:                                   #
#                                                                   #
# python zcode3.py encode SOURCE_DIR OUTPUT_DIR                     #
#                                                                   #
#                   or                                              #
#                                                                   #
# python zcode3.py decode SOURCE_DIR OUTPUT_DIR                     #
#                                                                   #
# SOURCE_DIR should be the path to the directory containing your    #
#     source files.                                                 #
# OUTPUT_DIR should be the path to the directory where you want     #
#     to save your encoded/decoded files.                           #
#####################################################################

# Python library imports
import os, fnmatch, codecs, re
import fire

# Z-Encoder Function (Important: output files contain escaped line breaks)
def z_encode(source, output):
    # Set replacements
    replacements = {b'\\u': b'qq', b'1': b'zonez', b'2': b'ztwoz', b'3': b'zthrz', b'4': b'zfourz', 
        b'5': b'zfivez', b'6': b'zsixz', b'7': b'zsevenz', b'8': b'zeightz', b'9': b'zninez', b'0': b'zqeroz'}

    # Walk though the directories
    for path, dirs, files in os.walk(os.path.abspath(source)):
        # Read each file
        for filename in fnmatch.filter(files, '*.txt'):
            print('Encoding ' + filename + '...')
            filepath = os.path.join(path, filename)
            with open(filepath, 'rb') as f:
                text = f.read().rstrip()  # rstrip to remove trailing spaces
                decoded = text.decode('unicode-escape').encode('latin1').decode('utf-8')
                encoded = decoded.encode('unicode-escape')
                # Replace the Unicode escapes with z-code
                for find, replace in replacements.items():
                    encoded = encoded.replace(find, replace)
            # Create a new output path
            outpath = os.path.join(output, filename)
            # Write the z-encoded file
            with open(outpath, 'wb') as f:
                f.write(encoded)
    print('Done!')
    
# Z-Encoder Function (Important: output files contain escaped line breaks)
def z_decode(source, output):
    # Set replacements
    replacements = {b'qq': b'\\u', b'zonez': b'1', b'ztwoz': b'2', b'zthrz': b'3', b'zfourz': b'4', 
        b'zfivez': b'5', b'zsixz': b'6', b'zsevenz': b'7', b'zeightz': b'8', b'zninez': b'9', b'zqeroz': b'0'}

    # Walk though the directories
    for path, dirs, files in os.walk(os.path.abspath(source)):
        # Read each file
        for filename in fnmatch.filter(files, '*.txt'):
            print('Decoding ' + filename + '...')
            filepath = os.path.join(path, filename)
            with open(filepath, 'rb') as f:
                text = f.read().rstrip()  # rstrip to remove trailing spaces
                # Replace the z-code with Unicode escapes
                for find, replace in replacements.items():
                    text = text.replace(find, replace)
                # Convert back to Unicode
                decoded = text.decode('unicode-escape')
            # Create a new output path
            outpath = os.path.join(output, filename)
            # Write the Unicode file
            with open(outpath, 'wb') as f:
                f.write(decoded.encode('utf-8'))
    print('Done!')

def execute(*items):
    try:
        assert len(items) == 3
        action = items[0]
        source = items[1]
        output = items[2]
        if action == "encode":
            z_encode(source, output)
        else:
            z_decode(source, output)
    except:
        help = """
        Your command has the wrong number of arguments.
        Use the format "python zcode.py ACTION SOURCE_DIR OUTPUT_DIR".
        ACTION should be "encode" or "decode".
        SOURCE_DIR should be a path the source directory for your texts.
        OUTPUT_DIR should be a path to the directory where you wish to save your encoded/decoded texts.
        """
        print(help)

if __name__ == '__main__':
    fire.Fire(execute)
