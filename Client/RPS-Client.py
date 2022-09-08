from os import system  # Lets us clear the terminal
from sockets import socket  # Allows us to use servers
from json import dump  # Let's us turn json data into dicts
from random import choice  # Allows the offline AI to choose a play
from colorama import init, deinit, Fore  # Adds some life to the terminal with colors

def offline_play():
    while True:
        system("cls")
        ai_play = choice(("Rock", "Paper", "Scissors")).lower()
        print(f"{Fore.GREEN}What would you like to play?")
        print(f"{Fore.YELLOW}>Rock\n>Paper\n>Scissors\n")
        player_play = input(f"{Fore.YELLOW}>>> ").lower()
        if player_play == ai_play:
            print(f"{Fore.WHITE}---\n{Fore.GREEN}{player_play.capitalize()} ties {ai_play.capitalize()}. Tied!{Fore.WHITE}\n---")
        elif player_play == "rock":
            if ai_play == "scissors":
                print(f"{Fore.WHITE}---\n{Fore.CYAN}Rock smashes Scissors. You win!{Fore.WHITE}\n---")
            else:
                print(f"{Fore.WHITE}---\n{Fore.RED}Paper covers Rock. You lose.{Fore.WHITE}\n---")
        elif player_play == "paper":
            if ai_play == "rock":
                print(f"{Fore.WHITE}---\n{Fore.CYAN}Paper covers Rock. You win!{Fore.WHITE}\n---")
            else:
                print(f"{Fore.WHITE}---\n{Fore.RED}Scissors cuts Paper. You lose.{Fore.WHITE}\n---")
        elif player_play == "scissors":
            if ai_play == "paper":
                print(f"{Fore.WHITE}---\n{Fore.CYAN}Scissors cuts Paper. You win!{Fore.WHITE}\n---")
            else:
                print(f"{Fore.WHITE}---\n{Fore.RED}Rock smashes Scissors. You lose.{Fore.WHITE}\n---")
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
  
  
def main_menu(game_version):
    while True:
        print(f"{Fore.GREEN}Rock Paper Scissors (v{game_version})")
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
    main_menu("0.5")
    print(f"{Fore.RED}Thank you for playing!\nExiting...")
    deinit()
