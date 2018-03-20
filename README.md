# Zcoder

# Summary
Zcoder encodes Unicode `.txt` files as "z-Code" and converts them back to Unicode. 

Z-Code is a made up name for a purely alphabetic equivalent to Python's four-digit Unicode escape sequences. All numbers are converted to their spellings wrapped in the letter "z" (e.g. "1" becomes "zonez", 
"2" becomes "ztwoz", etc.). The exceptions are "0", which becomes "zqeroz" and initial "\u", which becomes "qq".

The rationale for z-code is that I was unable to process Classical Chinese characters using the [http://mallet.cs.umass.edu](MALLET) 
topic modelling tool. By converting my texts to z-code, running them through MALLET, and then converting MALLET's 
output back to Unicode, I was able to achieve my desired results. Zcoder may be useful for piping text files into 
other tools where Unicode may create a processing challenge.

# Use
The script is written in Python 2.7.3. It requires configuration of a source directory for the input files at the 
top of the script. There are two functions, z_encode() and z_decode() at the bottom of the zcoder.py. Run the former 
to z-encode texts and the latter to convert them back to Unicode. If you have processed the files using MALLET or 
another tool, you can run z_decode the output to convert it to Unicode. Both scripts will process all files in the 
source directory, including any subdirectories. z_encode() will create a new directory based on the source directory 
with the suffix "-encoded" attached and will save its output there. z_decode() gets its input from the "-encoded" 
directory (unless you change it in the configuration) and creates a new "-decoded" directory, where it saves its 
output.

A sample folder with three Chinese texts is included for testing.

## Dependencies
zcoder.py imports the Python os, fnmatch, and codex libraries.

## Citation and Contact Information
Kleinman, Scott (July 30, 2014). ZCoder. v. 1.0. https://github.com/scottkleinman/zcoder.

Contact: scott.kleinman@csun.edu

## License Information
This work is licensed under a [http://creativecommons.org/licenses/by-nc-sa/4.0/](Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License).
