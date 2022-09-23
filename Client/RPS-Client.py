from os import system  # Lets us clear the terminal
from socket import socket  # Allows us to use servers
from json import loads, dumps  # Let's us turn json data into dicts
from random import choice  # Allows the offline AI to choose a play
from colorama import init, deinit, Fore  # Adds some life to the terminal with colors


def offline_play():
    while True:
        system("cls")
        ai_play = choice(("Rock", "Paper", "Scissors")).lower()
        print(f"{Fore.GREEN}What would you like to play?")
        print(f"{Fore.YELLOW}>Rock\n>Paper\n>Scissors\n")
        player_play = input(f"{Fore.YELLOW}>>> ").lower()
        system("cls")
        if player_play == ai_play:
            print(f"{Fore.GREEN}{player_play.capitalize()} ties {ai_play.capitalize()}. Tied!")
        elif player_play == "rock":
            if ai_play == "scissors":
                print(f"{Fore.CYAN}Rock smashes Scissors. You win!")
            else:
                print(f"{Fore.RED}Paper covers Rock. You lose.")
        elif player_play == "paper":
            if ai_play == "rock":
                print(f"{Fore.CYAN}Paper covers Rock. You win!")
            else:
                print(f"{Fore.RED}Scissors cuts Paper. You lose.")
        elif player_play == "scissors":
            if ai_play == "paper":
                print(f"{Fore.CYAN}Scissors cuts Paper. You win!")
            else:
                print(f"{Fore.RED}Rock smashes Scissors. You lose.")
        else:
            continue
        while True:
            print(f"{Fore.GREEN}Play again?")
            print(f"{Fore.YELLOW}>Yes\n>No\n")
            replay_choice = input(f"{Fore.YELLOW}>>> ").lower()
            if replay_choice == "yes":
                break
            elif replay_choice == "no":
                system("cls")
                return
            else:
                system("cls")
                continue


def online_join():
    pass


def private_join():
    pass
  
  
def main_menu():
    game_version = "0.5"
    while True:
        print(f"{Fore.GREEN}Rock Paper Scissors v{game_version}")
        print(f"{Fore.YELLOW}Play Offline\nPlay Online\nJoin Room\nExit\n")
        choice = input(f"{Fore.YELLOW}>>> ").lower()
        if choice == "play offline":
            offline_play()
        elif choice == "play online":
            online_join()
            pass
        elif choice == "join room":
            private_join()
            pass
        elif choice == "exit":
            system("cls")
            return
        else:
            system("cls")
            continue


if __name__ == "__main__":
    system("cls")
    init(autoreset=True)
    main_menu()
    print(f"{Fore.RED}Thank you for playing!\nExiting...")
    deinit()

"""
Debating adding supporting scripts to the client to make the code much cleaner
I usually would but this is intended to be as clean as possible for users with little coding knowledge
Realistically, you would have to setup python, run the requirements file, etc.
The whole "little coding knowledge" thing is already out the window
"""
