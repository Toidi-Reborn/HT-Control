

from tkinter import *
from classes.control import receiver



rec = receiver("192.168.1.252", 8102, 100)

def placeholder():
    print("temp")
def RECON():
    print(rec.sendCommand(rec.power("on")))
def RECOFF():
    print(rec.sendCommand(rec.power("off")))
def VOLUP():
    print(rec.sendCommand(rec.volume("up")))
def VOLDOWN():
    print(rec.sendCommand(rec.volume("down")))
def VOLMUTE():
    print(rec.sendCommand(rec.mute()))
def IHDMI1():
    print(rec.sendCommand(rec.input("hdmi1")))
def IHDMI2():
    print(rec.sendCommand(rec.input("hdmi2")))
def IHDMI3():
    print(rec.sendCommand(rec.input("hdmi3")))
def IHDMI4():
    print(rec.sendCommand(rec.input("hdmi4")))
def IHDMI5():
    print(rec.sendCommand(rec.input("hdmi5")))
def IHDMI6():
    print(rec.sendCommand(rec.input("hdmi6")))
def IHDMI7():
    print(rec.sendCommand(rec.input("hdmi7")))
def IBD():
    print(rec.sendCommand(rec.input("bd")))
def ICABLE():
    print(rec.sendCommand(rec.input("cable")))
def ITIVO():
    print(rec.sendCommand(rec.input("tivo")))
def IHDMIC():
    print(rec.sendCommand(rec.input("hdmiC")))
def ZONE2ON():
    print(rec.sendCommand(rec.zone2("on", "n/a")))
def ZONE2OFF():
    print(rec.sendCommand(rec.zone2("off", "n/a")))
def ZONE2VUP():
    print(rec.sendCommand(rec.zone2("vol", "up")))
def ZONE2VDOWN():
    print(rec.sendCommand(rec.zone2("vol", "down")))
def ZONE3ON():
    print(rec.sendCommand(rec.zone3("on" , "n/a")))
def ZONE3OFF():
    print(rec.sendCommand(rec.zone3("off", "n/a")))
def ZONE3VUP():
    print(rec.sendCommand(rec.zone3("vol", "up")))
def ZONE3VDOWN():
    print(rec.sendCommand(rec.zone3("vol", "down")))



rec.volume("up")
rec.volume("down")
rec.power("off")
rec.input("tivo")
#zones - 1st part: on, off, cycle, vol, ic = input change
#zones - 2nd part: doesnt matter for on, off, cycle.  ic needs input. vol needs up, down, mute
rec.zone2("ic", "pan") # chnages zone2 input to pan (Pandora)
rec.zone3("off", "tivo") # turns zone3 off - tivo means nothing
rec.zoneHD("vol", "up") # turns volume up in HDzone
rec.zone2("vol", "mute") # toggle mute in zone2
rec.output("bothon")

#test = input("test what?")
#rec.input(test)
#print(tv.rtTest())

print(rec.sendCommand(rec.volume("up")))

base = Tk()
base.title("Receiver Controller")
base.config(bg = "black", bd = 10, relief = RIDGE)

gui = Frame(base)
gui.config(bd = 10)
gui.grid(row = 0, column = 0, pady = 10, padx = 10)

rp1 = Label(gui, text = "Receiver Power")
rp1.grid(row = 0, column = 0, columnspan = 2)
pon = Button(gui, text = "On", command = RECON, width = 10)
pon.grid(row = 1, column = 0)
poff = Button(gui, text = "Off", command = RECOFF, width = 10)
poff.grid(row = 1, column = 1)

v1 = Label(gui, text = "Main Volume")
v1.grid(row = 3, column = 0, columnspan = 2)
vup = Button(gui, text = "Up", command = VOLUP, width = 10)
vup.grid(row = 4, column = 0)
vdown = Button(gui, text = "Down", command = VOLDOWN, width = 10)
vdown.grid(row = 4, column = 1)

out1 = Label(gui, text = "Outputs")
out1.grid(row = 6, column = 0, columnspan = 2)
out1on = Button(gui, text = "1 ON", command = placeholder, width = 10)
out1on.grid(row = 7, column = 0)
out2on = Button(gui, text = "2 ON", command = placeholder, width = 10)
out2on.grid(row = 7, column = 1)
outbon = Button(gui, text = "Both On", command = placeholder, width = 20)
outbon.grid(row = 8, column = 0, columnspan = 2)
outboff = Button(gui, text = "Both Off", command = placeholder, width = 20)
outboff.grid(row = 9, column = 0, columnspan = 2)

colspacer = Label(gui, text = "")
colspacer.grid(row = 0, column = 2, padx = 10)

i1 = Label(gui, text = "Inputs")
i1.grid(row = 0, column = 3)
ib1 = Button(gui, text = "HDMI 1", command = IHDMI1, width = 20)
ib1.grid(row = 1, column = 3)
ib2 = Button(gui, text = "HDMI 2", command = IHDMI2, width = 20)
ib2.grid(row = 2, column = 3)
ib3 = Button(gui, text = "HDMI 3", command = IHDMI3, width = 20)
ib3.grid(row = 3, column = 3)
ib4 = Button(gui, text = "HDMI 4", command = IHDMI4, width = 20)
ib4.grid(row = 4, column = 3)
ib5 = Button(gui, text = "HDMI 5", command = IHDMI5, width = 20)
ib5.grid(row = 5, column = 3)
ib6 = Button(gui, text = "HDMI 6", command = IHDMI6, width = 20)
ib6.grid(row = 6, column = 3)
ib7 = Button(gui, text = "HDMI 7", command = IHDMI7, width = 20)
ib7.grid(row = 7, column = 3)
ib8 = Button(gui, text = "DVD / BD", command = IBD, width = 20)
ib8.grid(row = 8, column = 3)
ib9 = Button(gui, text = "Cable", command = ICABLE, width = 20)
ib9.grid(row = 9, column = 3)
ib10 = Button(gui, text = "Tivo", command = ITIVO, width = 20)
ib10.grid(row = 10, column = 3)
ib11 = Button(gui, text = "Cycle Input", command = IHDMIC, width = 20)
ib11.grid(row = 11, column = 3)

colspacer2 = Label(gui, text = "")
colspacer2.grid(row = 0, column = 4, padx = 10)

z2 = Label(gui, text = "Zone 2")
z2.grid(row = 0, column = 5, columnspan = 2)
z2on = Button(gui, text = "On", command = ZONE2ON, width = 10)
z2on.grid(row = 1, column = 5)
z2off = Button(gui, text = "Off", command = ZONE2OFF, width = 10)
z2off.grid(row = 1, column = 6)
z2vol = Label(gui, text = "Volume")
z2vol.grid(row = 3, column = 5, columnspan = 2)
z2vup = Button(gui, text = "Up", command = ZONE2VUP, width = 10)
z2vup.grid(row = 4, column = 5)
z2vdown = Button(gui, text = "Down", command = ZONE2VDOWN, width = 10)
z2vdown.grid(row = 4, column = 6)

colspacer3 = Label(gui, text = "")
colspacer3.grid(row = 0, column = 7, padx = 10)

z3 = Label(gui, text = "Zone 3")
z3.grid(row = 0, column = 8, columnspan = 2)
z3on = Button(gui, text = "On", command = ZONE3ON, width = 10)
z3on.grid(row = 1, column = 8)
z3off = Button(gui, text = "Off", command = ZONE3OFF, width = 10)
z3off.grid(row = 1, column = 9)
z3vol = Label(gui, text = "Volume")
z3vol.grid(row = 3, column = 8, columnspan = 2)
z3vup = Button(gui, text = "Up", command = ZONE3VUP, width = 10)
z3vup.grid(row = 4, column = 8)
z3vdown = Button(gui, text = "Down", command = ZONE3VDOWN, width = 10)
z3vdown.grid(row = 4, column = 9)


gui.mainloop()







