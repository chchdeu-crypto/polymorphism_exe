#mission 1
class Divice:
    def __init__(self,name):
        self.name=name
    def activate(self,):
        print(f"Device {self.name} is now on")
class SmartTV(Divice):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"TV {self.name} is playing the home screen.")
class SmartSpeaker(Divice):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
       print(f"Speaker {self.name} is ready to play music")  
d1=SmartTV("samsung")
d2=SmartSpeaker("echo")
d1.activate()
d2.activate()

#mission 2
class Divice:
    def __init__(self,name):
        self.name=name
    def deactivate(self):
        print(f"Device {self.name} is now off.")
class SmartLamp(Divice):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"Lamp {self.name} is dimming and turning off.")
class SmartAC(Divice):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"AC {self.name} is cooling down and switching off.")
lamp=SmartLamp("Bedroom Lamp")
ac=SmartAC("living room AC")
lamp.deactivate()
ac.deactivate()

#mission 3
class Device:
    def __init__(self,name,is_on):
        self.name=name
        self.is_on=is_on
    def status(self):
        pass
class SmartTV(Device):
    def __init__(self, name, is_on,channel):
        super().__init__(name, is_on)
        self.channel=channel   
    def status(self):
        if self.is_on:
            print(f"{self.name}: on, watching channel {self.channel}")
        else:
            print(f"{self.name}: off")
class SmartSpeaker(Device):
    def __init__(self, name, is_on,song):
        super().__init__(name, is_on)
        self.song=song
    def status(self):
        if self.is_on:
            print(f"{self.name}: on, play {self.song}")
        else:
            print(f"{self.name}: off")
tv=SmartTV("LG", True, 8)   
speaker=SmartSpeaker("Alexa", True, "Bohemian Rhapsody")   
tv.status()
speaker.status()

#mission 4
class Device:
    def __init__(self,name):
        self.name=name
    def activate(self):
        pass
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"TV {self.name} is playing the home screen.")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"{self.name} is glowing warmly.")
class SmartSpeaker(Divice):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"speaker {self.name} is ready to play music")
devices = [SmartTV("LG"), SmartLamp("Desk Lamp"), SmartSpeaker("Echo")]
for d in devices:
    d.activate()

#mission 5
class Device:
    def __init__(self,name):
        self.name=name
    def set_volume(self):
        pass
class SmartSpeaker(Device):
    def __init__(self, name,level):
        super().__init__(name)
        self.level=level
    def set_volume(self):
        if self.level<=7:
            print(f"Speaker {self.name} is now at volume {self.level}/10")    
        else:
            print(f"Loud!")
class SmartTV(Device):
    def __init__(self, name,level):
        super().__init__(name)
        self.level=level
    def set_volume(self):
        if self.level==0:
            print("Muted")
        else:
            print(f"TV {self.name} volume: {self.level}")
speaker=SmartSpeaker("bose",6)
tv=SmartTV("lg",5)
speaker.set_volume()
tv.set_volume()

#mission 6
class Device:
    def __init__(self,name):
        self.name=name
    def run_command(self,cmd):
        self.cmd=cmd
        pass
class Smartdoor(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"Device {self.name} received command: {cmd} to unlock.")
class Smartcamera(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"Device {self.name} received command: {cmd} to take a shot.")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"Device {self.name} received command: {cmd} power on.")
class Smartlump(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"Device {self.name} received command: {cmd} to turn on .")
devices=[Smartdoor("yale"),Smartcamera("cannon"),SmartAC("LG"),Smartlump("nisko")]
def send_command(devices, cmd):
    for divace in devices:
        divace.run_command(cmd)
send_command(devices,"start")