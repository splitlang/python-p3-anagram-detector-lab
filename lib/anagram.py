# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []
        sorted_word = sorted(self.word)

        for anagram in possible_anagrams:
            anagram = anagram.lower()
            sorted_anagram = sorted(anagram)

            if sorted_word == sorted_anagram:
                matches.append(anagram)

        return matches