#!/usr/bin/env python

import os
import time
import urllib.request


BANNER=("""
    ▄     ▄   ▄█▄    █     ▄███▄   ██   █▄▄▄▄  
     █     █  █▀ ▀▄  █     █▀   ▀  █ █  █  ▄▀  
 ██   █ █   █ █   ▀  █     ██▄▄    █▄▄█ █▀▀▌   
 █ █  █ █   █ █▄  ▄▀ ███▄  █▄   ▄▀ █  █ █  █   
 █  █ █ █▄ ▄█ ▀███▀      ▀ ▀███▀      █   █    
 █   ██  ▀▀▀                         █   ▀     
                                    ▀          
 ▄█    ▄     ▄▀  ▄███▄      ▄   ▄█ ████▄ █▄▄▄▄ 
 ██     █  ▄▀    █▀   ▀      █  ██ █   █ █  ▄▀ 
 ██ ██   █ █ ▀▄  ██▄▄    ██   █ ██ █   █ █▀▀▌  
 ▐█ █ █  █ █   █ █▄   ▄▀ █ █  █ ▐█ ▀████ █  █  
  ▐ █  █ █  ███  ▀███▀   █  █ █  ▐         █   
    █   ██               █   ██           ▀    
  ┌─┐┌─┐┌┬┐┬ ┬┌─┐
  └─┐├┤  │ │ │├─┘
  └─┘└─┘ ┴ └─┘┴                                              
 """)

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def game_install():
    fetch_file("https://raw.githubusercontent.com/1ventorus/nuclear_ingenior/main/nuclear_ingenior.py", "nuclear_ingenior.py")
    os.system("cls")
    print(BANNER)
    print("launcher installé")
    time.sleep(2)

def requierment_install():
    fetch_file("https://raw.githubusercontent.com/1ventorus/nuclear_ingenior/main/game_system.py", "game_system.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/nuclear_ingenior/main/maj.py", "maj.py")
    os.system("cls")
    print(BANNER)
    print("requierment installé")
    time.sleep(2)

while True:
    os.system("cls")
    print(BANNER)
    print("installez le jeu ?  y/o")
    command= input(">>>")

    if command=="y":
        game_install()
        requierment_install()

    elif command=="o":
        os.system("cls")
        print("au revoir !")
        time.sleep(2)
        os.system("cls")
        break
