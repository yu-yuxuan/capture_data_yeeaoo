#!/usr/bin/python3
# http://www.yeeaoo.com/
import csv
import os, errno
import subprocess


def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)
def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)
    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


if __name__ == "__main__":
    file="url"
    ensure_dir("yeeaoo")
    with cd("yeeaoo"):
        with open('../Task1', 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter='_')
            for row in reader:
                ensure_dir(row[0])
                with cd(row[0]):
                    silentremove(file)
                    with open(file, "a") as myfile:
                        myfile.write('http://www.yeeaoo.com'+row[3]+ '\n')
        with open('../Task2', 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter='_')
            for row in reader:
                ensure_dir(row[0])
                with cd(row[0]):
                    with open(file, "a") as myfile:
                        myfile.write('http://www.yeeaoo.com'+row[3]+ '\n')
