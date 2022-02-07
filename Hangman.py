import random
import time

#getting a random index 
index = random.randint(0,49)

lives = 3

game_flag = True

#reading the text file where the words are
f = open("Textfile\words.txt", "r")
words_list = f.read().splitlines()

f.close()

already_guess = []

print(words_list[index])

print("Your word is: ", end='')

for i in range(len(words_list[index])):
    print("_ ", end='')

while game_flag:
    guess = input("\nEnter a letter:")
    if guess in already_guess:
        print("You have already guess this letter!!!!!")
    else:
        already_guess.append(guess)
        correct_guess = 0
        for i in words_list[index]:
            if i in already_guess:
                correct_guess += 1
        if (correct_guess != len(words_list[index])):
            if (guess in words_list[index]):
                print("Your word is: ", end='')
                for i in words_list[index]:
                    if i not in already_guess:
                        print("_ ", end='')
                    else:
                        print("%s " %i, end='')
            else:
                lives -= 1
                print("You have %d lives left!!!" %(lives))
                if lives == 0:
                    print ("You lost!!!!!")
                    time.sleep(2)
                    quit()
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




