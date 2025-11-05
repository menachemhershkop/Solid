#1
class Shape:
    def area(self):
        print(area)
class Circle(Shape):
    def __init__(self,r):
        self.radios=r
    def area(self):
        return self.r**2*3.14
class Square(Shape):
    def __init__(self,a):
        self.square=a
    def area(self):
        return a*a
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.width*self.width
#2
class Payment:
    def pay(self,amount):
        print("payment cash ",amount)
class CreditCardPayment(Payment):
    def pay(self,amount):
        print("payment via credit card ",amount)
class PayPalPayment(Payment):
    def pay(self,amount):
        print("payment via PayPal ",amount)
class CryptoPayment(Payment):
    def pay(self,amount):
        print("payment via crypto ",amount)
#3
class Notifier:
    def send(self,message):
        print(message,"message send...")
class EmailNotifier(Notifier):
    def send(self,message):
        print(message,"message send by email")
class SMSNotifier(Notifier):
    def send(self,message):
        print(message,"message send by SMS")
class PushNotifier(Notifier):
    def send(self,message):
        print(message,"push message send...")