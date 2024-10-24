import io
from pprint import pprint

class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding="utf-8") as file:
                all_line = []
                for line in file:
                    line_low = line.lower()
                    words = line_low.split()
                    all_line += words
                all_words[i] = all_line
        print(all_words)

a = WordsFinder("1.txt", "2.txt", "3.txt")
words_dict = a.get_all_words()
