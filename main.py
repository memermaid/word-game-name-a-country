import random
import csv

countries_used = []


# Introduction to the game, basic rules.
def intro():
    print('Welcome to the "Name a country" game!')
    print('\nYou are playing against AI. Rules are simple.')
    print('\nPlayer/AI enters the name of any country.')
    print('\nAI/Player must name the country starting with the last letter of the previous country.')
    print('\nFor example: \nPlayer1 => Costa Rica \nPlayer2 => Austria \nPlayer1 => Aruba \nPlayer2 => Australia \netc')
    print('\nFirst turn will be determined by the winner of "Rock, Scissors, Paper".')
    print('\nIf you want to stop the game, just enter "STOP".')
    print('\nGood luck!\n')


# Game Rock, Scissors, Paper to define whose the first move
def rock_scissors_paper():
    human_move = get_human_move()
    while not human_move:
        print("Invalid input. Try again! ")
        human_move = get_human_move()
    ai_move = get_ai_move()
    winner = get_winner(ai_move, human_move)
    while winner == 'tie':
        print("It was a tie. Let's try again!")
        print()
        human_move = get_human_move()
        while not human_move:
            print("Invalid input. Try again! ")
            human_move = get_human_move()
        ai_move = get_ai_move()
        winner = get_winner(ai_move, human_move)
    return winner


# Gets AI move for Rock, Scissors, Paper
def get_ai_move():
    ai_move = random.choice(["scissors", "rock", "paper"])
    return ai_move


# Gets human move
def get_human_move():
    human_move = input("What do you play? Rock, Scissors or Paper? ").lower()
    # print()
    # if is_valid_move(human_move):
    #     return human_move
    # else:
    #     return False
    while not is_valid_move(human_move):
        print("Invalid input. Try again! ")
        human_move = input("What do you play? Rock, Scissors or Paper? ").lower()
    return human_move


# Checks if the input move is only Rock, Scissors or Paper
def is_valid_move(move):
    if move == 'rock':
        return True
    elif move == 'scissors':
        return True
    elif move == 'paper':
        return True
    return False


# Returns the winner of Rock, Scissors, Paper
def get_winner(ai_move, human_move):
    if ai_move == human_move:
        return "tie"
    elif ai_move == "rock":
        if human_move == "scissors":
            return "ai"
        elif human_move == "paper":
            return "human"
    elif ai_move == "scissors":
        if human_move == "rock":
            return "human"
        elif human_move == "paper":
            return "ai"
    elif ai_move == "paper":
        if human_move == "scissors":
            return "human"
        elif human_move == "rock":
            return "ai"


# Checks if input country exists
def is_valid(player_country):
    with open("countries.csv") as f:
        reader = csv.reader(f)
        all_countries = list(reader)
        if any(player_country in country for country in all_countries):
            return True


# Checks if input country has not been already used
def is_used(player_country):
    if any(player_country in country for country in countries_used):
        return True


# Plays the game "Name a country"
def play_game(human_country, ai_country):
    with open("countries.csv") as f:
        reader = csv.reader(f)
        all_countries = list(reader)
        while human_country.lower() != "stop":
            human_country = input("Enter a country: ").capitalize()
            if human_country.lower() == "stop":
                print("AI won!")
                break
            if not is_valid(human_country):
                print("Wrong entry. You should name a valid country.\n")
                continue
            if human_country[0].lower() != ai_country[0][-1].lower():
                print("Wrong answer. Country name should start with the last letter of the country " + str(
                    ai_country[0][-1]).capitalize() + ".")
                continue
            if is_used(human_country):
                print("Country was already used.")
                print()
                print("AI won!")
                break
            else:
                countries_used.append(human_country)

            ai_country = random.choice(list(all_countries))
            while ai_country[0][0].lower() != human_country[-1].lower():
                ai_country = random.choice(list(all_countries))
            if is_used(ai_country[0]):
                print("Ai names", ai_country[0], "which was already used.")
                print("You won!")
                break
            else:
                countries_used.append(ai_country)
                print("AI names", ai_country[0])
                print()


def main():
    intro()
    first_player = rock_scissors_paper()
    with open("countries.csv") as f:
        reader = csv.reader(f)
        all_countries = list(reader)
        if first_player == 'human':
            print("You won! You name the first country.")
            print()

            human_country = input("Enter a country: ").capitalize()
            while not is_valid(human_country):
                human_country = input("Wrong entry. Please enter a valid country: ").capitalize()
            countries_used.append(human_country)

            ai_country = random.choice(list(all_countries))
            while ai_country[0][0].lower() != human_country[-1].lower():
                ai_country = random.choice(list(all_countries))
            print("AI names", ai_country[0])
            print()
            countries_used.append(ai_country)

        if first_player == 'ai':
            print("AI won! AI names the first country.")
            print()
            ai_country = random.choice(all_countries)
            countries_used.append(ai_country)
            print("It is:", ai_country[0])
            print()
            human_country = ''
        play_game(human_country, ai_country)


if __name__ == '__main__':
    main()
