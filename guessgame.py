import  random 
# Initializing  the min and max
min = 1
max = 500

def number_guessing_game():
    # Selecting the  random  number in the  between  min  and  max
    number = random.randint(min,max)
    player_name = input("Hello, what's your name")
    no_guess = 0  # initializing  the guess count
    print(f" okay, +{ player_name}+ ! iam  guessing a  number  between {min} and  {max}: ")

    while no_guess < 7:
        #taking the  user  input  in guessing the number
        guess = int(input())
        no_guess += 1
        if guess < number:
            print('Your guess is  too  low')
        elif guess > number:
            print('Your guess  is  too  high')
        else:
            break
    if guess == number:
         print(f"congratulation {player_name} you guessed the number in{no_guess} tries, And  the  number  is {guess}")
    else:
        print(f" sorry {player_name} you did not guess the  number, And  the  number  is {number} ")


number_guessing_game()





    
