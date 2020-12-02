
from random import randint

guesses = 0

# print('What is your name?')
playName = None
while True:
    playName = input('What is your name? \n')
    if len(playName) > 0:
        break

secret = randint(1,21)

while True:
    guess = int(input('Guess a number between one and twenty! \n'))
   
    if guess > 0 and guess < 20:
        if guess < secret:
            print('Your guess is too low')
        elif guess > secret:
            print('Your guess is too high')
        else:
            print(f'Good job {playName} you guessed it correctly in {guesses} tries')
            break
        guesses += 1
    if guesses > 6:
        print(f'Sorry {playName} you could not guess my number {secret}')
