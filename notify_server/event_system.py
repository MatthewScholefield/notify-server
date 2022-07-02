class EventSystem:
    def __init__(self, print_messages=False):
        self.callbacks = {}
        self.print_messages = print_messages

    def send(self, event, data):
        event_data = {'type': 'event', 'event': event, 'data': data}
        if self.print_messages:
            print(event_data)
        for callback in self.callbacks.get(event, []):
            callback(event_data)

    def subscribe(self, event, callback):
        self.callbacks.setdefault(event, []).append(callback)

    def unsubscribe(self, event, callback):
        callbacks = self.callbacks[event]
        callbacks.remove(callback)
        if not callbacks:
            del self.callbacks[event]
