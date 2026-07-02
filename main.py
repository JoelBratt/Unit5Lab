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
                    # turns to lowercase and does one line at a time to save on ram
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

def main():
    # The directory of the files
    files_dict = {
        "1": Path("princess_mars.txt"),
        "2": Path("Tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt")
    }
        # the loop for the program
    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        
        for key, path in files_dict.items():
            # Makes the name not horrible to read within menu
            formatted_name = path.stem.replace('_', ' ').title()
            print(f"{key}. {formatted_name}")
            
        print("5. Exit")
        
        # gets users input .strip turns it into a string
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '5':
            print("\nGoodbye!")
            break
            
        # validates then executes
        elif choice in files_dict:
            selected_file = files_dict[choice]
            print(f"\nProcessing '{selected_file.name}'...\n")
            
            # makes and instance of the wordanalyzer
            analyzer = WordAnalyzer(selected_file)
            
            # makes the report if it is successful
            if analyzer.process_file():
                analyzer.print_report()
            else:
                print(f"Failed to process '{selected_file.name}'. Please ensure the file exists in the directory.")
                
            input("\nPress Enter to return to the menu... ")
        else:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu... ")

if __name__ == "__main__":
    main()



