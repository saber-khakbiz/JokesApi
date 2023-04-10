from err_handel import JokeAPIError
from cowsay import cow, pig, beavis, get_output_string
from joke import Joke
import requests
import json



#!=============================First Class=======================================
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

#!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#!==================================Third Class=======================================
# Create a class JokeAPI Chuck Norris that also inherits from the Joke abstract class

class JokeAPIChuckNorris(Joke):

    def get_random_joke(self, category="animal"):
        # How many results to return. Must be between 1 and 30. Default is 1.
        self.category = category
        category_lst = ['animal', 'career', 'celebrity', 'dev', 'explicit',
                        'fashion', 'food', 'history', 'money', 'movie',
                        'music', 'political', 'religion', 'science', 'sport', 'travel']

        if self.category in category_lst:
            api_url = 'https://api.chucknorris.io/jokes/random?category={}'.format(
                self.category)
            response = requests.get(api_url)

            if response.status_code == requests.codes.ok:

                joke = json.loads(response.text)
                beavis(joke["value"])

            else:
                print("Error:", response.status_code, response.text)

        else:
            print("404 Category Not Found")

#!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



