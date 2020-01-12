"""
observer pattern: decouple objects
Observer: receive update
Observable: register/unregister/update_all
"""


class ConcreteObserver(object):
    def update(self, observed):
        print("Observing: {}".format(observed))


class Observable(object):
    def __int__(self):
        self.callbacks = set()

    def register(self, callback):
        self.callbacks.add(callback)

    def unregister(self, callback):
        self.callbacks.remove(callback)

    def unregister_all(self):
        self.callbacks = set()

    def update_all(self):
        for callback in self.callbacks:
            callback(self)


def main():
    observed = Observable()
    observer1 = ConcreteObserver()
    observed.register(lambda x: observer1.update(x))
    observed.update_all()


if __name__ == '__main__':
    main()
