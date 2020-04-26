import os
import shutil
import fnmatch

DESTINATION = r'G:\photos'
SOURCE = r'G:\Google Photos'


def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

try:
    filesToMove = gen_find("*.jpg", SOURCE)
    for name in filesToMove:
        shutil.move(name, DESTINATION)
except Exception as err:
    print(err)
