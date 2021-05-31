from practice_6_observer import Observer


class EventManager:
    def __init__(self):
        self._observers = []

    def subscribe(self, Observer):
        if not Observer in self._observers:
            self._observers.append(Observer)

    def event(self, operation, action):
        for observer in self._observers:
            observer.update(operation, action)
