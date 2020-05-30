from time import sleep
from simpleeval import simple_eval
from termcolor import colored
from random import choice

# Defind the Base class
class Bot:

    wait_time = 1

    def __init__(self, runtype = 'once'):
        self.q = ''
        self.a = ''
        self.runtype = runtype

    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'cyan')

    def run(self):
        sleep(Bot.wait_time)
        print(self._format(self.q))

        while True:
            self.a = input().lower()
            sleep(Bot.wait_time)
            if self.runtype == 'once':
                print(self._format(self._think(self.a)))
                break
            elif self.a in ['x', 'q', 'exit', 'quit', 'no']:
                print("See you next time! Bye!")
                break
            else:
                print(self._format(self._think(self.a)))

class HelloBot(Bot):
    def __init__(self):
        super().__init__()
        self.q = 'Hi, what is your name?'

    def _think(self, s):
        return f"Hello, {s}!"

class GreetingBot(Bot):
    def __init__(self):
        super().__init__()
        self.q = "How are you feeling today?"
    
    def _think(self, s):
        if 'good' in s:
            return "I am feeling good too!"
        elif 'great' in s:
            return "I am feeling great too!"
        else:
            return "I'm sorry to hear that."

class FavColorBot(Bot):
    def __init__(self):
        super().__init__()
        self.q = "What is your favorite color?"

    def _think(self, s):
        colors = ['red', 'yellow', 'green', 'blue', 'pink', 'grey', 'purple', 'white']
        return f"You like {s}? My favorite color is {choice(colors)}."

class CalculateBot(Bot):
    def __init__(self, runtype = 'loop'):
        self.runtype = runtype
        self.q = "Hi, i could do calculation now. You could try now!"

    def _think(self, s):
        return f"The result is {simple_eval(s)}. Do you want to try again?"
        
    # add the loop run() in Base class
    # def run(self):
        # sleep(Bot.wait_time)
        # print(self._format(self.q))
        
        # while True:
        #     self.a = input()
        #     sleep(Bot.wait_time)
        #     if self.a in ['x', 'q', 'exit', 'quit']:
        #         print("See you next time! Bye!")
        #         break
        #     else:
        #         print(self._format(self._think(self.a)))
        #         sleep(Bot.wait_time)
        #         print(self._format("Let's try again!"))

# Define a class for garfield
class Garfield:

    def __init__(self, wait_time = 1):
        Bot.wait = wait_time
        self.bots = []

    def add(self, bot):
        self.bots.append(bot)

    def run(self):
        sleep(Bot.wait)
        print("Hello, I am Garfield. I'm dialog bot. Let's talk.")
        for bot in self.bots:
            bot.run()


def main():
    garfield = Garfield(1)
    garfield.add(HelloBot())
    garfield.add(GreetingBot())
    garfield.add(FavColorBot())
    garfield.add(CalculateBot())

    garfield.run()

if __name__ == "__main__": main()