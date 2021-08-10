"""Word Finder: finds random words from a dictionary."""

from random import randint
class WordFinder:
    ...
    def __init__(self):
        file = open('words.txt', 'r')
        self.lines = file.read().splitlines()
    def random(self):
        index = randint(0, len(self.lines))
        return self.lines[index]
