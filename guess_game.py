import os # to change the working directory
import pygame # to play music
import random # to generate a random number

def get_path(filename):
    """Get the path to the given filename."""
    return os.path.join(os.path.dirname(__file__), filename)

# Get the paths to the mp3 files
correct = get_path('correct.mp3')
incorrect = get_path('incorrect.mp3')
lets_go = get_path('lets-go.mp3')
bye = get_path('bye.mp3')

# Initial high score
high_score = float('inf')

def play_game(max_guesses): 
    # Play the guessing game with the given number of maximum guesses
    global high_score
    secret_number = random.randint(1, 100)
    num_guesses = 0
    
    while num_guesses < max_guesses: # Loop until the user runs out of guesses
        # Ask the user to guess the number
        try:
            guess = input("Guess the number (between 1 and 100): ")
            if guess == 'quit':
                print("Quitting the game...")            
                return
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Invalid input. Please enter a number between 1 and 100.")
                continue
        except ValueError: # If the user enters a non-integer, print an error message
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        
        num_guesses += 1
        
        # Provide feedback to the user
        if guess < secret_number:
            print("You guessed too low!")
        elif guess > secret_number:
            print("You guessed too high!")
        else:
            print(f"Congratulations, you guessed the number in {num_guesses} guesses!") # Print a message if the user guessed the number
            
            if num_guesses < high_score: # Check if the user got a new high score
                high_score = num_guesses
                print(f"New high score: {high_score}! Wow!")
            pygame.mixer.music.load(correct) # Load the mp3 file
            pygame.mixer.music.play() # Play the song
            while pygame.mixer.music.get_busy():
                continue # Wait for the song to finish playing before proceeding
            return
    
    print(f"Sorry, you did not guess the number. The number was {secret_number}.") # Print a message if the user ran out of guesses
    pygame.mixer.music.load(incorrect)
    pygame.mixer.music.play() 
    while pygame.mixer.music.get_busy():
        continue 
    
def main():
    global high_score 
    
    pygame.init() # Initialize pygame
    
    print("Welcome to the guessing game!")
    print("I'm choosing a number between 1 and 100. Can you guess what it is?")
    print("You can choose the difficulty level: easy, medium, or hard. Easy has unlimited guesses, medium has 10 guesses, and hard has 5 guesses or you can type 'quit' to exit.")
    
    while True:
        # Ask the user to choose the difficulty level
        level = input("Choose difficulty level: easy, medium, hard, or quit: ")
        if level.lower() == 'easy':
            max_guesses = float('inf')
            print("You have unlimited guesses!")
        elif level.lower() == 'medium':
            max_guesses = 10
            print("You have 10 guesses.")
        elif level.lower() == 'hard':
            max_guesses = 5
            print("You have 5 guesses.")
        elif level.lower() == 'quit':
            print("Quitting the game...")
            pygame.mixer.music.load(bye)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            break
        else:
            print("Invalid input. Please choose a valid difficulty level or type 'quit' to exit.")
            continue
        
        play_game(max_guesses)
    
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            pygame.mixer.music.load(lets_go)
            pygame.mixer.music.play() 
            while pygame.mixer.music.get_busy():
                continue
            print("Alright, let's play again! Try this time to guess the number in less guesses than before.")
        elif play_again.lower() == "no": 
            print("Thanks for playing! See you next time!")
            print("This program was coded by Farzan Vahidiankamyar for the final project of the course 'KI in der Logistik'.")
            pygame.mixer.music.load(bye)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == '__main__':
    main()