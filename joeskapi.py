from err_handel import NoInternetConnectionError, JokeAPIError
from cowsay import cow, pig, get_output_string
from abc import ABC, abstractmethod
import requests
import socket
import json


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

#!=============================first Class=======================================
# Create a class JokeAPIY that also inherits from the Joke abstract class


class JokeAPIY(Joke):

    def get_random_joke(self):

        # Send a GET request to the JokeAPIY API and get the response
        response = requests.get('https://v2.jokeapi.dev/joke/Any')

        # Check if the response is successful (status code 200)
        if response.status_code != 200:
            raise JokeAPIError(
                get_output_string('fox', 'JokeAPIY API returned an error'))

        # Convert the response to JSON format
        json_data = response.json()

        # Check if the JSON response contains the 'setup' and 'delivery' keys
        if 'setup' not in json_data or 'delivery' not in json_data:
            raise JokeAPIError(
                get_output_string('fox', 'JokeAPIY API returned invalid data'))

        # Extract the joke and return it
        return json_data['setup'] + '\n' + json_data['delivery']

#!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#!=============================Seconde Class====================================
# Create a class JokeAPINinjas that also inherits from the Joke abstract class

class JokeAPINinjas(Joke):

    def get_random_joke(self, limit=1) -> str:
        # How many results to return. Must be between 1 and 30. Default is 1.
        self.limit = limit
        MY_API_KEY = '08grfo6DmJVnThqWHpaZQQ==ZjzPDIMiJY0x0xmh'
        api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(
            self.limit)
        # Send a GET request to the JokeAPINinjas API and get the response
        response = requests.get(api_url, headers={'X-Api-Key': MY_API_KEY})

        # Check if the response is successful (status code 200)
        if response.status_code == requests.codes.ok:
            joke_lst = json.loads(response.text)
            for joke in joke_lst:
                pig(joke["joke"])
        else:
            print("Error:", response.status_code, response.text)

#!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


if __name__ == "__main__":

    joke_api_y = JokeAPIY()
    joke1 = joke_api_y.get_random_joke()
    cow(joke1)

    # joke_api_ninjas = JokeAPINinjas()
    # joke2 = joke_api_ninjas.get_random_joke(limit=2)
