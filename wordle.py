import random

def random_word(length):
    with open('words_alpha.txt') as f:
        words = f.read().splitlines()
        return random.choice([i for i in words if len(i) == length])

def play_game(word, temp):
    cur_guess = temp
    guess = input("What is your guess? ('exit' to end game) ")
    if (guess == "exit"):
        return
    if (len(guess) != len(word)):
        print("Not a valid word. Try again.")
        play_game(word, temp)
    else:
        for i in range(len(word)):
            for j in range(i, len(guess)):
                if (i == j and guess[j] == word[i]):
                    #print("Correct letter at: ", i)
                    #print(guess[i], " ", word[i])
                    cur_guess = cur_guess[:i] + cur_guess[i:].replace(cur_guess[i], word[i], 1)   
                elif (word[i] == guess[j] and i!=j):
                    print("Letter", guess[j], "is in the incorrect place at", j)             
    print(cur_guess)
    if '_' not in cur_guess:
        print("Congrats! You win :D")
        return
    else:
        return play_game(word, cur_guess)

def main():
    word_length = input("Input length of word: ")
    word = random_word(int(word_length))
    #print(word)
    temp = "_" * len(word)
    play_game(word, temp)

if __name__ == "__main__":
    main()