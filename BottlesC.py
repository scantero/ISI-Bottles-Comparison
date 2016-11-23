class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, bottles_at_start, bottles_at_end):
        o = self.verse(bottles_at_start)
        for bottles in range (bottles_at_start - 1, bottles_at_end - 1, -1):
            o += "\n" + self.verse(bottles) 
        return o

    def verse(self, bottles):
        return str(Round(bottles))

class Round:
    def __init__(self, bottles):
        self.bottles = bottles

    def __str__(self):
        return self.challenge() + self.response()

    def challenge(self):
        return \
            self.bottles_of_beer().capitalize() + " " + self.on_wall() + ", " + \
            self.bottles_of_beer() + ".\n"

    def response(self):
        return \
            self.go_to_the_store_or_take_one_down() + ", " + \
            self.bottles_of_beer() + " " + self.on_wall() + ".\n"

    def bottles_of_beer(self):
        return \
            "{0} {1} of {2}".format(self.anglicized_bottle_count(), self.pluralized_bottle_form(), self.beer())

    def beer(self):
        return "beer"

    def on_wall(self):
        return "on the wall"
    
    def pluralized_bottle_form(self):
        return "bottle" if self.last_beer() else "bottles"

    def anglicized_bottle_count(self):
        return "no more" if self.all_out() else str(self.bottles)

    def go_to_the_store_or_take_one_down(self):
        if self.all_out():
            self.bottles = 99
            lyrics = self.buy_new_beer()
        else:
            lyrics = self.drink_beer()
            self.bottles -= 1

        return lyrics

    def buy_new_beer(self):
        return "Go to the store and buy some more"

    def drink_beer(self):
        return "Take {0} down and pass it around".format(self.it_or_one())

    def it_or_one(self):
        return "it" if self.last_beer() else "one"

    def all_out(self):
        return self.bottles == 0

    def last_beer(self):
        return self.bottles == 1

        

