# Zcoder

## Summary

`Zcoder` encodes Unicode `.txt` files as "z-Code" and converts them back to Unicode. 

Z-Code is a made up name for a purely alphabetic equivalent to Python's four-digit Unicode escape sequences. All numbers are converted to their spellings wrapped in the letter "z" (e.g. "1" becomes "zonez", 
"2" becomes "ztwoz", etc.). The exceptions are "0", which becomes "zqeroz" and initial "\u", which becomes "qq".

The rationale for z-code is that I was unable to process Classical Chinese characters using the [http://mallet.cs.umass.edu](MALLET) 
topic modelling tool. By converting my texts to z-code, running them through MALLET, and then converting MALLET's 
output back to Unicode, I was able to achieve my desired results. Zcoder may be useful for piping text files into 
other tools where Unicode may create a processing challenge.

## Dependencies

`Zcoder` is written for Python 3.6, although it seems to work in Python 2.7. It requires the [Python Fire](https://github.com/google/python-fire) library. To install, it, run `pip install fire`.

## Usage

Assume you have three directories: `original_files`, `encoded_files`, and `decoded_files`. To convert your original text files to z-code run the following command from the command line:

```
python zcoder.py encode original_files encoded_files
```

This will convert all text files (and only text files) in the `original` directory to `zcode` and save the new files in the `encoded_files` directory.

To convert the files back to Unicode, run 

```
python zcoder.py decode encoded_files decoded_files
```

Of course, you would not actually want to decode the same files from the `encoded_files` directly created by the first command above. In the scenario that led to the creation of this script, the z-coded files are run through MALLET, and the MALLET output files are the ones decoded by `zcoder`.

A sample folder with two Chinese texts is included for testing.

## Citation and Contact Information

Kleinman, Scott (March 20, 2018). ZCoder. v. 2.0. https://github.com/scottkleinman/zcoder.

Contact: scott.kleinman@csun.edu

## License Information

This work is licensed under a [http://creativecommons.org/licenses/by-nc-sa/4.0/](Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License).
