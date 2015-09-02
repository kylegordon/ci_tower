#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# A little Python script to change the status of some GPIOs
# POST JSON with a 'status' of red, amber or green, and it will
# change the GPIOs appropriately

# Test with curl --data "status=red" http://172.24.32.134/test.py
# curl --data '{"status":"red"}' http://172.24.32.134/test.py

# enable debugging and dump to /tmp/

import sys
import cgi
import json
import time

from subprocess import call

import cgitb
cgitb.enable(logdir='/tmp', display=True, format='text',)

print "Content-Type: text/plain;charset=utf-8"
print

print "CI Announcer!"

posted_input = sys.stdin.read()

if posted_input == "":
    print "Nothing posted"
    exit()

data = json.loads(posted_input)

print data

colour = data.get("status")
flash = data.get("flash", "no")

if colour == "":
    print "No colour specified or colour key provided"
    exit()


def go_green(flash):
    # Turn the others off
    call(["echo 0 > /sys/class/gpio/gpio12/value"], shell=True)
    call(["echo 0 > /sys/class/gpio/gpio13/value"], shell=True)

    if flash == "yes":
        # Flash green
        time.sleep(0.5)
        call(["echo 1 > /sys/class/gpio/gpio11/value"], shell=True)
        time.sleep(0.5)
        call(["echo 0 > /sys/class/gpio/gpio11/value"], shell=True)
        time.sleep(0.5)
        call(["echo 1 > /sys/class/gpio/gpio11/value"], shell=True)
        time.sleep(0.5)
        call(["echo 0 > /sys/class/gpio/gpio11/value"], shell=True)
        time.sleep(0.5)

    call(["echo 1 > /sys/class/gpio/gpio11/value"], shell=True)


def go_amber(flash):
    # Turn the others off
    call(["echo 0 > /sys/class/gpio/gpio11/value"], shell=True)
    call(["echo 0 > /sys/class/gpio/gpio13/value"], shell=True)

    if flash == "yes":
        # Flash amber
        time.sleep(0.5)
        call(["echo 1 > /sys/class/gpio/gpio12/value"], shell=True)
        time.sleep(0.5)
        call(["echo 0 > /sys/class/gpio/gpio12/value"], shell=True)
        time.sleep(0.5)
        call(["echo 1 > /sys/class/gpio/gpio12/value"], shell=True)
        time.sleep(0.5)
        call(["echo 0 > /sys/class/gpio/gpio12/value"], shell=True)
        time.sleep(0.5)

    call(["echo 1 > /sys/class/gpio/gpio12/value"], shell=True)


def go_red(flash):
    # Turn the others off
    call(["echo 0 > /sys/class/gpio/gpio11/value"], shell=True)
    call(["echo 0 > /sys/class/gpio/gpio12/value"], shell=True)

    if flash == "yes":
        # Flash amber
        time.sleep(0.5)
        call(["echo 1 > /sys/class/gpio/gpio13/value"], shell=True)
        time.sleep(0.5)
        call(["echo 0 > /sys/class/gpio/gpio13/value"], shell=True)
        time.sleep(0.5)
        call(["echo 1 > /sys/class/gpio/gpio13/value"], shell=True)
        time.sleep(0.5)
        call(["echo 0 > /sys/class/gpio/gpio13/value"], shell=True)
        time.sleep(0.5)

    call(["echo 1 > /sys/class/gpio/gpio13/value"], shell=True)


def go_off():
    call(["echo 0 > /sys/class/gpio/gpio11/value"], shell=True)
    call(["echo 0 > /sys/class/gpio/gpio12/value"], shell=True)
    call(["echo 0 > /sys/class/gpio/gpio13/value"], shell=True)


if colour == "red":
    print "You requested red"
    go_red(flash)

elif colour == "amber":
    print "You requested amber"
    go_amber(flash)

elif colour == "green":
    print "You requested green"
    go_green(flash)

elif colour == "off":
    print "You requested off"
    go_off()

else:
    print "Only 'red', 'amber', 'green' and 'off' values are accepted."
