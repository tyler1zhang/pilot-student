from bot import *


class Garfield:
    def __init__(self):
        self.bots = []

    def add(self, bot):
        self.bots.append(bot)

    def run(self):
        print(f"Hi, this is Garfield dialog bot. Let's chat!")
        for bot in self.bots:
            bot.run()


if __name__ == "__main__":
    garfield = Garfield()
    garfield.add(HelloBot())
    garfield.add(GreetingBot())
    garfield.add(FavColor())
    garfield.add(CalcBot())
    garfield.run()