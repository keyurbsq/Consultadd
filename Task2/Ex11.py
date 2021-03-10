counter = 1
while counter <= 5:
    guessNumber = int(input('Please enter your lucky number:'))
    print('Your', counter, 'guessed number is', guessNumber)
    if guessNumber == 10:
        print('Good guess!')
        break
    elif not guessNumber:
        print('Sorry but that was not very successful')
    else:
        print('Try again!')
    if counter == 5:
        print('Game Over!')
    counter = counter + 1