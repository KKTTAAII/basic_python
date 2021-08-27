def print_upper_words(words, must_start_with):
    """ For a list of words, this will print out the words that start with the letter(s) in
    must_start_with only.
    
    The words will be printed in all uppercase """
    
    for word in words:
        for letter in must_start_with:
            if word[0] == letter.lower() or word[0] == letter.upper():
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"g", "y"})

