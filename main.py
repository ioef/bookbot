
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for ch in text:
        if not ch.isalpha() : continue
        ch = ch.lower()
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] +=1 

    return letters

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    print(" --- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document\n")
    
    
    lettersDict = count_letters(file_contents)

    for w in sorted(lettersDict, key=lettersDict.get, reverse=True):
        print(f"The '{w}' character was found {lettersDict[w]} times")

    print("\n--- End report ---")