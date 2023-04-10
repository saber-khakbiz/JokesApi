from err_handel import NoInternetConnectionError
from cowsay import get_output_string
from abc import ABC, abstractmethod
import socket

# Create an abstract class Joke that contains an abstract method get_random_joke


class Joke(ABC):

    def __init__(self) -> None:
        try:
            # Try to establish a connection to google DNS server
            socket.create_connection(('8.8.8.8', 53), timeout=3)
        except OSError:
            # If a connection could not be established, raise an error
            raise NoInternetConnectionError(
                get_output_string('tux', 'No internet connection'))

    @abstractmethod
    def get_random_joke(self):
        pass
