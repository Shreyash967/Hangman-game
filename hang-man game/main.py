import random
from hangman_words import word_list
from hangman_ascii import hangman_logo,stages

def start_game():
    a = input("Enter 'S'To Start the game:").lower()
    if a == "s":
        random_word = random.choice(word_list).lower()
        placeholder = ""
        for i in range(len(random_word)):
            placeholder += "-"
        print(placeholder)
        print(stages[6])
        lives=6
        correct_guesses =[]
        game_over = False
        while not game_over:
            print(f"You have R.lives: {lives}")
            user_choice = input("Enter your choice:").lower()
            if user_choice in correct_guesses:
                print(f"You have already guessed this word {user_choice}")
            display = ""
            for i in range(len(random_word)):
                if user_choice == random_word[i]:
                    display += random_word[i]
                    correct_guesses.append(random_word[i])
                elif random_word[i] in correct_guesses:
                   display += random_word[i]
                else:
                    display += "-"
            print(display)

            if user_choice not in random_word:
                lives -= 1
                if lives == 0:
                    game_over = True
                    print(f"the Correct Word Was {random_word}...")
                    print(" ********************** Game Over!!!! ***************************")


            if "-" not in  display :
                game_over = True
                print(f"You Guessed The Correct Word Was {display}")
                print("*********************  You Winnnn!!! *******************")
            print(stages[lives])
    else:
        print("Invalid input")
        start_game()

print("Welcome To Hangman Game : \n Description :- \n This a Popular game of hangman, In this You have 6 lives,\n You have to guess the Words before you get hanged")
print("There Will Be a Progress Bar and Remaining live Count (R.Lives:) \n That is All, Now Plz enjoy game of hangman.  ")
print(hangman_logo)
print(start_game())