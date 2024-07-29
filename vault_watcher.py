#!/usr/bin/python

### This script was made so I can put it in some kind of bar, and it would display that if my luksVault is mounted or not
### The script works by checking if there is a file availble or not, this file called CHECK is just an empty file that is
### only used for this purpose, if it's not available display nothing in order to make the bar look more clean
import os

def luksWatcher():
    if(os.path.exists("/mnt/notsecret/CHECK")):
        print("☢️ ✅")



if __name__ == "__main__":
    luksWatcher()