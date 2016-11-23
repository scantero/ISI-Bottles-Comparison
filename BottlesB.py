class Bottles:
    NoMore = lambda verse: \
        "No more bottles of beer on the wall, " + \
        "no more bottles of beer.\n" + \
        "Go to the store and buy some more, " + \
        "99 bottles of beer on the wall.\n"

    LastOne = lambda verse: \
        "1 bottle of beer on the wall, " + \
        "1 bottle of beer.\n" + \
        "Take it down and pass it around, " + \
        "no more bottles of beer on the wall.\n"

    Penultimate = lambda verse: \
        "2 bottles of beer on the wall, " + \
        "2 bottles of beer.\n" + \
        "Take one down and pass it around, " + \
        "1 bottle of beer on the wall.\n"

    Default = lambda verse: \
        "{0} bottles of beer on the wall, ".format(verse.number) + \
        "{0} bottles of beer.\n".format(verse.number) + \
        "Take one down and pass it around, " + \
        "{0} bottles of beer on the wall.\n".format(verse.number - 1)

    def song(self):
        return self.verses(99, 0)

    def verses(self, finish, start):
        o = self.verse(finish)
        for verse_number in range (finish - 1, start - 1, -1):
            o += "\n" + self.verse(verse_number) 
        return o


    def verse(self, number):
        return self.verse_for(number).text()

    def verse_for(self, number):
        if  number == 0:
            return Verse(number, Bottles.NoMore)
        elif number == 1:
            return Verse(number, Bottles.LastOne)
        elif number == 2:
            return Verse(number, Bottles.Penultimate)
        else:
            return Verse(number, Bottles.Default)            

class Verse:
    def __init__(self, number, lyrics):
        self.number = number
        self._lyrics = lyrics

    def text(self):
        return self._lyrics(self)

        
