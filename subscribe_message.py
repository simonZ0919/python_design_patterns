"""
subscriber: subscribe topic(type of message)
publisher: publish message to dispatcher
dispatcher: middleware, subscribe/unsubscribe, pass message to subscriber
"""


class Message(object):
    def __init__(self):
        self.payload = None
        self.topic = 'All'


class Subscriber(object):
    def __init__(self, dispatcher, topic):
        dispatcher.subscribe(self, topic)

    def process(self, message):
        print("Message: {}".format(message.payload))


class Publisher(object):
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def publish(self, message):
        self.dispatcher.send(message)


class Dispatcher(object):
    def __init__(self):
        self.topic_subscribers = dict()

    def subscribe(self, subscriber, topic):
        self.topic_subscribers.setdefault(topic, set()).add(subscriber)

    def unsubscribe(self, subscriber, topic):
        self.topic_subscribers.setdefault(topic, set()).discard(subscriber)

    def unsubscribe_all(self, topic):
        self.subscribers = self.topic_subscribers[topic] = set()

    def send(self, message):
        for subscriber in self.topic_subscribers[message.topic]:
            subscriber.process(message)


def main():
    dispatcher = Dispatcher()
    publisher = Publisher(dispatcher)
    subscriber = Subscriber(dispatcher, 'my topic')

    message = Message()
    message.payload = "My payload"
    message.topic = 'my topic'

    publisher.publish(message)


if __name__ == '__main__':
    main()
