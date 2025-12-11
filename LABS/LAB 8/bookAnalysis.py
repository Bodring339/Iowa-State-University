"""
Muhammad Muhamedjonov, 11-05-2025
LAB 8, This code replaces words from a sentence with another random word from this sentence
"""

def analyzeBook(filename):
    with open(filename, "r", encoding="utf-8") as f:
        count = {}
        for line in f:
            for word in line.split():
            # remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')
                # ignore case
                word = word.lower()
                # ignore numbers
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
        return count

def outputAnalysis(count, filename):
    keys = list(count.keys())
    keys.sort()
    # save the word count analysis to a file
    with open(filename[0:len(filename) - 4] + "_analyses.txt", "w", encoding='utf-8') as out:
        for word in keys:
            if(word in count):
                out.write(word + " " + str(count[word]))
                out.write('\n')
    

def main():
    filename = input("Enter the filename (with .txt): ")

    count = analyzeBook(filename)
    outputAnalysis(count, filename)

if(__name__ == "__main__"):
    main()