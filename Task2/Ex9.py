while True:
    number = int(input('Please enter your lucky number:'))

    if number == 10:
        print('Good guess!')
        break
    else:
        answer = input('Do you want to keep continue?')
        if answer == 'no':
            break
        else:
            continue
