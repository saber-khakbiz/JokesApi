import requests
from abc import ABC, abstractmethod

# Create an abstract class Joke that contains an abstract method get_random_joke


class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass

# Create a class JokeAPIY that also inherits from the JokeAPI abstract class
class JokeAPIY(Joke):
    def get_random_joke(self):
        # Send a GET request to the JokeAPIY API and get the response
        response = requests.get('https://v2.jokeapi.dev/joke/Any')
        # Convert the response to JSON format
        json_data = response.json()
        # Extract the joke and return it
        return json_data['setup'] + '\n' + json_data['delivery']
    
    

joke_api_y = JokeAPIY()
joke1 = joke_api_y.get_random_joke()
print(joke1)