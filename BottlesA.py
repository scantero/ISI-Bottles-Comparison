class Bottles:

    def verse(self, n = None):
        return "{0} bottle{1}".format(("No more" if n == 0 else n), ("s" if n != 1 else "")) + \
            " of beer on the wall, " + \
            "{0} bottle{1} of beer.\n".format(('no more' if n == 0 else n),("s" if n != 1 else "")) + \
            "{0}, ".format("Take {0} down and pass it around".format("one" if n > 1 else "it") if n > 0 else "Go to the store and buy some more") + \
            "{0} bottle{1}".format((99 if n-1 < 0 else 'no more' if n-1 == 0 else n-1), ("s" if n-1 != 1 else "")) + \
            " of beer on the wall.\n"

    def verses(self, last, first):
        o = self.verse(last)
        for i in range (last-1, first-1, -1):
            o += "\n" + self.verse (i)

        return o


    def song(self):
        return self.verses(99,0)
