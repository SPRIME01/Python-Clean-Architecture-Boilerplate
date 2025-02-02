from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Type

class Event:
    pass

class EventHandler(ABC):
    @abstractmethod
    def handle(self, event: Event):
        pass

class EventBus(ABC):
    @abstractmethod
    def publish(self, event: Event):
        pass

    @abstractmethod
    def subscribe(self, event_type: Type[Event], handler: EventHandler):
        pass

class SimpleEventBus(EventBus):
    def __init__(self):
        self._handlers: Dict[Type[Event], List[EventHandler]] = {}

    def publish(self, event: Event):
        event_type = type(event)
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                handler.handle(event)

    def subscribe(self, event_type: Type[Event], handler: EventHandler):
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)
