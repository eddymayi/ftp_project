#!/usr/bin/python
# Remove files older than n days
import os
import time

def remove_files(number_of_days, path):
    """
    Removes files from the passed in path that are older than or equal
    to the number_of_days
    """
    time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    for root, _, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
            try:
               stat = os.stat(full_path)
               if stat.st_mtime <= time_in_secs:
                   os.remove(full_path)
            except OSError:
               print "Unable to locate file: %s" % full_path


if __name__ == "__main__":
   remove_files(60, "/ftp/")
