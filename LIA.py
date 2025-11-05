# class BirdUnit:
#     def fly():
#         print("I am flying...")
# class Drone(BirdUnit):
#     pass
# class Tank(BirdUnit):
#     pass
# Absurd tank can't fly

class FlyUnit:
    def fly():
        print("I am fly")
class GroundUnit:
    def drive():
        print("I am driving")
class Drone(FlyUnit):
    pass
class Tank(GroundUnit):
    pass