#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath('textfile.txt')
    
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bank"
    
    # copy over the permissions, modification times, and other info
    shutil.copy(src, dst)
    
    # rename the original file
    os.rename('newfile.txt', 'textfile.txt')
    
    # now put things into a ZIP archive


    # more fine-grained control over ZIP files

def main2():
  if path.exists("textfile.txt"):
    src = path.realpath('textfile.txt')
    
    root_dir, tail = path.split(src)

    make_archive('archive', 'zip', root_dir)

def main3():
  if path.exists("textfile.txt"):
    src = path.realpath('textfile.txt')
    
    with ZipFile('testzip.zip', 'w') as newzip:
      newzip.write('textfile.txt')
      
if __name__ == "__main__":
  main3()
