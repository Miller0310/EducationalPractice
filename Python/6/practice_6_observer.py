class Observer:
    def __init__(self, operation, action):
        self.operation = operation
        self.action = action

    def update(self, operation, action):
        if operation is self.operation:
            self.action(operation, action)