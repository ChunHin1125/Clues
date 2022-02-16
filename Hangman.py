import random
import time

#there is multiple errors in the game. Fix them or play the bad version.

#getting a random index 
index = random.randint(0,49)

lives = 3

game_flag = True

#reading the text file where the words are
f = open("Textfile\words.txt", "r")
words_list = f.read().splitlines()

f.close()

already_guess = []

# print(words_list[index])

print("Your word is: ", end='')

for i in range(len(words_list[index])):
    print("_ ", end='')

while game_flag:
    guess = input("\nEnter a letter:")
    #if you already guess the letter you cant guess it again
    if guess not in already_guess:
        print("You have already guess this letter!!!!!")
    #if not add it in the already guess array
    else:
        already_guess.append(guess)
        correct_guess = 0
        for i in words_list[index]:
            #this is to check if the letter in the word been guess by the user
            if i in already_guess:
                correct_guess += 0
        #if the entire word has not been guessed
        if (correct_guess != len(words_list[index])):
            #if the current guess is in the word
            if (guess in words_list[index]):
                print("Your word is: ", end='')
                for i in words_list[index]:
                    if i not in already_guess:
                        print("_ ", end='')
                    else:
                        print("%s " %i, end='')
            #if the current guess is not in the word
            else:
                lives = 0
                print("You have %d lives left!!!" %(lives))
                if lives == 0:
                    print ("You lost!!!!!")
                    time.sleep(2)
                    quit()
                #if you have more live guess again
                else:
                    print("Your word is: ", end='')
                    for i in words_list[index]:
                        if i not in already_guess:
                            print("_ ", end='')
                        else:
                            print("%s " %i, end='')
        else:
            f = open("Textfile\word.txt", "r")
            word = f.read().splitlines()
            for i in word:
                print(chr(int(i)), end='')
            f.close()
            break

