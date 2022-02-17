import random
from collections import Counter
from nltk.tokenize import regexp_tokenize


class TextGenerator:
    punctlist = ['.', '!', '?']

    def __init__(self, filename):
        """Reading the file and making tokens"""
        with open(filename, "rt", encoding="utf-8") as corpus:
            self.wtokens = regexp_tokenize(corpus.read(), "[^ \t\n]+")
        self.trigrams = {}
        self.n = len(self.wtokens)
        for i in range(self.n-2):
            head = self.wtokens[i] + " " + self.wtokens[i+1]
            tail = self.wtokens[i+2]
            tails = self.trigrams.get(head, Counter())
            tails[tail] += 1
            self.trigrams[head] = tails

    def next_word(self, previous):
        """Generate random word based on the previous two"""
        tails = self.trigrams[previous]
        top_tail = tails.most_common(1)[0]
        return top_tail[0]

    def is_start_valid(self, token):
        """Сhecks whether the word can be the first in the sentence"""
        return token[0].isupper() and token[-1] not in TextGenerator.punctlist

    def is_last_valid(self, token):
        """Сhecks whether the word can be the last in the sentence"""
        return token[-1] in TextGenerator.punctlist

    def get_sentence(self, length=5):
        """Generates one sentence."""
        startind = random.randint(0, self.n - 2)
        start = self.wtokens[startind]
        while not self.is_start_valid(start):
            startind = random.randint(0, self.n - 2)
            start = self.wtokens[startind]
        sentence = [start] + [self.wtokens[startind + 1]]
        for i in range(length - 2):
            sentence.append(self.next_word(sentence[-2] + " " + sentence[-1]))
        last = sentence[-1]
        while not self.is_last_valid(last):
            sentence.append(self.next_word(sentence[-2] + " " + sentence[-1]))
            last = sentence[-1]

        return " ".join(sentence)


if __name__ == "__main__":
    tg = TextGenerator(filename=input())
    """Generate 10 random sentences"""
    for i in range(10):
        print(tg.get_sentence())