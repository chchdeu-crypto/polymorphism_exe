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