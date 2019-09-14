import telnetlib

'''
        with telnetlib.Telnet(self.host, self.port, self.timeout) as session:
            session.write(b, "")
'''


class printTest:
    def helloP(self):
        print("This is Hello")

    def goodbye(self):
        print("This is goodbye")


class receiver:
    hostIP = ""
    port = ""
    timeout = ""
    choiceDir = {
        "bd": "25",
        "dvd": "04",
        "cable": "06",  # sat/cbl
        "tivo": "15",  # dvr/bdr
        "hdmi1": "19",
        "hdmi2": "20",
        "hdmi3": "21",
        "hdmi4": "22",
        "hdmi5": "23",
        "hdmi6": "24",
        "hdmi7": "34",
        "hdmiC": "31",  # HDMI cycle
        "network": "26",  # network cycle
        "iRadio": "38",  # Internet Radio
        "spot": "53",  # Spotify
        "pan": "41",  # Pandora
        "mServer": "44",  # Media Server
        "usb": "17",  # Ipod/USB
        "tv": "05",
        "cd": "01",
        "usbDac": "13",
        "tuner": "02",
        "phono": "00",
        "mIn": "12",  # Multi Ch In
        "bt": "33",  # blutooth audio
        "cy": "cy"
    }
    choiceSound = {
        "STEREO (cyclic)": "0001",
        "STANDARD (cyclic)": "0010",
        "PRO LOGIC2 MOVIE": "0013",
        "PRO LOGIC2 MUSIC": "0014",
        "PRO LOGIC2 GAME": "0015",
        "PRO LOGIC": "0012",
        "Neo:6 CINEMA": "0016",
        "Neo:6 MUSIC": "0017",
        "Neo:X CINEMA": "0037",
        "Neo:X MUSIC": "0038",
        "Neo:X GAME": "0039",
        "Dolby Surround": "0040",
        "EXTENDED STEREO": "0041",
        "MTS DTS-ES Neo:6": "0025",
        "MTS DTS-ES matrix": "0026",
        "MTS DTS-ES discrete": "0027",
        "MTS Neo:X CINEMA ": "0043",
        "MTS Neo:X MUSIC": "0044",
        "MCS Neo:X GAME": "0045",
        "MCS Dolby Surround": "0050",
        "ADVANCED SURROUND (cycle)": "0100",
        "ACTION": "0101",
        "DRAMA": "0103",
        "ADVANCED GAME": "0118",
        "SPORTS": "0117",
        "CLASSICAL": "0107",
        "ROCK/POP": "0110",
        "Front Stage Surround Advance": "0003",
        "ECO MODE (cyclic)": "0200",
        "ECO MODE 1": "0212",
        "ECO MODE 2": "0213",
        "RETRIEVER AIR": "0153",
        "PHONES SURROUND": "0113",
        "AUTO SURR/STREAM DIRECT (cycle)": "0005",
        "AUTO SURROUND": "0006",
        "Auto Level Control (A.L.C.)": "0151",
        "DIRECT": "0007",
        "PURE DIRECT": "0008",
        "OPTIMUM SURROUND": "0152",
    }
    statusRequest = {
        "power": "?P",
        "volume": "?V",
        "mute": "?M",
        "aMode": "?L",
        "z2p": "?AP",
        "z3p": "?BP",
        "zHDp": "?ZEP",
        "z2i": "?ZS",
        "z3i": "?ZT",
        "zHDi": "?ZEA",
        "z2v": "?ZV",
        "z3v": "?YZ",
        "zHDv": "?HZV"
    }

    def __init__(self, hostIP, port, timeout):
        self.hostIP = hostIP
        self.port = port
        self.timeout = timeout

    def sendCommand(self, command):
        with telnetlib.Telnet(self.hostIP, self.port, self.timeout) as session:
            session.write(command)
        #return command

    def volume(self, x):
        error = False
        if x == "up":
            print("Volume Up - VU")
            x = "VU"
        elif x == "down":
            print("Volume Down - VD")
            x = "VD"
        else:
            error = True

        if error:
            x = "Entry Invalid"
        else:
            x = x + "<CR>"
        return x

    def power(self, x):
        #print("power Line")
        error = False
        if x == "on":
            print("On is selected")
            x = "PO"
        elif x == "off":
            print("Off is selected")
            x = "PF"
        elif x == "cycle":
            print("Cycling Power")
            x = "PZ"
        else:
            error = True

        if error:
            x = "Entry Invalid"
        else:
            x = x + "<CR>"
        return x


    def mute(self):
        print("MZ<CR>")

    def input(self, x):
        #print("input line")
        x = (self.choiceDir.get(x, "na"))
        if x == "na":
            x = "Invalid Entry"
        elif x == "cy":
            x = "FD<CR>"
        else:
            x = x + "FN<CR>"
        return x

    def zone2(self, x, i):
        #print("zone2 Line")
        choice = {
            "on": "APO<CR>",
            "off": "APF<CR>",
            "cycle": "ZSFU<CR>",
            "ic": "inputs",
            "vol": "vol"
        }
        x = (choice.get(x, "na"))
        if x == "inputs":
            x = (self.choiceDir.get(i,"na")) + "ZS<CR>"
        elif x == "vol":
            if i == "up":
                x = "ZU<CR>"
            elif i == "down":
                x = "ZD<CR>"
            elif i == "mute":
                x = "Z2MZ<CR>"
            else:
                print("Volume input invalid")
        return x

    def zone3(self, x, i):
        #print("Zone3 Line")
        choice = {
            "on": "BPO<CR>",
            "off": "BPF<CR>",
            "cycle": "ZTFU<CR>",
            "ic": "inputs",
            "vol": "vol"
        }
        x = (choice.get(x, "na"))
        if x == "inputs":
            x = (self.choiceDir.get(i, "na")) + "ZT<CR>"
        elif x == "vol":
            if i == "up":
                x = "YU<CR>"
            elif i == "down":
                x = "YD<CR>"
            elif i == "mute":
                x = "Z3MZ<CR>"
            else:
                print("Volumn input invalid")
        return x

    def zoneHD(self, x, i):
        #print("ZoneHD Line")
        choice = {
            "on": "ZEO<CR>",
            "off": "ZEF<CR>",
            "cycle": "ZSFU<CR>",
            "ic": "inputs",
            "vol": "vol"
        }
        x = (choice.get(x, "na"))
        if x == "inputs":
            x = (self.choiceDir.get(i, "na")) + "ZEA<CR>"
        elif x == "vol":
            if i == "up":
                x = "HZU<CR>"
            elif i == "down":
                x = "HZD<CR>"
            elif i == "mute":
                x = "HZMZ<CR>"
            else:
                print("Volumn input invalid")
        return x

    def output(self, x):
        #print("hdmi output line")
        if x == "ho1":
            x = "1"
        elif x == "ho2":
            x = "2"
        elif x == "bothon":
            x = "0"
        elif x == "off":
            x = "3"
        x = x + "HO<CR>"
        return x

    def soundMode(self, x):
        #print("Sound Mode Line")
        x = (self.choiceSound.get(x, "Sound Mode is Invalid"))
        x = x + "SR<CR>"
        return x

class tv:
    def rtTest(self):
        x = "Hello"
        return x
