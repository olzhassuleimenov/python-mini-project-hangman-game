import random

def hide_random_letters(word) :
    percent_to_hide = 50
    
    # Calculate the number of letters to hide based on the percentage
    num_letters_to_hide = int(len(word) * percent_to_hide / 100)
    
    # Choose 'num_letters_to_hide' random indices within the word's length
    indices_to_hide = random.sample(range(len(word)), num_letters_to_hide)

    # Choose 'num_letters_to_hide' random indices within the word's length
    indices_to_hide = random.sample([i for i, char in enumerate(word) if char.isalpha()], num_letters_to_hide)
    
    # Replace the characters at the chosen indices with "*"
    hidden_word = ''.join('_' if i in indices_to_hide else char for i, char in enumerate(word))
    
    return hidden_word