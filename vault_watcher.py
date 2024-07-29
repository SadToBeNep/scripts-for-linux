#!/usr/bin/python

### This script was made so I can put it in some kind of bar, and it would display that if my luksVault is mounted or not
### The script works by checking if there is a file availble or not, this file called CHECK is just an empty file that is
### only used for this purpose, if it's not available display nothing in order to make the bar look more clean


### In order for the virtual-machine watcher to work, we need to allow `virsh domstate [vm_name] to be run without sudo password`
### this can be achieved by modifying the sudoers file

### The need for them to run in async isn't necessary, it's just a bit faster since the virsh command takes a bit more time than the file checking

### TODO: Set up MEGA cloud with gocryptfs and also make a watcher for that ❌
### 
import os
from subprocess import check_output
import asyncio


async def luksWatcher():
    if(os.path.exists("/mnt/notsecret/CHECK")):
        print("☢️ ✅ ")

async def virtualMachineWatcher():
    output = check_output(['sudo','virsh','domstate','win11']).decode()
    if("off" in output):
        pass
    else:
        print("  ✅ ")

async def main():
    await asyncio.gather(
        luksWatcher(),
        virtualMachineWatcher()
    )

if __name__ == "__main__":
   asyncio.run(main())