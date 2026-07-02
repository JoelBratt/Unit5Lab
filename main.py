"""
Word Counter
Joel Bratt
Counts Words in document
7/2/2026
"""
import string
from pathlib import Path

class WordAnalyzer:
    def __init__(self, filepath):
        # stores filepath
        self.__filepath = Path(filepath)
        # holds the word occurances
        self.__frequencies = {}

    def process_file(self):
        # checks if the file is there
        if not self.__filepath.exists():
            return False
            
        try:
            #encoding to prevent errors and "r" for read mode
            with self.__filepath.open('r', encoding='utf-8') as file:
                
                extended_punctuation = string.punctuation
                translator = str.maketrans('', '', extended_punctuation)
                
                for line in file:
                    # turns to lowercase
                    clean_line = line.translate(translator).lower()
                    
                    # spits into words
                    words = clean_line.split()
                    
                    for word in words:
                        self.__frequencies[word] = self.__frequencies.get(word, 0) + 1
            return True
            
        except FileNotFoundError:
            # deals with file not being there
            print(f"Error: Could not find '{self.__filepath.name}'.")
            return False
    def print_report(self):
        # alphabetical sort for the words
        sorted_words = sorted(self.__frequencies.keys())
        for word in sorted_words:
            # sperates the word from the :
            print(f"{word:<10} :: {self.__frequencies[word]}")




