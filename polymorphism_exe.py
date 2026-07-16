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

#mission 7
class Device:
    def __init__(self,name):
        self.name=name
    def run_schedule(self,hour):
        pass
class SmartLamp(Device):
    def __init__(self,name):
        super().__init__(name)
    def run_schedule(self, hour):
        if 18<=hour<=23:
            print(f"{self.name}: turning on")
        else:
            print(f"{self.name}: turning off")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self, hour):
        if 12<=hour<=20:
            print(f"{self.name}: turning on")
        else:
            print(f"{self.name}: turning off")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self, hour):
        if 20<=hour<=23:
            print(f"{self.name}: turning on")
        else:
            print(f"{self.name}: turning off")
lamp=SmartLamp("nisko")
ac=SmartAC("bosch")
tv=SmartTV("sansung")
lamp.run_schedule(21)
ac.run_schedule(21)
tv.run_schedule(21)

#mission 8
class Device:
    def __init__(self,name):
        self.name=name
    def energy_usege(self):
        pass
class SmartTV (Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usege(self):
        return 150
class  SmartAC (Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usege(self):
        return 900
class SmartLamp (Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usege(self):
        return 8
class SmartSpeaker (Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usege(self):
        return 30
devices=[SmartTV("lg"),SmartAC("bosch"),SmartLamp("nisko"),SmartSpeaker("jbl")]
total=0
for d in devices:
    print(f"{d.__class__.__name__}: {d.energy_usege()}W")
    total+=d.energy_usege()
print(total)

#mission 9
class Device:
    def __init__(self,name):
        self.name=name
        self.is_on=False
    def activate(self):
        pass
    def deactivate(self):
        pass
    def status(self):
        pass
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"TV {self.name}: on")
        self.is_on=True
    def deactivate(self):
        print(f"TV {self.name}: off ")
        self.is_on=False
    def status(self):
        if self.is_on:
            print(f"smartTV {self.name}: is on ")
        else:
            print(f"smartTV {self.name}: is off")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"SmartAC {self.name}: on")
        self.is_on=True
    def deactivate(self):
        print(f"SmartAC {self.name}: off ")
        self.is_on=False
    def status(self):
        if self.is_on:
            print(f"SmartAC {self.name}: is on ")
        else:
            print(f"SmartAC {self.name}: is off")
class Smartdoor(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"Smartdoor {self.name}: lock")
        self.is_on=True
    def deactivate(self):
        print(f"Smartdoor {self.name}: unlock ")
        self.is_on=False
    def status(self):
        if self.is_on:
            print(f"Smartdoor {self.name}: is lock ")
        else:
            print(f"Smartdoor {self.name}: is unlok")
class SmartLight(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"SmartLight {self.name}: on")
        self.is_on=True
    def deactivate(self):
        print(f"SmartLight {self.name}: off ")
        self.is_on=False
    def status(self):
        if self.is_on:
            print(f"SmartLight {self.name}: is on ")
        else:
            print(f"SmartLight {self.name}: is off")
class SmartCamera(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"SmartCamera {self.name}: on")
        self.is_on=True
    def deactivate(self):
        print(f"SmartCamera {self.name}: off ")
        self.is_on=False
    def status(self):
        if self.is_on:
            print(f"SmartCamera {self.name}: is on ")
        else:
            print(f"SmartCamera {self.name}: is off")
class HomeSystem:
    def __init__(self):
        self.devices=[SmartTV("LG"),SmartAC("bosch"),Smartdoor("yale"),SmartLight("nisko"),SmartCamera("cannon")]
    def activate_all(self):
        for d in self.devices:
            d.activate()
    def deactivate_all(self):
        for d in self.devices:
            d.deactivate()
    def system_report(self):
        for d in self.devices:
            d.status()
home=HomeSystem()
home.activate_all()
home.deactivate_all()
home.system_report()

#mission 10
class Device:
    def __init__(self,name):
        self.name=name
    def trigger_alarm(self,alert_type):
        pass
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def trigger_alarm(self, alert_type):
        print(f"lamp {self.name} is flashing: {alert_type}")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def trigger_alarm(self, alert_type):
        print(f" speaker {self.name}: is playing alram {alert_type}")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def trigger_alarm(self, alert_type):
        print(f"TV {self.name}: is showing emergency  {alert_type}")
class SmartDoorLock(Device):
    def __init__(self, name):
        super().__init__(name)
    def trigger_alarm(self, alert_type):
        print(f"door {self.name}: locked {alert_type}")
class AlarmSystem:
    def __init__(self):
        self.devices=[SmartLamp("nisko"),SmartSpeaker("JBL"),SmartTV("LG"),SmartDoorLock("yale")]
    def send_alert(self,alert_type):
        for d in self.devices:
            d.trigger_alarm(alert_type)
arm=AlarmSystem()
arm.send_alert("fire")
arm.send_alert("break in")
