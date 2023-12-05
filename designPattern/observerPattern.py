class Observer:
    def __init__(self):
        self.observers = []
        self.msg = ""

    def notify(self, event_data):
        for observer in self.observers:
            observer.notify(event_data)

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)


class SMSNotifier:
    def notify(self, event_data):
        print(event_data, "received by SMS")
        print("send sms")


class EmailNotifier:
    def notify(self, event_data):
        print(event_data, "received by Email")
        print("send email")


class PushNotifier:
    def notify(self, event_data):
        print(event_data, "received by Push")
        print("send push notification")


notifier = Observer()

SMSNotifier = SMSNotifier()
EmailNotifier = EmailNotifier()
PushNotifier = PushNotifier()

notifier.register(SMSNotifier)
notifier.register(EmailNotifier)
notifier.register(PushNotifier)

notifier.notify("user activation recived..")
