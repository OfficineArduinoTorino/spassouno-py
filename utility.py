import termios
import select
import sys
import tty

import socket
import os

def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial


def getname():
    return socket.gethostname()


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def read_key():
    if isData():
        k = sys.stdin.read(1)
        # Exteded key (Up, Down, ...)
        if ord(k) == 27:
            k += sys.stdin.read(2)
        return k
    else:
        return ''


def init_key_read():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    return old_settings


def restore_key_read(old_settings):
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


def find_usb_path():
    partitionsFile = open("/proc/partitions")
    lines = partitionsFile.readlines()[2:]#Skips the header lines
    for line in lines:
        words = [x.strip() for x in line.split()]
        minorNumber = int(words[1])
        deviceName = words[3]
        if minorNumber % 16 == 0:
            path = "/sys/class/block/" + deviceName
            if os.path.islink(path):
                if os.path.realpath(path).find("/usb") > 0:
                    return "/dev/%s" % deviceName
    return None
