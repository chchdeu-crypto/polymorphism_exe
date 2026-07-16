#mission 1
class divice:
    def __init__(self,name):
        self.name=name
    def activate(self,):
        print(f"Device {self.name} is now on")
class SmartTV(divice):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"TV {self.name} is playing the home screen.")
class SmartSpeaker(divice):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
       print(f"Speaker {self.name} is ready to play music")  
d1=SmartTV("samsung")
d2=SmartSpeaker("echo")
d1.activate()
d2.activate()

#mission 2
class divice:
    def __init__(self,name):
        self.name=name
    def deactivate(self):
        print(f"Device {self.name} is now off.")
class SmartLamp(divice):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"Lamp {self.name} is dimming and turning off.")
class SmartAC(divice):
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