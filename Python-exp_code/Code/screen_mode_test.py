#! /usr/bin/env monkeyrunner
# Filename: screen_mode_test
# Description: This file is used to auto-test.

import sys, os, time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice,MonkeyImage

# define some useful path
adb_path = r"D:\Android4.0\Android4.0\Android\android-sdk\platform-tools\adb.exe"
filename = "screen_mode_test"

# connect to the device, returning a MonkeyDevice
device = MonkeyRunner.waitForConnection()
if not device:
    print >> sys.stderr, "Couldn't get connection"
    sys.exit(1)

# Take snapshot
def takeSnapShot(index):
    MonkeyRunner.sleep(1.0)
    result = device.takeSnapshot()
    tmp = time.strftime("%m.%d_%H.%M")
    result.writeToFile(filename + '_' + str(index) + '_' + tmp + '.png', 'png')

### begine to test
if __name__=='__main__':
    # start activity
    device.startActivity(component='com.android.camera/.Camera')

    # Test takeSnapShot
    for i in range(1, 11):
        takeSnapShot(i)
        MonkeyRunner.sleep(3.0)
        device.press('DPAD_CENTER', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(3.0)

    #Exit Activity
    device.press('KEYCODE_BACK', 'DOWN_AND_UP')
    MonkeyRunner.sleep(0.5)

    cmd = adb_path + " pull sdcard/DCIM/100ANDRO"
    os.system(cmd)
