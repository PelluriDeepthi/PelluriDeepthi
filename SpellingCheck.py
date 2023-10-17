from spellchecker import Spellchecker
correcter = Spellchecker()
word = input("Enter a word:")
if word in correcter:
    print("Correct")
else:
    correct_word = correcter.correction(word)
    print("Correct spelling is:", correct_word)