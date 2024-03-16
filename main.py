def main():
    path = "./books/frankenstein.txt"
    book = getBook(path)
    wordCount = countWords(book)
    letters = countLetters(book)
    generateReport(path, wordCount, letters)

def getBook(path):
    with open(path) as b:
        return b.read()

def generateReport(path, wordCount, letters):
    print(f"--- Begin report of {path} ---")
    print(f"{wordCount} words found in the document\n")
    listOfLetters = [{key: value} for key, value in letters.items()]
    listOfLetters.sort(reverse=True, key=getDictionaryValue)
    for letter in listOfLetters:
        for key, value in letter.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End Report ---")

def getDictionaryValue(d):
    for key in d:
        return d[key]
    

def countWords(book):
    words = book.split()
    return len(words)

def countLetters(book):
    # Only count letters, not all characters.
    letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0,"f": 0,"g": 0,"h": 0,"i": 0,"j": 0,"k": 0,"l": 0,"m": 0,"n": 0,"o": 0,"p": 0,"q": 0,"r": 0,"s": 0,"t": 0,"u": 0,"v": 0,"w": 0,"x": 0,"y": 0,"z": 0}
    l = list(book)
    for letter in l:
        ll = letter.lower()
        if ll in letters:
            letters[ll] += 1
    return letters
            

main()