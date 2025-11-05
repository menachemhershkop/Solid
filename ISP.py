#1
# class ISoldier:
#     def shoot(self):
#         print('shoot')
#     def navigate(self):
#         print('navigate')
#     def call_air_support(self):
#         print('call air support')
# class Infantry(ISoldier):
#     def ability(self):
#         self.shoot()
#         self.navigate()
# class ForwardObserver(ISoldier):
#     def ability(self):
#         self.shoot()
#         self.call_air_support()
# class Pilot(ISoldier):
#     def ability(self):
#         self.call_air_support()
#Poor distribution and allocation of resources
from pydoc import classify_class_attrs


class ISoldier:
    pass
class IShooter(ISoldier):
    pass
class INavigator(ISoldier):
    pass
class IAirSupportCaller(ISoldier):
    pass
class Infantry(ISoldier,INavigator):
    def ability(self):
        print("I am shooting an navigate")
class ForwardObserver(IShooter,IAirSupportCaller):
    def ability(self):
        print("I am shooting and call to air force")
class Pilot(IAirSupportCaller):
    def ability(self):
        print("I am calling to air force")

#2
# class IVehicle:
#     def drive(self):
#         print("I am drive")
#     def fly(self):
#         print("I am fly")
#     def sail(self):
#         print("I am sail")
# class Tank(IVehicle):
#     def ability(self):
#         self.drive()
# class FighterJet(IVehicle):
#     def ability(self):
#         self.fly()
#         self.drive()
# class Submarine(IVehicle):
#     def ability(self):
#         self.sail()
# Since everyone comes to fulfill something different, there will be things that will not be realized.
class IVehicle:
    pass
class IDrive(IVehicle):
    pass
class IFly(IVehicle):
    pass
class ISail(IVehicle):
    pass
class Tank(IDrive):
    def ability(self):
        print("I'm drive")
class FighterJet(IDrive,IFly):
    def ability(self):
        print("I'm flies, drives on runway")
class Submarine(ISail):
    def ability(self):
        print("i'm sail underwater")
#3
# class ICommSystem:
#     def send_radio(self):
#         print("radio")
#     def send_satellite(self):
#         print("satellite")
#     def send_morse_code(self):
#         print("morse code")
# class FieldRadio(ICommSystem):
#     def ability(self):
#         self.send_radio()
# class SatelliteComm(ICommSystem):
#     def ability(self):
#         self.send_satellite()
# class LegacyMorseUnit(ICommSystem):
#     def ability(self):
#         self.send_morse_code()
#Each department implements only one method
class ICommSystem:
    pass
class IRadioComm(ICommSystem):
    pass
class ISatellite(ICommSystem):
    pass
class IMorseComm(ICommSystem):
    pass
class FieldRadio(IRadioComm):
    def ability(self):
        print("Radio")
class SatelliteComm(ISatellite):
    def ability(self):
        print("Satellite")
class LegacyMorseUnit(IMorseComm):
    def ability(self):
        print("morse")