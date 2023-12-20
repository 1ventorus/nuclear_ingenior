#!/usr/bin/env python

import os
import time
import urllib.request

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def game_install():
    fetch_file("https://raw.githubusercontent.com/1ventorus/nuclear_ingenior/main/nuclear_ingenior.py", "nuclear_ingenior.py")
    print("launcher installé")
    time.sleep(2)

def requierment_install():
    fetch_file("https://raw.githubusercontent.com/1ventorus/nuclear_ingenior/main/game_system.py", "game_system.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/nuclear_ingenior/main/maj.py", "maj.py")
    print("requierment installé")
    time.sleep(2)

if os.path.exists("nuclear_ingenior.py"):
    os.remove("nuclear_ingenior.py")

if os.path.exists("game_system.py"):
    os.remove("game_system.py")

if os.path.exists("maj.py"):
    os.remove("maj.py")

game_install()
requierment_install()
