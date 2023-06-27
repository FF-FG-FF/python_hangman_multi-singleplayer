import random

choice = input("Do you Want to play Multiplayer ( Y / N)")

#determines between Multiplayer and Singleplayer and carries out correct tasks for mode chose
if choice == "y" or choice == "Y":
    hidden_word = input("Type in a word for the other player to guess: ")
    max_attempts = int(input("Enter the max number of attempts for the other player: "))
elif choice == "n" or choice == "N":
    group_items = ["youtube", "fruit", "food", "trucks", "cars", "cartoons", "laptop", "playstation",
                    "numbers", "school", "lobster", "america", "polish", "coconut","python", 
                    "wheels", "iphone", "university", "fortune","cornerstone","concrete","four"]
    random.shuffle(group_items)
    hidden_word = group_items[0]
    print("Currently Playing in Single Player!")
    max_attempts = 6
else:
    print("Invalid choice Please Try again")
    
    
word_length = len(hidden_word)

#initialize variables
attempts = 0
incorrect_guesses = []

#creates a list of underscores(or whats inside the quotes)
word_disguise = ["_" for i in range(word_length)]

while True:
    #joins the underscores together with whats inside the quotes
    word_display = " ".join(word_disguise)
    
    print(f"The Word has {word_length} letters")
    print(word_display)
    
    guess = input("Take A Guess At the Word(type one letter): ")
    
    if guess in hidden_word:
        #tracks correct guesses
        for i in range(word_length):
            if guess == hidden_word[i]:
                word_disguise[i] = guess
    else:
        #tracks incorrect guesses
        attempts += 1
        incorrect_guesses.append(guess)
        print(f"Incorrect guess {', '.join(incorrect_guesses)}")
     
    #checks if the  player has won 
    if "_" not in word_disguise:
        print("Congrats you guessed the word correctly")
        break
    elif attempts == max_attempts:
    #checks if the player has lost
        print(f"Sorry You have Hit the max number of attempts {max_attempts}")
        break
    
print("GAME OVER")    