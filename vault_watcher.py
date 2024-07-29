#!/usr/bin/python
import os

def luksWatcher():
    if(os.path.exists("/mnt/notsecret/CHECK")):
        print("☢️ ✅")



if __name__ == "__main__":
    luksWatcher()