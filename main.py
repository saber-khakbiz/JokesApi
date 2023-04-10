from jokesapi import JokeAPIY, JokeAPINinjas, JokeAPIChuckNorris
from cowsay import cow


if __name__ == "__main__":

    # class JokeAPIY
    joke_api_y = JokeAPIY()
    joke1 = joke_api_y.get_random_joke()
    cow(joke1)

    # class JokeAPI Ninjas
    joke_api_ninjas = JokeAPINinjas()
    joke2 = joke_api_ninjas.get_random_joke(limit=1)

    # class JokeAPI Chuck Norris
    joke_api_chuck_norris = JokeAPIChuckNorris()
    joke3 = joke_api_chuck_norris.get_random_joke(category="sport")
