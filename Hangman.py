import random

#getting a random index 
index = random.randint(0,49)


#reading the text file where the words are
f = open("words.txt", "r")
words_list = f.read().splitlines()

already_guess = []
correct_guess = []

print(chr(97) + chr(110) + chr(115) + chr(119) + chr(101) + chr(114) + chr(32) + chr(105) + chr(110) + chr(32) + chr(119) + chr(111) + chr(114) + chr(107) + chr(115) + chr(104) + chr(101) + chr(101) + chr(116)) 

print(words_list[index])

