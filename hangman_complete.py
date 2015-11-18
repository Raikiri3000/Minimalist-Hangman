import random
import os

def GetAnswerWithUnderscores(answer, letters_guessed):
    word = ''
    for c in answer:
        if c in letters_guessed:
            word += c
        else:
            word += '_'
    return word

def GetWordSeparatedBySpaces(word):
    new_string = ''
    for c in range(len(word)):
        new_string += word[c]
        if c == len(word) - 1:
            break
        new_string += ' '
    return new_string

def IsWinner(answer, letters_guessed):
    word = GetAnswerWithUnderscores(answer, letters_guessed)
    if word == answer:
        return True
    else:
        return False

def IsLegalGuess(current_guess, letters_guessed):
    if current_guess in letters_guessed:
        return 'This letter was previously guessed'
    if len(current_guess) > 1:
        return 'This is not a single letter'
    return 'yes'

def GetLegalGuess(letters_guessed):
    guess = input('Guess a letter: ')
    ans = IsLegalGuess(guess, letters_guessed)
    if ans != 'yes':
        print(ans)
        guess = GetLegalGuess(letters_guessed)
    return guess

def IsGuessRevealing(answer, legal_letter_guess):
    if legal_letter_guess in answer:
        return True
    return False

def GetAllEnglishWords():
    l = []
    fin = open('hangman_english_words.txt')
    for line in fin:
        word = line.strip()
        l.append(word)
    return l

def GetRandomWord(words):
    num = random.randint(1, len(words) - 1)
    return words[num]

def Play(answer):
    strikes = 0
    winner = False
    letters_guessed = ''
    display = GetWordSeparatedBySpaces(GetAnswerWithUnderscores(answer, letters_guessed))
    while True:
        if strikes > 5 or winner == True:
            break
        print('You have ', strikes, ' strikes')
        print(display)
        guess = GetLegalGuess(letters_guessed)
        if IsGuessRevealing(answer, guess) == False:
            strikes += 1
            print('Sorry, no')
            letters_guessed += guess
            continue
        letters_guessed += guess
        display = GetWordSeparatedBySpaces(GetAnswerWithUnderscores(answer, letters_guessed))
        if IsWinner(answer, letters_guessed) == True:
            winner = True
    if winner != True:
        print('The word was ', answer)
    else:
        print(answer)
        print('Congratulations!')
    return winner

def GetPlayRecord():
    fin = open('hangman_play_record.txt')
    line = fin.readline()
    line = line.strip()
    l = line.split(',')
    for i in range(len(l)):
        l[i] = int(l[i])
    return l

def RecordPlay(win):
    l = GetPlayRecord()
    fout = open('hangman_play_record.txt', 'w')
    if win == True:
        l[0] = l[0] + 1
    l[1] = l[1] + 1
    wins = str(l[0])
    plays = str(l[1])
    line = wins + ',' + plays
    fout.write(line)

def StartupAndPlay():
    words = GetAllEnglishWords()
    wl = GetPlayRecord()
    print('So far, you have won ', wl[0], ' out of ', wl[1], ' games')
    print('Welcome back')
    input('Press Enter')
    while True:
        os.system('cls')
        wl = GetPlayRecord()
        print('So far, you have won ', wl[0], ' out of ', wl[1], ' games')
        answer = GetRandomWord(words)
        win = Play(answer)
        RecordPlay(win)
        rep = input('Play again? (Y/N): ')
        rep = rep.upper()
        if rep == 'N':
            break

if __name__ == "__main__":
    # execute only if run as a script
    StartupAndPlay()
