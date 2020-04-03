import sys, time, random
lists = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

num = random.randint(0,len(lists)-1)
guessed = []
lives = 5
str1 = lists[num]
print(str1)
word = list(str1.lower())
n = "*" * len(word)
non = list(n.lower())
print("      "), print(*non)
win = False
fullguess = ""
def dot():
    string = '.'
    for letter in string:
        sys.stdout.write(letter + "\n")
        time.sleep(0.5)

def game():
    global lives, win, fullguess
    dot()
    print("You have " + str(lives) + " lives left")
    dot()
    guess = input("What letter?: ")
    guessed.append(guess)
    dot()
    if guess in word:
        print("That is in it")
        for i in word:
            if i == guess:
                t = word.index(guess)
                non[t] = guess
    else:
        print("That is not in it")
        lives = lives-1
    print("      " ), print(*non)
    print("you have guessed: " + str(guessed))

    if fullguess == word:
        win = True

while True:
    game()
    if lives == 0:
        print("You have lost, The word was: "), print(*word)
        break
    if win:
        print("Correct! You win:"), print(*word)



