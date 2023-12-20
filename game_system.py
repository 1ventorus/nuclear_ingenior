#!/usr/bin/env python

import os
import time
import threading

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
                                              
 """)
Help=("""
    start : lance 1 simulation
    add cool1 : augmente la vitesse de la pompe 1
    remove cool1 : reduit la viteese de la pompe 1
    add cool2 : augmente la vitesse de la pompe 2
    remove cool2 : reduit la viteese de la pompe 2
    add power : augmente la puissance du coeur
    remove power power : reduit la puissance du coeur
    add tour : augmente la simulation de 1 tour
    remove tour : reduit la simultion de 1 tour
    save : sauvegarde l'état du réacteur
""")

efficacity = 1
tour = 50

# action sur le réacteur
class ToolSystem:
    def __init__(self):
        self.cool1 = 50
        self.cool2 = 50
        self.coolingspeed = (self.cool1+self.cool2)/2
        self.powerLevel = 1

    def increase_pump_speed1(self):
        if self.cool1 < 100:
            self.cool1 += 10
        self.coolingspeed = (self.cool1+self.cool2)/2

    def decrease_pump_speed1(self):
        if self.cool1 > 0:
            self.cool1 -= 10
        self.coolingspeed = (self.cool1+self.cool2)/2

    def increase_pump_speed2(self):
        if self.cool2 < 100:
            self.cool2 += 10
        self.coolingspeed = (self.cool1+self.cool2)/2

    def decrease_pump_speed2(self):
        if self.cool2 > 0:
            self.cool2 -= 10
        self.coolingspeed = (self.cool1+self.cool2)/2

    def increase_power_level(self):
        if self.powerLevel <10:
            self.powerLevel += 1

    def decrease_power_level(self):
        if self.powerLevel > 0:
            self.powerLevel -= 1

TS = ToolSystem()

# propriété
class CoreSystem:
    def __init__(self):
        self.temp = 0
        self.pv = 100

CS = CoreSystem()

class ArmorSystem:
    def __init__(self):
        self.temp = 0
        self.pv = 100
    
AS = ArmorSystem()

class PlayerInfo:
    def __init__(self):
        self.pv = 100
        self.xp = 0
    
PI = PlayerInfo()

def hall():
    os.system("cls")
    print(BANNER)
    print("joueur :")
    print(f"pv : {PI.pv}         xp : {PI.xp}")
    print("")
    print("coeur :")
    print(f"pv : {CS.pv}         temperature : {CS.temp} k")
    print("")
    print("bouclier :")
    print(f"pv : {AS.pv}         temperature : {AS.temp} k")
    print("")
    print("puissance des pompes      |    puissance du réacteur")
    print("__________________________|_________________________")
    print(f" 1 : {TS.cool1} %                    {TS.powerLevel}")
    print(f" 2 : {TS.cool2} %                 ")
    print(f" total : {TS.coolingspeed} %     ")
    print(f"nombre de tour par sim : {tour}")

class SimulationThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            for i in range(tour):
                hall()

                if (TS.powerLevel*10) > TS.coolingspeed:
                    CS.temp += 2*TS.powerLevel
                    if CS.pv < 50:
                        AS.temp +=1*(TS.powerLevel*2)
                    else:
                        AS.temp += 1*TS.powerLevel

                elif (TS.powerLevel*10)==TS.coolingspeed:
                    pass

                else:
                    CS.temp -= 1*TS.powerLevel
                    if CS.pv < 50:
                        AS.temp -=1*(TS.powerLevel/2)
                    else:
                        AS.temp -= 1*TS.powerLevel

                if CS.temp > 10000:
                    if CS.pv>0:
                        CS.pv -=1

                if AS.temp > 6000:
                    if AS.pv>0:
                        AS.pv -= 1

                if AS.pv <50:
                    if PI.pv >0:
                        PI.pv -= 1

                time.sleep(TS.coolingspeed/50)
            self.running = False

    def stop(self):
        self.running = False
        hall()
ST = SimulationThread()

def save():
    with open("save_games.txt", "w+") as fichier:
        fichier.write(str(PI.pv) + "\n")
        fichier.write(str(PI.xp) + "\n")
        fichier.write(str(CS.pv) + "\n")
        fichier.write(str(CS.temp) + "\n")
        fichier.write(str(AS.pv) + "\n")
        fichier.write(str(AS.temp) + "\n")
        fichier.write(str(efficacity) + "\n")
        fichier.write(str(TS.powerLevel) + "\n")

if os.path.exists("save_games.txt"):
    with open("save_games.txt", "r") as file:
        info = file.read()
        saved = info.splitlines()
        PI.pv = int(saved[0])
        PI.xp = int(saved[1])
        CS.pv = int(saved[2])
        CS.temp = int(saved[3])
        AS.pv = int(saved[4])
        AS.temp = int(saved[5])
        efficacity = int(saved[6])
        TS.powerLevel = int(saved[7])
    
while True:
    os.system("cls")
    print(BANNER)

    print("lancer le réacteur y/o")
    home = input(">>>")

    if home=="y":
        hall()
        while True:
            
            if PI.pv==0:
                os.system("cls")
                print("oh non vous êtes mort !")
                break

            if CS.pv==0:
                os.system("cls")
                print(" vous avez fais exploser le coeur avec vous !")
            
            player = input(">>>")
            if player=="start":
                ST.start()

            elif player=="add tour":
                tour +=10
                hall()

            elif player=="remove tour":
                if tour >0:
                    tour-=10
                hall()

            elif player=="add cool1":
                TS.increase_pump_speed1()
                hall()

            elif player=="remove cool1":
                TS.decrease_pump_speed1()
                hall()

            elif player=="add cool2":
                TS.increase_pump_speed2()
                hall()

            elif player=="remove cool2":
                TS.decrease_pump_speed2()
                hall()

            elif player=="add power":
                TS.increase_power_level()
                hall()
            
            elif player=="remove power":
                TS.decrease_power_level()
                hall()

            elif player=="help":
                hall()
                print(Help)

            elif player=="clear":
                hall()

            elif player=="save":
                save()

            elif player=="stop":
                ST.stop()
                break
        
    elif home=="o":
        os.system("cls")
        break

