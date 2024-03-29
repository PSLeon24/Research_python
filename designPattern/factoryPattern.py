class AndroidSmartphone:
    def send(self, message):
        print("send a message via Android platform")


class WindowsSmartphone:
    def send(self, message):
        print("send a message via Window Mobile platform")


class iOSSmartphone:
    def send(self, message):
        print("send a message via iOS platform")


# Create a factory class
class SmartphoneFactory(object):
    def __init__(self):
        pass

    def create_smartphone(self, devicetype):
        if devicetype == "android":
            smartphone = (
                AndroidSmartphone()
            )  # <-- create a real object in factory class.
        elif devicetype == "window":
            smartphone = (
                WindowsSmartphone()
            )  # <-- create a real object in factory class.
        elif devicetype == "ios":
            smartphone = iOSSmartphone()  # <-- create a real object in factory class.
        return smartphone


# Create detailed objects via factory class
smartphone_factory = SmartphoneFactory()
message_sender1 = smartphone_factory.create_smartphone("android")
message_sender1.send("hi")

message_sender2 = smartphone_factory.create_smartphone("window")
message_sender2.send("hello")

message_sender3 = smartphone_factory.create_smartphone("ios")
message_sender3.send("are you there?")
