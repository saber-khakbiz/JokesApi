import requests
from abc import ABC, abstractmethod

# Create an abstract class Joke that contains an abstract method get_random_joke


class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass
