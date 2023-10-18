################## Task 1 #############

while True:
    guess = input("Guess a letter: ")

    if guess.isalpha() and len(guess) == 1:
        print("Correct ")
    
        break

    else: 
        print("Invalid letter. Please, enter a single alphabetical character.")

################## Task 2 #############
# import random

# word_list = ["Apple", "Orange","Mango","Grapes","Banana"]
# random_word = random.choice(word_list)

# while True:
   
#     guess = input("Guess a letter: ")
#     if guess in random_word:
#         print(f"Good guess! {guess} is in the word {random_word}")
#         break

#     else:
#         print(f"Sorry, {guess} is not in the word. Try again.")


################## Task 3 #############
import random

def check_guess(guess):
    
    word_list = ["Apple", "Orange","Mango","Grapes","Banana"]
    random_word = random.choice(word_list)

    while True:
    
        guess = input("Guess a letter for a word: ").lower()
        if guess in random_word:
            print(f"Good guess! {guess} is in the word {random_word}")
            break

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():

    while True:
        guess = input("Guess a letter: ")

        if guess.isalpha() and len(guess) == 1:
            print("Correct ")
        
            break

        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess()


ask_for_input()