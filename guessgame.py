import  random 

min = 1
max = 100

def number_guessing_game():
    number = random.randint(min,max)

    player_name = input("Hello, what's your name")
    no_guess = 0 

    print(f" okay, +{ player_name}+ ! iam  guessing a  number  between {min} and  {max}: ")

    while no_guess < 7:
        guess = int(input())

        no_guess += 1

        if guess < number:

            print('Your guess is  too  low')

        elif guess > number:

            print('Your guess  is  too  high')

        else:

            break
    if guess == number:

        print(f"congratulation {player_name} you guessed  rhe  number in{no_guess} tries")

    else:

        print(f" sorry {player_name} you did not guess the  number, And  the  number  is {number} ")


number_guessing_game()





    
