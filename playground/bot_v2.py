from random import choice
from time import sleep
from simpleeval import simple_eval
from termcolor import colored

class Bot:
    # Wait 1 second before bot say anything. 
    wait = 1

    def __init__(self, cycle = "once"):
        self.cycle = cycle
        self._question()

    def _question(self):
        self.q = ''
    
    def _think(self, s):
        return s
    
    def _say(self, s):
        sleep(Bot.wait)
        print(colored(s, 'cyan'))
    
    def run_once(self):
        self._say(self.q)
        self.a = input()
        self._say(self._think(self.a))

    def run_loop(self):
        self._say(self.q)
        self._say("When you want to quit, please type 'quit.")
        while True:
            self.a = input().lower()
            if self.a in ['quit', 'no']:
                self._say("It's nice talking with you. See you.")
                break
            else:
                self._say(self._think(self.a))
                self._say("Do you want to try again?")

    def run(self):
        if self.cycle == "once":
            self.run_once()
        elif self.cycle == 'looped':
            self.run_loop()



class HelloBot(Bot):
    def _question(self):
        self.q = "Hello, What's your name?"

    def _think(self, s):
        return f"Hi {s}, Nice to meet you."

class GreetingBot(Bot):
    def _question(self):
        self.q = "How are you today?"

    def _think(self, s):
        if 'good' in s.lower():
            return "That's good, I am good too."
        elif 'fine' in s.lower():
            return "That's nice, I am fine too."
        else:
            return "I am sorry to hear that."

class FavColor(Bot):
    def _question(self):
        self.q = "What's your favorite color?"

    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"Oh, {s} is a beautiful color. I like {choice(colors)}. "

class CalcBot(Bot):

    def _question(self):
        self.q = "Now I could do calculation. Do you want to try?"

    def _think(self, s):
        return f"Done. The result is {simple_eval(s)}"
          


if __name__ == "__main__":
    #testing code
    h = HelloBot()
    g = GreetingBot()
    f = FavColor()
    c = CalcBot('looped')

    h.run()
    g.run()
    f.run()
    c.run()