# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, word):
        anagrams = []
        for w in word:
            if w != self.word and sorted(w) == sorted(self.word):
                anagrams.append(w)
        return anagrams        
