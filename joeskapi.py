import socket
import requests
from abc import ABC, abstractmethod
from err_handel import NoInternetConnectionError, JokeAPIError

# Create an abstract class Joke that contains an abstract method get_random_joke


class Joke(ABC):

    def __init__(self) -> None:
        try:
            # Try to establish a connection to google DNS server
            socket.create_connection(('8.8.8.8', 53), timeout=3)
        except OSError:
            # If a connection could not be established, raise an error
            raise NoInternetConnectionError('No internet connection')

    @abstractmethod
    def get_random_joke(self):
        pass


# Create a class JokeAPIY that also inherits from the JokeAPI abstract class


class JokeAPIY(Joke):

    def get_random_joke(self):

        # Send a GET request to the JokeAPIY API and get the response
        response = requests.get('https://v2.jokeapi.dev/joke/Any')

        # Check if the response is successful (status code 200)
        if response.status_code != 200:
            raise JokeAPIError('JokeAPIY API returned an error')

        # Convert the response to JSON format
        json_data = response.json()

        # Check if the JSON response contains the 'setup' and 'delivery' keys
        if 'setup' not in json_data or 'delivery' not in json_data:
            raise JokeAPIError('JokeAPIY API returned invalid data')

        # Extract the joke and return it
        return json_data['setup'] + '\n' + json_data['delivery']



if __name__ == "__main__":
    
    joke_api_y = JokeAPIY()
    joke1 = joke_api_y.get_random_joke()
    print(joke1)
