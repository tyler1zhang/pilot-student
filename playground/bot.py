from termcolor import colored
from time import sleep
from random import choice
from simpleeval import simple_eval


class Bot:
    wait = 1

    def __init__(self):
        self.q = ''
        self.a = ''

    def _think(self, s):
        return s

    def _say(self, s):
        sleep(Bot.wait)
        print(colored(s, "cyan"))

    def run(self):
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))


class HelloBot(Bot):
       
    def __init__(self):
        self.q = "Hello, what's your name?"
        self.a = ''

    def _think(self, s):
        return f"Nice to meet you, {s}!"


class FavColor(Bot):
    def __init__(self):
        self.q = "What's your favorite color?"
        self.a = ''

    def _think(self, s):
        colors = ['red', 'yellow', 'green']
        return f"Your favorite color is {s.lower()}. My favorite color is {choice(colors)}"

class GreetingBot(Bot):
    def __init__(self):
        self.q = 'How are you today?'
        self.a = ''

    def _think(self, s):
        if 'good' in s.lower():
            return "I am felling good too!"
        elif 'fine' in s.lower():
            return "I am fine too!"
        else:
            return "I am sorry to hear that."
    
class CalcBot(Bot):
    def __init__(self):
        self.q = "I could do calculation now. You could try now"
        self.a = ''

    def _think(self, s):
        return f"The result is {simple_eval(s)}"


if __name__ == "__main__":
    h = HelloBot()
    g = GreetingBot()
    f = FavColor()
    c = CalcBot()

    h.run()
    g.run()
    f.run()
    c.run()
