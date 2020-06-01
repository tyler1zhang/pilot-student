from bot_v2 import *

class Garfield:
    def __init__(self):
        self.bots = []
        
    def add(self, s):
        self.bots.append(s)
        return None

    def run(self):
        print("Hi! this is Garfield dialog system.")
        for bot in self.bots:
            bot.run()

if __name__ == "__main__":
    g = Garfield()

    g.add(HelloBot())
    g.add(GreetingBot())
    g.add(FavColor())
    g.add(CalcBot('looped'))

    g.run()